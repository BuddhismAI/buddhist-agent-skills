# Buddhist Agent Skills

Open-source home for Buddhism-related AI skills and their compiled knowledge wikis.

- Chinese / 中文说明: [README.zh-CN.md](./README.zh-CN.md)

## Purpose

This repository holds reusable topic skills for Buddhist study, source-grounded reasoning, and knowledge-compounding workflows.

The goal is to keep Buddhist domain skills in one canonical home so multiple apps and agent runtimes can share:

- behavior and routing guidance
- compiled topic wikis
- correctness anchors
- collection-level knowledge artifacts

More importantly, this repo exists to help make authentic Buddhist teachings available to everyone through AI systems. The idea is that any developer should be able to integrate these skills into their own application and give users access to Buddhist teachings that are:

- authentic to the source tradition
- more accurate than generic model recall
- grounded in traceable texts and structured knowledge
- usable across many agent frameworks and product surfaces

We want Buddhist teaching to be available not only inside one app, but across many agents and applications in a way that remains careful, source-aware, and respectful of the tradition.

## Why A Separate Repository

This repository is intentionally separate from any single application.

That separation makes it easier to:

- reuse the same Buddhist skills across multiple apps
- evolve doctrinal knowledge independently from product code
- open-source the knowledge layer for broader adoption
- keep topic skills as durable shared infrastructure rather than app-local prompt files

## Skills + Source Lookup

This repository is designed to work alongside a public remote MCP tool for source lookup.

That MCP piece is still TBD and is not included in this repository yet.

The two pieces serve different roles:

- this repo provides the skill behavior, topic maps, correctness anchors, and compiled knowledge indexes
- the MCP tool, once available, will provide direct lookup into original source material and related corpus data

That combination matters. On their own, skills can give an agent a strong conceptual map, but pairing them with source lookup helps the agent stay grounded in original teachings and retrieve supporting evidence more reliably.

In other words:

- the skill helps the agent understand what it is looking at
- the MCP helps the agent find the underlying source material
- together they help agents answer Buddhist questions more completely and more faithfully

## Current Scope

Initial focus:

- `skills/madhyamaka/` - Madhyamaka skill and topic wiki

Planned future candidates:

- `skills/yogachara/`
- `skills/pramana/`
- `skills/lamrim/`
- `skills/buddhism/` - thin overview and routing skill across topics

## Repository Structure

Each topic skill is the canonical home for:

- `SKILL.md` - behavior, routing, and answering guidance
- `references/` - compiled wiki pages

These files often include indexes and structured reference material that become much more powerful when paired with source retrieval tooling.

Within a topic skill:

- `references/*.md` holds cross-collection synthesis
- `references/collections/*` holds per-collection wikis

## How These Skills Are Built

These skills are not meant to be loose prompt wrappers around generic model memory.

At a high level, the knowledge is built through a source-first synthesis process:

- start from real teaching materials such as lecture transcripts, commentaries, and related source texts
- process a collection sequentially rather than as isolated fragments, so later units can build on earlier ones
- discover and refine the collection's internal structure as the work progresses
- produce per-collection knowledge documents that explain argument flow, concepts, terminology, citations, and practice implications
- then synthesize across collections into topic-level reference documents that capture recurring methods, debates, classifications, and correctness anchors

The result is a layered knowledge base:

- source materials remain the ultimate authority
- collection-level docs preserve depth and provenance
- topic-level docs provide the conceptual map an agent can use at answer time

This is one of the main reasons the repository is useful for agents: it gives them a structured intellectual framework, not just raw retrieval results.

## Development Model

This repo is designed to be symlinked into consuming projects.

For example, a project may symlink:

- `.claude/skills/<skill>`
- `.agents/skills/<skill>`
- `backend/sandbox/.claude/skills/<skill>`

to the canonical directory in this repository.

Editing through the symlink updates the original files, because the symlink points at the same underlying path.

## Working Agreement

- Treat this repository as the source of truth for the extracted Buddhist skills.
- If a consuming project edits a symlinked skill, the corresponding changes belong to this repository.
- When a task changes skill content substantially, commit the changes here as part of the normal workflow.

## Feedback And Issues

If you spot a problem, a weak explanation, a broken reference, or a doctrinal issue, please open an issue.

Suggestions are also very welcome, whether they are about:

- factual corrections
- better structure or terminology
- missing source coverage
- clearer agent behavior
- ideas for new topic skills or source-lookup tooling

See [CLAUDE.md](./CLAUDE.md) for agent-specific instructions.
