# Repository Instructions

This file provides guidance to AI coding agents working with this repository.

## Purpose

`buddhist-agent-skills` is a repository for reusable Buddhism-related agent skills and their compiled topic wikis.

The initial topic is `madhyamaka`, but the repository is intended to grow into a broader hub of Buddhist topic skills.

## Structure

- `skills/<topic>/SKILL.md` - behavior and routing instructions
- `skills/<topic>/references/` - compiled knowledge wiki

Inside a topic skill:

- `references/*.md` is the cross-collection layer
- `references/collections/*` is the per-collection wiki layer

## Language Convention

- Use English for behavior guidance, routing rules, and agent-facing instructions.
- Use Chinese for Buddhism-related knowledge content, doctrinal explanations, collection notes, and reference materials.
- When in doubt, Buddhist content should default to Chinese.

## Maintenance Expectations

- Keep docs clear, concise, and welcoming to outside contributors.
- Prefer generic, reusable language over app-specific assumptions.
- When modifying files in this repository, keep commits scoped and descriptive.
- Preserve the topic-skill architecture rather than collapsing everything into one monolithic Buddhism skill.

## Open Source Defaults

- Add lightweight documentation when introducing new top-level structure.
