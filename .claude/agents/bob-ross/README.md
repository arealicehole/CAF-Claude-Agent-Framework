# Bob Ross - Multi-Agent Visual Creation System

*"We don't make mistakes, just happy little accidents."*

**Version:** 1.2.0 | **Status:** Production Ready
**API:** Kie.ai Nano Banana Pro (Google Gemini)
**Part of:** [CAF - Claude Agent Framework](https://github.com/arealicehole/CAF-Claude-Agent-Framework)

---

## Overview

Bob Ross is a multi-agent visual creation system that transforms design briefs into beautiful images. Like the legendary painter, it approaches each creation with patience, vision, and the belief that every image deserves love.

### Key Features

- **Design Brief Driven** - Parse existing briefs or create new ones
- **Multi-Agent Workflow** - Specialized agents for each task
- **Quality Control** - Automatic review against design specs
- **Smart Iteration** - Edit API or re-prompt based on feedback
- **Kie.ai Integration** - Uses Nano Banana Pro for generation

---

## Quick Start

### 1. Setup API Key

Get your Kie.ai API key from: https://kie.ai/api-key

Then set it in `config/kie-config.json`:

```json
{
  "kie_ai": {
    "api_key": "YOUR_KIE_API_KEY_HERE"
  }
}
```

Or set environment variable:
```bash
export KIE_API_KEY="your_api_key_here"
```

### 2. Use the Agent

**From Claude Code:**

```
Use the bob-ross agent to create images from this design brief:

Project: Product Launch
Platform: Instagram
Style: Premium, minimal, modern
Images needed:
1. Hero shot - product on marble, text "DESIGNED DIFFERENT"
2. Feature highlight - close-up of product details
3. Lifestyle - product in use context

Save to: ./output/product-launch/
```

**Or ask Bob Ross to create a brief:**

```
Use the bob-ross agent to create 3 Instagram posts for a coffee shop.
Autumn vibes, cozy atmosphere, feature lattes.
```

---

## Brand Guide Setup

Bob Ross looks for brand specs to ensure consistent styling.

**Location:** `.brand/BRAND_GUIDE.md` (in your project root)

**Template:** `templates/BRAND_GUIDE_TEMPLATE.md`

**Minimum needed:**
- Primary Color: #XXXXXX
- Secondary Color: #XXXXXX
- Style Keywords: modern, minimal, etc.
- Watermark: @handle (optional)

**No brand guide?** Provide specs in your request or use defaults.

---

## Architecture

```
                    ┌─────────────────────────────────┐
                    │         BOB ROSS                │
                    │   The Happy Little Orchestrator │
                    │   (Maintains Design Brief Vision)│
                    └───────────────┬─────────────────┘
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        │                           │                           │
        ▼                           ▼                           ▼
┌───────────────┐         ┌─────────────────┐         ┌─────────────────┐
│ Design Brief  │         │  Happy Prompt   │         │  Canvas Painter │
│    Painter    │◄───────►│    Crafter      │────────►│  (Kie.ai API)   │
│(Parse/Create) │         │ (Build Prompts) │         │ (Generate Art)  │
└───────────────┘         └─────────────────┘         └────────┬────────┘
                                    ▲                          │
                                    │                          ▼
                          ┌─────────┴────────┐         ┌───────────────┐
                          │  Brush Refiner   │◄────────│   Art Critic  │
                          │ (Improve Prompts)│         │(Review vs Brief)│
                          └──────────────────┘         └───────┬───────┘
                                    ▲                          │
                                    │                          ▼
                                    │                 ┌─────────────────┐
                                    └─────────────────│ Happy Decision  │
                                                      │(Edit or Reprompt)│
                                                      └─────────────────┘
```

---

## Agent Roles

| Agent | Model | Purpose |
|-------|-------|---------|
| **bob-ross** | Sonnet | Orchestrates workflow, maintains vision |
| **design-brief-painter** | Haiku | Parses/creates design briefs |
| **happy-prompt-crafter** | Haiku | Crafts Nano Banana optimized prompts |
| **canvas-painter** | Haiku | Calls Kie.ai API, handles async polling |
| **art-critic** | Sonnet | Reviews images against brief |
| **happy-little-decision** | Haiku | Decides: edit API or re-prompt |
| **brush-refiner** | Haiku | Improves prompts based on feedback |

---

## Workflow

### The Joy of Painting

1. **Prepare Canvas** - Design brief is parsed/created
2. **Mix Colors** - Prompt is crafted for each image
3. **Paint Canvas** - Kie.ai generates the image
4. **Step Back** - Art Critic reviews against brief
5. **Happy Decisions** - If not approved, decide how to fix
6. **Sign Masterpiece** - Save approved images

### Iteration Strategy

- **Attempt 1:** Original prompt, strict review (80+ to pass)
- **Attempt 2:** Refined prompt, moderate review (75+ to pass)
- **Attempt 3:** Further refined, lenient review (70+ to pass)
- **After 3:** Accept best result if score > 60

---

## Configuration

### kie-config.json

```json
{
  "kie_ai": {
    "api_key": "YOUR_KEY",
    "base_url": "https://api.kie.ai/api/v1",
    "model": "nano-banana-pro"
  },
  "defaults": {
    "aspect_ratio": "1:1",
    "resolution": "2K",
    "output_format": "png"
  },
  "generation": {
    "max_attempts": 3,
    "poll_interval_seconds": 3,
    "max_wait_seconds": 120
  },
  "review": {
    "approval_threshold": {
      "attempt_1": 80,
      "attempt_2": 75,
      "attempt_3": 70
    }
  }
}
```

---

## Usage Examples

### Example 1: Generate from Brief

```
Use the bob-ross agent to create images from /briefs/product-launch.md
Save to /output/product-launch/
```

### Example 2: Create Brief + Generate

```
Use the bob-ross agent to create:
- 5 Instagram carousel slides for a cannabis dispensary event
- Festive winter theme, green and red colors
- Text: "KANNA KICKBACK 6" on slide 1
- Style: Fun, illustrated, cannabis culture meets holidays
```

### Example 3: Single Image

```
Use the bob-ross agent to create a hero image:
- Premium smartphone on marble surface
- Soft studio lighting
- Text "DESIGNED DIFFERENT" at bottom
- 16:9 for website header
- Save to ./hero.png
```

### Example 4: Image Series with Consistency

```
Use the bob-ross agent to create a 3-part Instagram story:
- Character: Cute illustrated coffee cup mascot
- Maintain character consistency across all frames
- Frame 1: Character waking up
- Frame 2: Character getting filled with coffee
- Frame 3: Character happy and energized
```

---

## Design Brief Format

Design briefs can be structured JSON or natural language. The Design Brief Painter converts any input to this structure:

```json
{
  "project_name": "Product Launch",
  "platform": "instagram",
  "image_count": 3,
  "images": [
    {
      "image_id": "slide_01",
      "title": "Hero Image",
      "description": "Product on marble with bold text",
      "visual_style": {
        "mood": "premium, minimal",
        "lighting": "soft studio",
        "color_palette": ["#1a1a1a", "#ffffff"]
      },
      "text_overlays": [
        { "text": "DESIGNED DIFFERENT", "position": "bottom center" }
      ],
      "technical": {
        "aspect_ratio": "1:1",
        "resolution": "2K"
      },
      "success_criteria": [
        "Product clearly visible",
        "Text readable"
      ]
    }
  ]
}
```

---

## API Pricing

| Resolution | Cost per Image |
|------------|----------------|
| 1K - 2K | $0.12 |
| 4K | $0.24 |

Rate limit: 1,000 RPM (requests per minute)

---

## File Structure

```
.claude/agents/bob-ross/
├── bob-ross.md              # Main orchestrator agent
├── README.md                # This file
├── agents/
│   ├── design-brief-painter.md
│   ├── happy-prompt-crafter.md
│   ├── canvas-painter.md
│   ├── art-critic.md
│   ├── happy-little-decision.md
│   └── brush-refiner.md
├── config/
│   └── kie-config.json      # API and settings
└── utils/
    └── kie_generator.py     # Python API client
```

---

## CLI Utility

Generate images directly from command line:

```bash
# Basic generation
python utils/kie_generator.py \
  --prompt "A serene mountain landscape at sunset" \
  --output ./mountain.png

# With options
python utils/kie_generator.py \
  --prompt "Premium product shot" \
  --aspect-ratio "16:9" \
  --resolution "4K" \
  --output ./product.png

# Image-to-image editing
python utils/kie_generator.py \
  --prompt "Make the colors more vibrant" \
  --image-input "https://example.com/source.png" \
  --output ./edited.png
```

---

## Troubleshooting

### "Authentication failed"
- Check API key in config or environment variable
- Verify key at https://kie.ai/api-key

### "Rate limit exceeded"
- Wait 60 seconds and retry
- Consider batching requests

### "Images don't match brief"
- Brief may need more specific details
- Add explicit color hex codes
- Include style references
- Be specific about text positioning

### "Text spelling errors"
- Nano Banana is good but not perfect at text
- Try spelling out letter-by-letter in prompt
- Use simpler, shorter text

---

## Best Practices

1. **Be Specific** - The more detail in the brief, the better results
2. **Use Color Hex Codes** - "#FF6B35" instead of "orange"
3. **Include Style References** - "Apple product photography" helps
4. **Prioritize Elements** - Put most important things first
5. **Review Carefully** - Check first image before generating series
6. **Iterate Wisely** - Sometimes starting fresh beats endless refinement

---

## Philosophy

*"There's nothing wrong with having a tree as a friend."*

Bob Ross approaches every image with:
- **Patience** - Quality takes time
- **Vision** - The brief is the north star
- **Acceptance** - Happy accidents can become features
- **Persistence** - Keep painting until it's right

---

## Global Installation

To use Bob Ross across all your projects, copy to your user-level Claude agents:

```bash
cp -r .claude/agents/bob-ross ~/.claude/agents/
```

---

## Credits

**Created:** 2025-11-26
**Powered by:** Kie.ai Nano Banana Pro API
**Inspired by:** Bob Ross and the Joy of Painting

---

*"Happy painting, and God bless."* 🎨
