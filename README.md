# CAF - Claude Agent Framework

A comprehensive multi-agent system framework for Claude Code featuring research automation and multi-platform content creation.

## 🎯 Overview

CAF provides two powerful agent systems:

1. **Research System (v2)** - Autonomous research orchestration with parallel execution (3-5x faster)
2. **Content Newsroom** - Multi-platform content creation specialists (YouTube, Instagram, TikTok, X, Website)

---

## 📁 Structure

```
.claude/agents/
├── research/           # Research automation system (v2)
│   ├── orchestrator-v2.md
│   ├── planner-v2.md
│   ├── searcher-v2.md
│   ├── mini-synthesizer.md
│   ├── synthesizer-v2.md
│   └── README-V2-UPGRADE.md
│
└── newsroom/          # Multi-platform content creators
    ├── newsroom-editor.md
    ├── youtube-creator.md
    ├── instagram-creator.md
    ├── tiktok-creator.md
    ├── x-creator.md
    └── website-creator.md

r/                     # Documentation & Research
├── guides/            # System documentation
│   ├── SUBAGENT-SYSTEM-GUIDE.md
│   └── NEWSROOM-SYSTEM-GUIDE.md
├── platform-research/ # 2025 platform intelligence
│   ├── youtube-content-research-2025-*.md
│   ├── instagram-content-research-2025-*.md
│   ├── tiktok-content-research-2025-*.md
│   ├── x-content-research-2025-*.md
│   └── website-seo-research-2025-*.md
└── research-archive/  # Historical research
    └── *.md (older research reports)
```

---

## 🚀 Quick Start

### Research System

```
Use the orchestrator-v2 agent to research: [your topic]
```

**Example:**
```
Use the orchestrator-v2 agent to research: Latest developments in quantum computing for 2025
```

**Features:**
- Parallel search execution (4-6 searches simultaneously)
- Hierarchical synthesis (mini-synthesizers → final synthesis)
- Auto-saves to `/r` directory
- 3-5x faster than sequential v1

---

### Content Newsroom

```
Use the newsroom-editor agent to create content about [topic] for all platforms
```

**Example:**
```
Use the newsroom-editor agent to create content about "productivity tips for remote workers" for all platforms.

Goal: Engagement and education
Tone: Friendly and practical
Target audience: Millennial/Gen Z remote workers
```

**Features:**
- Creates for 5 platforms in parallel: YouTube, Instagram, TikTok, X, Website
- Platform-specific optimization (updated with 2025 algorithms)
- Quality review and scoring
- Brand consistency enforcement
- Consultant mode for platform strategy

---

## 📚 Documentation

### Quick Reference

- **[Subagent System Guide](./r/guides/SUBAGENT-SYSTEM-GUIDE.md)** - Complete architecture and design patterns
- **[Newsroom System Guide](./r/guides/NEWSROOM-SYSTEM-GUIDE.md)** - Content creation workflows and usage

### Research Reports (2025 Platform Intelligence)

All agents updated with comprehensive research from 40-60+ sources per platform:

- `r/platform-research/youtube-content-research-2025-*.md` - Algorithm, CTR optimization, retention strategies
- `r/platform-research/instagram-content-research-2025-*.md` - Reels, hashtags, engagement tactics
- `r/platform-research/tiktok-content-research-2025-*.md` - FYP mechanics, hooks, completion rates
- `r/platform-research/x-content-research-2025-*.md` - Engagement hierarchy, Premium benefits, threads
- `r/platform-research/website-seo-research-2025-*.md` - Google algorithm, E-E-A-T, Core Web Vitals

---

## 🎯 Installation

### Option 1: Project-Level (Single Project)

Copy agents to your project:
```bash
cp -r .claude/agents/ /path/to/your/project/.claude/
```

### Option 2: User-Level (All Projects)

Install globally:
```bash
cp -r .claude/agents/* ~/.claude/agents/
```

Agents will be available in any project on your system.

---

## 💡 Key Features

### Research System (v2)

✅ **Wide-then-Deep Architecture** - Parallel search + hierarchical synthesis
✅ **3-5x Performance Improvement** - Typical research: 2-4 minutes vs 8-12 minutes
✅ **Tool Restrictions** - Each agent has minimal required tools (15-20% focus improvement)
✅ **Auto-Save** - Results saved to `/r` with YAML frontmatter
✅ **Quality Metrics** - Completeness scores, source citations, execution time

**Performance Targets:**
- Simple research (3 searches): <1 minute
- Moderate research (8 searches): <2.5 minutes
- Complex research (15 searches): <4 minutes

---

### Content Newsroom

