# Mr. Rogers - AI Video Generation Agent System

> "Won't you be my neighbor?" - A friendly, methodical approach to AI video generation

Mr. Rogers is a multi-agent orchestration system for generating videos using the **Sora 2 Pro Text To Video API**. It's the video counterpart to the Bob Ross image generation system.

## Overview

Mr. Rogers coordinates a team of specialized sub-agents to transform video ideas into high-quality AI-generated videos:

```
User Request → Video Brief → Scene Composition → Generation → Review → Refinement (if needed)
```

## Agent Architecture

| Agent | File | Purpose |
|-------|------|---------|
| **Mr. Rogers** | `mr-rogers.md` | Main orchestrator - coordinates all sub-agents |
| **Video Brief Painter** | `agents/video-brief-painter.md` | Parses/creates structured video briefs |
| **Scene Composer** | `agents/scene-composer.md` | Crafts optimized Sora prompts (50-100 words) |
| **Video Painter** | `agents/video-painter.md` | Calls Sora API, handles async polling |
| **Video Critic** | `agents/video-critic.md` | Reviews videos against brief requirements |
| **Scene Refiner** | `agents/scene-refiner.md` | Improves prompts based on critic feedback |

## Quick Start

1. Ensure the API config exists at `.claude/agents/bob-ross/config/kie-config.json`
2. (Optional) Create a brand guide at `.brand/BRAND_GUIDE.md`
3. Request a video:

```
Create a cozy coffee shop video for Instagram Reels
```

Mr. Rogers will:
1. Check for your brand guide
2. Create a detailed video brief
3. Compose an optimized Sora prompt
4. Generate the video (1-3 minutes)
5. Review and refine if needed
6. Deliver the final video URL

## API Configuration

Mr. Rogers uses the same Kie.ai API configuration as Bob Ross:

```
.claude/agents/bob-ross/config/kie-config.json
```

The config includes:
- `api_key` - Kie.ai API key (works for both image and video)
- `models.video` - `sora-2-pro-text-to-video`
- `defaults.video` - Default video parameters

## Video Parameters

| Parameter | Options | Description |
|-----------|---------|-------------|
| `aspect_ratio` | `portrait`, `landscape` | Video orientation |
| `n_frames` | `10`, `15` | Duration (10s or 15s) |
| `size` | `standard`, `high` | Video quality |
| `remove_watermark` | `true`, `false` | Remove Sora watermark |

### Platform Mapping

| Platform | Aspect Ratio | Duration |
|----------|--------------|----------|
| TikTok | portrait (9:16) | 10-15s |
| Instagram Reels | portrait (9:16) | 10-15s |
| YouTube Shorts | portrait (9:16) | 10-15s |
| YouTube | landscape (16:9) | 10-15s |
| General/Website | landscape (16:9) | 10-15s |

## Prompt Best Practices

Mr. Rogers uses these Sora prompting principles:

1. **50-100 words** - Sweet spot for detail vs coherence
2. **One scene, one action** - No scene changes
3. **Simple camera work** - One movement type only
4. **Style anchors** - Film stock references, era references
5. **Specific details** - "worn wooden table" not "nice table"

### Example Prompt Structure
```
[Style anchor]. [Scene setting]. [Subject with details]. [Action]. [Camera movement]. [Lighting]. [Mood].
```

## Brand Integration

Create `.brand/BRAND_GUIDE.md` in your project root with:

```markdown
# Brand Guide

## Colors
- Primary: #HEX
- Secondary: #HEX

## Visual Style
[Description of brand aesthetic]

## Tone
[Brand personality and mood]
```

Mr. Rogers will incorporate these into video generation.

## Directory Structure

```
.claude/agents/mr-rogers/
├── mr-rogers.md              # Main orchestrator
├── README.md                 # This file
├── agents/
│   ├── video-brief-painter.md
│   ├── scene-composer.md
│   ├── video-painter.md
│   ├── video-critic.md
│   └── scene-refiner.md
├── config/                   # Uses bob-ross/config/kie-config.json
└── templates/                # Video brief templates (future)
```

## Workflow Details

### 1. Video Brief Painter
Transforms requests into structured briefs:
- Core concept
- Platform & aspect ratio
- Scene description
- Action beats (0-3s, 3-7s, 7-10s)
- Camera work
- Visual style & lighting
- Color palette & mood

### 2. Scene Composer
Converts briefs to Sora prompts:
- Selects style anchors (film stock, era)
- Writes scene foundation (15-25 words)
- Adds subject & action (10-20 words)
- Specifies camera (5-10 words)
- Sets lighting & mood (10-15 words)

### 3. Video Painter
Handles API interaction:
- Reads config for API key
- Creates task with Sora API
- Polls for completion (30s initial, 15s intervals)
- Returns video URL or error

### 4. Video Critic
Reviews against requirements:
- Scene accuracy (30%)
- Action/movement (25%)
- Camera work (20%)
- Visual style (15%)
- Technical quality (10%)

Verdict: `APPROVED` (≥3.5 avg) or `NEEDS_WORK` (<3.5 avg)

### 5. Scene Refiner
Improves prompts when needed:
- Targeted changes (not rewrites)
- Adds specificity
- Fixes technical issues
- Max 3 attempts total

## Comparison: Bob Ross vs Mr. Rogers

| Aspect | Bob Ross (Images) | Mr. Rogers (Video) |
|--------|-------------------|-------------------|
| API Model | nano-banana-pro | sora-2-pro-text-to-video |
| Generation Time | ~10-30 seconds | ~1-3 minutes |
| Output | Static images | 10-15 second videos |
| Aspect Ratios | 1:1, 4:5, 16:9, etc. | portrait, landscape |
| Prompt Length | Varies | 50-100 words optimal |
| Camera Work | N/A | Critical consideration |
| Action | Static scene | Continuous motion |

## Pricing (Estimated)

| Quality | 10 seconds | 15 seconds |
|---------|------------|------------|
| Standard | $1.00 | $1.50 |
| High | $2.00 | $3.00 |

*Prices in USD, subject to change*

## Tips for Best Results

1. **Keep it simple** - One location, one main subject
2. **Describe motion explicitly** - "steam rising" not just "hot coffee"
3. **Use style references** - "Kodak Portra" is better than "warm colors"
4. **Specify camera clearly** - "slow dolly out" not "camera moves back"
5. **Include atmosphere** - Lighting and mood matter
6. **Be patient** - Video generation takes time

## Troubleshooting

### Video not matching description
- Make the key element more explicit
- Add emphasis: "clearly visible", "prominently"
- Simplify competing elements

### Camera issues
- Use only ONE camera movement type
- Add speed modifier: "very slow", "gentle"
- Try static shot for complex scenes

### Style not right
- Add specific film stock reference
- Include era/aesthetic anchor
- Specify what to avoid: "not oversaturated"

### Technical artifacts
- Simplify the prompt
- Reduce number of elements
- Use more common/stable subjects

---

*"It's a beautiful day in this neighborhood, a beautiful day to make videos."*
