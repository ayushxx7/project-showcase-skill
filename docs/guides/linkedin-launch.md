# LinkedIn Launch Guide

Transform your project into LinkedIn engagement using the `linkedin-magic` sub-skill.

## Workflow

1. **Prep** — Run the main showcase skill first (capture + audit + README)
2. **Generate** — Pick a post variant (see below)
3. **Bundle** — Run `linkedin-magic/scripts/bundle_assets.py` to prepare images
4. **Post** — Use the generated content + assets

## Post Variants

### 🚀 The Viral Hype (Short & Punchy)
Focus: "The Magic Pill" angle. Emojis, badges, high-conversion hooks.
Best for: Projects with a clear, simple value proposition.

### 🏗️ The Deep Dive (Technical Architecture)
Focus: "How it works." Mermaid diagrams, tech stack logic.
Best for: Infrastructure, tools, frameworks.

### 📈 The Health Audit (Trust & Quality)
Focus: Repo Health score. Proves reliability.
Best for: Open-source libraries, production-ready tools.

### 💡 The Story (Problem/Solution)
Focus: Narrative. Why you built it and the struggle it solves.
Best for: Personal projects, startup tools.

## Templates

See `linkedin-magic/references/post_templates.md` for fill-in-the-blank templates for each variant.

## Asset Bundling

```bash
python3 linkedin-magic/scripts/bundle_assets.py
```

This scans `showcase/` and `assets/` for the best images and copies them to `linkedin_launch/` with descriptive names:
- `01_Landing_Page.png`
- `02_Dashboard_View.png`
- `03_System_Architecture.png`
- `04_CLI_Demo.gif`
- `05_Repo_Health.png`

## Hashtag Strategy

Core: `#BuildingInPublic #AIAgents #OpenSource`
Tech-specific: `#Python #React #AI #MachineLearning`
Skill-specific: `#ShowcaseSkill #VibeCoding`

## Pro Tips

- **First Comment Rule** — Post links in the first comment, not the main post (avoids algorithm penalty)
- **Lead with visuals** — LinkedIn is a visual platform. Images > text.
- **Human-first tone** — Avoid robotic "AI-generated" language.
