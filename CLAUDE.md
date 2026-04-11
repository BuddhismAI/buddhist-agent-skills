# Repository Instructions

This file provides guidance to AI coding agents working with this repository.

## Purpose

`buddhist-agent-skills` is a repository for reusable Buddhism-related agent skills and their compiled topic wikis.

The initial topic is `madhyamaka`, but the repository is intended to grow into a broader hub of Buddhist topic skills.

## Structure

- `skills/buddhism/SKILL.md` - unified behavior and routing instructions
- `skills/buddhism/references/topics/<topic>/` - per-topic behavior docs, concept maps, correctness anchors
- `skills/buddhism/references/collections/` - per-collection wiki docs
- `skills/buddhism/references/maps/` - topic and collection indexes

## Language Convention

- Use English for behavior guidance, routing rules, and agent-facing instructions.
- Use Chinese for Buddhism-related knowledge content, doctrinal explanations, collection notes, and reference materials.
- When in doubt, Buddhist content should default to Chinese.

## Maintenance Expectations

- Keep docs clear, concise, and welcoming to outside contributors.
- Prefer generic, reusable language over app-specific assumptions.
- When modifying files in this repository, keep commits scoped and descriptive.
- Maintain the unified Buddhism skill with per-topic depth through topic index docs (`references/topics/<topic>/index.md`). Add new topics as collections are processed, not speculatively.

## Development Workflow

- This repo is a **public skill repo** — keep it clean of development artifacts (specs, design docs, scripts, logs).
- All development work (specs, design docs, ingestion pipelines, evaluation data, architecture notes) belongs in the `development/` submodule.
- Only publish finished skills and their references to the top-level `skills/` directory.
- The `development/` directory is a **separate git repo** (submodule). Changes to files in `development/` must be committed and PR'd in the submodule repo (`BuddhismAI/buddhist-agent-skills-dev`), not the parent. After merging in the submodule, update the submodule pointer in the parent with `git add development && git commit`.

## Open Source Defaults

- Add lightweight documentation when introducing new top-level structure.
