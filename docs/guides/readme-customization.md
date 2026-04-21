# README Customization ✍️

The Project Showcase Skill is designed to be "surgical"—it knows how to inject content without destroying your hard-earned manual documentation.

## The Injection Points

By default, the skill looks for or creates the following sections:
1. **Elevator Pitch**: A concise summary at the top.
2. **Visual Gallery**: The screenshots and GIFs immediately following the pitch.
3. **Installation & Features**: Core functional sections.

## How it Identifies Your Content

The skill uses advanced pattern matching to detect existing headers.
- **Never Duplicates**: If you already have an "Installation" section, it won't add a second one.
- **Superiority Choice**: If the generated content is better (clearer, more visual), it might propose a replacement.
- **Hybrid Merge**: It can merge generated features with your manual ones.

## Customizing the Vibe

You can influence the final README by providing hints to the agent:
- *"Add a dark-mode-first gallery."*
- *"Keep my manual 'How it Works' section untouched."*
- *"Ensure the health score is moved to a separate REPO_HEALTH.md file."*
