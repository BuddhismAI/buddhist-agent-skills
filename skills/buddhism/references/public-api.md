# Public API for Buddhist Text Search

When MCP tooling is unavailable, agents can call these REST endpoints directly to search and fetch Buddhist teaching texts. No authentication required.

**Base URL:** `https://api.shuiyue.ai/api/v1`

Use this API as a grounding fallback. Skill references help route the question, but local corpus fetches provide citable source evidence. Some Buddhist Assistant runtimes also expose fashi or skill-reference search; public agents should treat those as optional.

## Search

`POST /api/v1/search`

```json
{
  "query": "菩提心",
  "limit": 5,
  "sources": ["local"],
  "chunk_types": ["summary", "qa", "lesson"]
}
```

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `query` | string | yes | — | Search query, 1-500 chars |
| `limit` | int | no | 5 | Max results, 1-10 |
| `sources` | string[] | no | local corpus | Prefer `["local"]` for public grounding. In-app/authenticated runtimes may also support `["fashi"]` or `["skill_refs"]`; do not assume they are available from the public endpoint |
| `chunk_types` | string[] | no | all | Filter local results: summary, qa, lesson, misconception, koan, key_term, verse |

Response includes `fetch_ref` on each result — use it to fetch the full text:

```json
{
  "results": [
    {
      "source": "local",
      "title": "入菩萨行论 第1课",
      "snippet": "菩提心的功德...",
      "metadata": {"teacher": "索达吉堪布", "collection": "入菩萨行论"},
      "fetch_ref": {"source": "local", "source_id": "课程/入菩萨行论/第1课.html"}
    }
  ]
}
```

If a public deployment returns `source_path` / `sourcePath` instead of `fetch_ref`, treat that value as the local corpus path for `/api/v1/corpus/{path}`.

## Quick Source Check

Use this when you need reliable local source grounding and MCP tools are missing:

```bash
curl -sS -X POST "https://api.shuiyue.ai/api/v1/search" \
  -H "Content-Type: application/json" \
  -d '{"query":"菩提心 次第","limit":5,"sources":["local"],"chunk_types":["qa","lesson","summary"]}'
```

Then fetch the strongest local result. Prefer `fetch_ref.source_id`; if absent, use the result's `source_path` / `sourcePath`.

```bash
curl -sS "https://api.shuiyue.ai/api/v1/corpus/课程/入菩萨行论/第1课.html?mode=excerpts&match_text=菩提心&context_chars=600&max_matches=3"
```

For full-text review of a short document:

```bash
curl -sS "https://api.shuiyue.ai/api/v1/corpus/课程/入菩萨行论/第1课.html?mode=full"
```

### Searching skill references

If the runtime supports it, use `sources: ["skill_refs"]` to search the skill's own reference wiki. This is a routing mechanism — it finds the right file and section, then you read the full file for context. If unsupported, use the installed files under `references/` directly.

```json
{
  "query": "离一多因如何破微尘",
  "sources": ["skill_refs"],
  "limit": 5
}
```

Response includes `metadata.file` (path relative to `references/`) and `metadata.section` (H2 heading):

```json
{
  "results": [
    {
      "source": "skill_refs",
      "title": "离一多因 — 在破微尘之实一上的应用",
      "snippet": "离一多因在第50课中具体用于分析微尘...",
      "metadata": {
        "skill": "buddhism",
        "file": "collections/中观庄严论/推理方法/离一多因.md",
        "section": "在破微尘之实一上的应用（第50-55课）",
        "collection": "中观庄严论",
        "topics": "离一多因, 破实一"
      },
      "fetch_ref": {
        "source": "skill_refs",
        "source_id": "buddhism/collections/中观庄严论/推理方法/离一多因.md"
      }
    }
  ]
}
```

## Fetch Skill Reference

`GET /api/v1/document/skill_refs/{source_id}`

Fetches full content of a skill reference file. Use `fetch_ref.source_id` from `skill_refs` search results.

Example:
```
GET /api/v1/document/skill_refs/buddhism/collections/中观庄严论/推理方法/离一多因.md
```

If this endpoint is unavailable in the public deployment, read the installed file under `references/` instead. Do not cite skill references as final evidence.

## Fetch Local Corpus Text

`GET /api/v1/corpus/{source_path}`

| Param | In | Required | Description |
|-------|----|----------|-------------|
| `source_path` | path | yes | `fetch_ref.source_id` from search results |
| `mode` | query | no | `full`, `excerpts`, or `range` (default: `full`) |
| `match_text` | query | for excerpts unless `match_terms` is set | Return focused windows around matched text |
| `match_terms` | query | for excerpts unless `match_text` is set | Comma-separated terms for focused windows |
| `context_chars` | query | no | Characters around each match |
| `max_matches` | query | no | Max matched windows, 1-20 (default: 3) |

Example — fetch full text:
```
GET /api/v1/corpus/课程/入菩萨行论/第1课.html?mode=full
```

Example — fetch matching excerpts:
```
GET /api/v1/corpus/课程/入菩萨行论/第1课.html?mode=excerpts&match_text=菩提心&context_chars=600
```

`source_docs` paths such as `development/data/markdown/...` are provenance labels from preprocessing. They may not exist in an installed public skill repo. Use API search/fetch paths instead of trying to open those paths directly.

## Fetch Fashi.ai Text

`GET /api/v1/fashi/{segment_id}`

Use this only when search results or another runtime already gave you a fashi `segment_id`. Public local search may not return fashi hits.

| Param | In | Required | Description |
|-------|----|----------|-------------|
| `segment_id` | path | yes | `fetch_ref.source_id` from search results (integer) |

Example:
```
GET /api/v1/fashi/12345
```

## Typical Workflow

1. **Find the right reference doc**: use installed files under `references/`, or optional `sources: ["skill_refs"]` if the runtime supports it.
2. **Read the reference file** locally (if the skill is installed) or fetch via `GET /api/v1/document/skill_refs/{source_id}` when that endpoint is available.
3. **Search for citations**: `POST /api/v1/search` with `sources: ["local"]` for citable evidence. In-app runtimes may also support `["local", "fashi"]`.
4. **Fetch full source text**: use the appropriate fetch endpoint based on `fetch_ref.source`
   - `source: "local"` or `"corpus"` → `GET /api/v1/corpus/{source_id}`
   - `source: "fashi"` → `GET /api/v1/fashi/{source_id}`
   - `source: "skill_refs"` → `GET /api/v1/document/skill_refs/{source_id}`
5. Use `mode=excerpts` with `match_text` or `match_terms` on local fetches to get focused context windows instead of entire documents
