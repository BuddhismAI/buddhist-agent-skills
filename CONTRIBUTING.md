# Contributing

Thanks for contributing to `buddhist-agent-skills`.

## Principles

- Keep each skill focused on a doctrinal or practice topic.
- Prefer topic skills with multiple collections over one monolithic Buddhism skill.
- Keep cross-collection synthesis in `references/*.md`.
- Keep per-collection analysis in `references/collections/*`.
- Keep installable skill metadata in `agents/openai.yaml` aligned with `SKILL.md` when present.
- Preserve provenance so claims can be traced back to source texts or collection docs.
- Use English for behavior guidance and repository-facing instructions.
- Use Chinese for Buddhism-related content and reference materials.

## When editing from another repo

Some consuming projects use symlinks to point into this repository.

If you edit a skill through a symlinked path, you are still editing the real files in this repository. Please make the content commit here.

## Suggested workflow

1. Update the topic skill content.
2. If the skill is user-installable, update `agents/openai.yaml` when the skill name, framing, or default prompt changes.
3. Verify links and structure still make sense.
4. Commit here with a message that describes the knowledge or skill change.

## Scope

This repository is for reusable Buddhist agent skills and their knowledge artifacts.

Application-specific code, UI behavior, and app wiring should stay in the consuming project repository unless they are truly generic.
