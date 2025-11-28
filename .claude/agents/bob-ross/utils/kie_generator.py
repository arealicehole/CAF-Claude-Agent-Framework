#!/usr/bin/env python3
"""
Kie.ai Nano Banana Pro API Generator

A utility for generating images using the Kie.ai API.
Used by the Bob Ross multi-agent visual creation system.

Usage:
    python kie_generator.py --prompt "Your prompt" --output "output.png"
    python kie_generator.py --prompt "Edit this" --image-input "source.png" --output "edited.png"
"""

import requests
import json
import time
import os
import sys
import argparse
from pathlib import Path
from typing import Optional, List, Dict, Any


class KieAIGenerator:
    """Client for Kie.ai Nano Banana Pro API"""

    def __init__(self, api_key: Optional[str] = None, config_path: Optional[str] = None):
        """
        Initialize the Kie.ai generator.

        Args:
            api_key: Kie.ai API key (Bearer token)
            config_path: Path to config JSON file
        """
        self.config = self._load_config(config_path)
        self.api_key = api_key or self._get_api_key()
        self.base_url = self.config.get("kie_ai", {}).get("base_url", "https://api.kie.ai/api/v1")
        self.model = self.config.get("kie_ai", {}).get("model", "nano-banana-pro")

        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def _load_config(self, config_path: Optional[str] = None) -> Dict[str, Any]:
        """Load configuration from JSON file"""
        if config_path is None:
            # Default to config in same directory structure
            config_path = Path(__file__).parent.parent / "config" / "kie-config.json"

        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Warning: Config file not found at {config_path}, using defaults")
            return {}
        except json.JSONDecodeError as e:
            print(f"Warning: Invalid JSON in config file: {e}")
            return {}

    def _get_api_key(self) -> str:
        """Get API key from config or environment"""
        # First check environment variable
        env_key = os.environ.get("KIE_API_KEY")
        if env_key:
            return env_key

        # Then check config
        config_key = self.config.get("kie_ai", {}).get("api_key")
        if config_key and config_key != "YOUR_KIE_API_KEY_HERE":
            return config_key

        raise ValueError(
            "No API key found. Set KIE_API_KEY environment variable or update config/kie-config.json"
        )

    def create_task(
        self,
        prompt: str,
        aspect_ratio: str = "1:1",
        resolution: str = "2K",
        output_format: str = "png",
        image_input: Optional[List[str]] = None,
        callback_url: Optional[str] = None
    ) -> str:
        """
        Create a new image generation task.

        Args:
            prompt: Text description of the image to generate
            aspect_ratio: Output aspect ratio (1:1, 16:9, 9:16, etc.)
            resolution: Output resolution (1K, 2K, 4K)
            output_format: Output format (png, jpg)
            image_input: Optional list of image URLs for image-to-image
            callback_url: Optional webhook URL for completion notification

        Returns:
            Task ID for polling
        """
        url = f"{self.base_url}/jobs/createTask"

        payload = {
            "model": self.model,
            "input": {
                "prompt": prompt,
                "aspect_ratio": aspect_ratio,
                "resolution": resolution.upper(),  # API requires uppercase
                "output_format": output_format,
                "image_input": image_input or []
            }
        }

        if callback_url:
            payload["callBackUrl"] = callback_url

        try:
            response = requests.post(url, json=payload, headers=self.headers, timeout=30)
            response.raise_for_status()

            data = response.json()
            if data.get("code") != 200:
                raise Exception(f"API error: {data.get('msg', 'Unknown error')}")

            return data["data"]["taskId"]

        except requests.exceptions.HTTPError as e:
            self._handle_http_error(e)
            raise

    def check_status(self, task_id: str) -> Dict[str, Any]:
        """
        Check the status of a generation task.

        Args:
            task_id: The task ID to check

        Returns:
            Task status data
        """
        url = f"{self.base_url}/jobs/recordInfo"
        params = {"taskId": task_id}

        response = requests.get(url, params=params, headers=self.headers, timeout=30)
        response.raise_for_status()

        data = response.json()
        if data.get("code") != 200:
            raise Exception(f"API error: {data.get('msg', 'Unknown error')}")

        return data["data"]

    def wait_for_completion(
        self,
        task_id: str,
        poll_interval: float = 3.0,
        max_wait: float = 120.0,
        verbose: bool = True
    ) -> Dict[str, Any]:
        """
        Poll until task completes or times out.

        Args:
            task_id: The task ID to wait for
            poll_interval: Seconds between status checks
            max_wait: Maximum seconds to wait
            verbose: Print progress updates

        Returns:
            Final task result
        """
        start_time = time.time()

        while time.time() - start_time < max_wait:
            status_data = self.check_status(task_id)
            state = status_data.get("state")

            if state == "success":
                # Parse resultJson
                result_json = json.loads(status_data.get("resultJson", "{}"))
                return {
                    "success": True,
                    "urls": result_json.get("resultUrls", []),
                    "cost_time": status_data.get("costTime"),
                    "task_id": task_id
                }

            elif state == "fail":
                return {
                    "success": False,
                    "error": status_data.get("failMsg", "Unknown error"),
                    "error_code": status_data.get("failCode"),
                    "task_id": task_id
                }

            # Still waiting
            if verbose:
                elapsed = int(time.time() - start_time)
                print(f"  Waiting for generation... ({elapsed}s)", end="\r")

            time.sleep(poll_interval)

        return {
            "success": False,
            "error": "Timeout waiting for task completion",
            "task_id": task_id
        }

    def generate(
        self,
        prompt: str,
        aspect_ratio: str = "1:1",
        resolution: str = "2K",
        output_format: str = "png",
        image_input: Optional[List[str]] = None,
        verbose: bool = True
    ) -> Dict[str, Any]:
        """
        Generate an image and wait for completion.

        High-level method that combines create_task and wait_for_completion.

        Args:
            prompt: Text description of the image
            aspect_ratio: Output aspect ratio
            resolution: Output resolution
            output_format: Output format
            image_input: Optional source images for image-to-image
            verbose: Print progress

        Returns:
            Generation result with image URLs
        """
        if verbose:
            print(f"Creating generation task...")
            print(f"  Prompt: {prompt[:80]}...")

        # Get config values
        gen_config = self.config.get("generation", {})
        poll_interval = gen_config.get("poll_interval_seconds", 3)
        max_wait = gen_config.get("max_wait_seconds", 120)

        # Create task
        task_id = self.create_task(
            prompt=prompt,
            aspect_ratio=aspect_ratio,
            resolution=resolution,
            output_format=output_format,
            image_input=image_input
        )

        if verbose:
            print(f"  Task ID: {task_id}")

        # Wait for completion
        result = self.wait_for_completion(
            task_id=task_id,
            poll_interval=poll_interval,
            max_wait=max_wait,
            verbose=verbose
        )

        if verbose:
            if result["success"]:
                print(f"\n  Success! Generated {len(result['urls'])} image(s)")
                print(f"  Time: {result.get('cost_time', 'N/A')}ms")
            else:
                print(f"\n  Failed: {result.get('error')}")

        return result

    def download_image(self, url: str, output_path: str) -> bool:
        """
        Download a generated image to local file.

        Args:
            url: Image URL from generation result
            output_path: Local path to save image

        Returns:
            True if successful
        """
        try:
            response = requests.get(url, stream=True, timeout=60)
            response.raise_for_status()

            # Ensure directory exists
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)

            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            return True

        except Exception as e:
            print(f"Error downloading image: {e}")
            return False

    def _handle_http_error(self, error: requests.exceptions.HTTPError):
        """Handle HTTP errors with helpful messages"""
        status_code = error.response.status_code

        messages = {
            400: "Bad request - check your parameters",
            401: "Authentication failed - check your API key",
            402: "Insufficient credits - add credits to your account",
            429: "Rate limit exceeded - wait and retry",
            500: "Server error - retry later"
        }

        message = messages.get(status_code, f"HTTP error {status_code}")
        print(f"Error: {message}", file=sys.stderr)

        try:
            error_data = error.response.json()
            print(f"Details: {error_data}", file=sys.stderr)
        except:
            pass


