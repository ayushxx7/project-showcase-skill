---
name: linkedin-magic
description: "Automate viral LinkedIn posts for project showcasing. Invokes project-showcase to prepare the repo, then generates high-fidelity content, visual asset bundles, and engagement strategies for professional growth."
---

# LinkedIn Showcase Magic Skill 🚀✨

This skill is your personal PR agent. It transforms raw code into professional social currency by automating the "Documentation -> Hype" pipeline.

## Prerequisites
- **Project Showcase Skill**: This skill depends on `project-showcase` being installed.
- **GitHub CLI (`gh`)**: Required for metadata fetching and repository management.

## Core Workflows

### 1. The "Karma Farm" Prep
- **Goal**: Ensure the project is visually stunning and architecturally clear before posting.
- **Action**:
    - Invoke the `project-showcase` skill: *"Showcase this project for LinkedIn. Ensure the architecture diagram and health score are updated."*
    - Ensure `capture.py` has generated high-res screenshots in the `showcase/` folder.
    - Verify that the README has the professional badges and "Live App" links.

### 2. High-Impact Content Generation
- **Goal**: Create content that resonates with different LinkedIn audiences (Recruiters, Engineers, Founders).
- **Triggers**: "Showcase this on LinkedIn", "Karma farm this project", "Create a viral post for my work".
- **Post Variants**:
    - **🚀 The Viral Hype (Short & Punchy)**: Focuses on "The Magic Pill" aspect. Uses emojis, badges, and high-conversion hooks.
    - **🏗️ The Deep Dive (Technical Architecture)**: Focuses on the "how it works." Highlights the Mermaid diagrams and tech stack logic.
    - **📈 The Health Audit (Trust & Quality)**: Focuses on the Repo Health score. Proves reliability and professional standards.
    - **💡 The Story (Problem/Solution)**: Narrative-driven post about why you built it and the struggle it solves.

### 3. Visual Asset Bundling
- **Goal**: Package the "Showcase Gallery" for easy upload.
- **Action**:
    - Locate all PNG/GIF assets in the `showcase/` or `assets/` folder.
    - Create a local `linkedin_launch/` folder.
    - Copy the 3 best assets (Landing, Dashboard, Architecture) into this folder with descriptive names.
    - Provide the exact file paths to the user: *"Here are your 3 launch assets ready for LinkedIn upload: [path1], [path2], [path3]"*.

### 4. Hashtag & Engagement Strategy
- **Goal**: Maximize reach through surgical tagging.
- **Action**:
    - Identify the core tech stack (e.g., #Python, #React, #AI).
    - Inject trending "Vibe Coding" hashtags: #BuildingInPublic #AIAgents #GeminiCLI #ShowcaseSkill.
    - Provide a "Call to Action" (CTA) strategy (e.g., "Check the live app in the comments!").

## Bundled Resources
- **`references/post_templates.md`**: Proven LinkedIn high-performance structures.
- **`scripts/bundle_assets.py`**: A utility to surgically select and rename the best showcase assets for social media.

## Mandatory Execution Checklist
Before handing the "Launch Kit" to the user, the agent MUST:

- [ ] **Prep**: Was `project-showcase` run? (README updated, health score present?)
- [ ] **Visuals**: Are there at least 2 high-res screenshots or 1 GIF?
- [ ] **Architecture**: Is the Mermaid diagram included in the "Deep Dive" post?
- [ ] **Variants**: Have 3 distinct post styles been generated?
- [ ] **Links**: Are the Repo URL and Live App URL verified?
- [ ] **Bundle**: Is the `linkedin_launch/` folder ready with renamed assets?

## Best Practices
- **Human-First Tone**: Avoid overly robotic "AI-generated" language. Use surgical, high-vibe terminology (e.g., "Surgical updates", "Magic pill", "Vibe coding").
- **Visual Evidence**: Always lead with the images. LinkedIn is a visual platform.
- **The "First Comment" Rule**: Remind the user to post the links in the first comment to avoid LinkedIn's algorithm penalizing external links in the main post.

---
*Built with ❤️ for Karma Farmers and Vibe Coders.*