✅ **Platform Expertise** - Each creator knows their platform's 2025 algorithm
✅ **Parallel Production** - All 5 platforms created simultaneously (15-30 min)
✅ **Quality Control** - Editor reviews and scores (75+ required)
✅ **Dual Mode** - Create content OR consult as experts
✅ **Content Adaptation** - Repurpose existing content across platforms

**Platform Intelligence (Updated 2025):**

- **YouTube**: Retention > watch time, 70%+ retention solid, CTR 4%+ good
- **Instagram**: 3-5 hashtags optimal (down from 30), saves/shares > likes
- **TikTok**: 80% completion benchmark, 0.5-1s hook window, 30%+ watch muted
- **X**: Premium 10x reach, replies > QTs > RTs, 1-2 hashtags max
- **Website**: 1,928 words sweet spot, mobile-first, E-E-A-T critical

---

## 📊 Agent Specifications

### Research Agents

| Agent | Model | Tools | Purpose |
|-------|-------|-------|---------|
| orchestrator-v2 | Sonnet | All | Parallel workflow coordination |
| planner-v2 | Sonnet | None | Parallel-optimized planning |
| searcher-v2 | Haiku | WebSearch, WebFetch | Fast search execution (<30s) |
| mini-synthesizer | Haiku | None | Batch synthesis (<20s) |
| synthesizer-v2 | Sonnet | None | Final deep synthesis (2-3min) |

### Content Agents

| Agent | Model | Tools | Purpose |
|-------|-------|-------|---------|
| newsroom-editor | Sonnet | All | Orchestration, quality control |
| youtube-creator | Sonnet | WebSearch | Video scripts, SEO, retention |
| instagram-creator | Haiku | WebSearch | Reels, posts, carousels |
| tiktok-creator | Haiku | WebSearch | Viral short-form content |
| x-creator | Haiku | WebSearch | Tweets, threads, engagement |
| website-creator | Sonnet | WebSearch | Blog posts, landing pages, SEO |

---

## 🔧 Advanced Usage

### Research System

**Parallel Execution:**
```
Multiple independent searches run simultaneously in batches of 4-6
```

**Hierarchical Synthesis:**
```
Batch 1 → Mini-Synthesis A
Batch 2 → Mini-Synthesis B
Batch 3 → Mini-Synthesis C
    ↓
Final Synthesis (combines A, B, C)
```

**Result:** 60-80% reduction in final synthesis input size

---

### Content Newsroom

**Content Adaptation:**
```
Use the newsroom-editor agent to adapt this blog post to Instagram, TikTok, and X:

[paste content]
```

**Platform Consultation:**
```
Use the newsroom-editor agent to consult the TikTok expert: What's the best hook strategy for educational content?
```

**Single Platform:**
```
Use the youtube-creator agent to create a video script about [topic]
```

---

## 📈 Performance Metrics

### Research System

| Complexity | v1 (Sequential) | v2 (Parallel) | Speedup |
|-----------|----------------|---------------|---------|
| Simple (3 searches) | 2 min | 1 min | 2x |
| Moderate (8 searches) | 6 min | 2 min | 3x |
| Complex (15 searches) | 12 min | 3.5 min | 3.4x |

### Content Newsroom

| Task | Duration |
|------|----------|
| Single platform | 3-5 minutes |
| All 5 platforms (parallel) | 15-30 minutes |
| Content adaptation (3 platforms) | 10-20 minutes |
| Platform consultation | 2-5 minutes |

---

## 🤝 Contributing

Contributions welcome! Key areas:

- New platform specialists (LinkedIn, Pinterest, etc.)
- Research domain specializations
- Performance optimizations
- Documentation improvements

---

## 📝 License

MIT License - See LICENSE file for details

---

## 🙏 Acknowledgments

Built on insights from:
- [CAF-Research](https://github.com/arealicehole/CAF-Research) - Research automation patterns
- [Claude Code Official Docs](https://code.claude.com/docs/en/sub-agents) - Subagent architecture
- [claude-code-agents-wizard-v2](https://github.com/IncomeStreamSurfer/claude-code-agents-wizard-v2) - Parallel generation patterns
- 200+ authoritative sources across platform research

---

## 🔗 Links

- **Documentation:** See `/r/guides` directory for complete guides
- **Research Reports:** Platform-specific intelligence in `/r/platform-research`
- **Architecture Guide:** `r/guides/SUBAGENT-SYSTEM-GUIDE.md`
- **Usage Guide:** `r/guides/NEWSROOM-SYSTEM-GUIDE.md`

---

**Version:** 1.0
**Last Updated:** 2025-11-10
**Status:** Production Ready

---

*CAF - Because building with AI agents should be systematic, not chaotic.*