def main():
    """CLI interface for Kie.ai generator"""
    parser = argparse.ArgumentParser(
        description="Generate images using Kie.ai Nano Banana Pro API"
    )

    parser.add_argument(
        "--prompt", "-p",
        required=True,
        help="Text description of the image to generate"
    )

    parser.add_argument(
        "--output", "-o",
        default="output.png",
        help="Output file path (default: output.png)"
    )

    parser.add_argument(
        "--aspect-ratio", "-a",
        default="1:1",
        choices=["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"],
        help="Aspect ratio (default: 1:1)"
    )

    parser.add_argument(
        "--resolution", "-r",
        default="2K",
        choices=["1K", "2K", "4K"],
        help="Resolution (default: 2K)"
    )

    parser.add_argument(
        "--format", "-f",
        default="png",
        choices=["png", "jpg"],
        help="Output format (default: png)"
    )

    parser.add_argument(
        "--image-input", "-i",
        nargs="*",
        help="Source image URLs for image-to-image editing"
    )

    parser.add_argument(
        "--api-key", "-k",
        help="Kie.ai API key (or set KIE_API_KEY env var)"
    )

    parser.add_argument(
        "--config", "-c",
        help="Path to config JSON file"
    )

    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Suppress progress output"
    )

    args = parser.parse_args()

    try:
        # Initialize generator
        generator = KieAIGenerator(
            api_key=args.api_key,
            config_path=args.config
        )

        # Generate image
        result = generator.generate(
            prompt=args.prompt,
            aspect_ratio=args.aspect_ratio,
            resolution=args.resolution,
            output_format=args.format,
            image_input=args.image_input,
            verbose=not args.quiet
        )

        if not result["success"]:
            print(f"Generation failed: {result.get('error')}", file=sys.stderr)
            sys.exit(1)

        # Download first image
        if result["urls"]:
            image_url = result["urls"][0]

            if not args.quiet:
                print(f"Downloading to {args.output}...")

            success = generator.download_image(image_url, args.output)

            if success:
                if not args.quiet:
                    print(f"Saved: {args.output}")
                # Print URL for use by other tools
                print(f"URL: {image_url}")
            else:
                print("Failed to download image", file=sys.stderr)
                sys.exit(1)
        else:
            print("No images in result", file=sys.stderr)
            sys.exit(1)

    except ValueError as e:
        print(f"Configuration error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
