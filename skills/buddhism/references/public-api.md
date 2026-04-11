# Public API for Buddhist Text Search

When MCP tooling is unavailable, agents can call these REST endpoints directly to search and fetch Buddhist teaching texts. No authentication required.

**Base URL:** `https://api.shuiyue.ai/api/v1`

## Search

`POST /api/v1/search`

```json
{
  "query": "菩提心",
  "limit": 5,
  "sources": ["local", "fashi"],
  "chunk_types": ["summary", "qa", "lesson"]
}
```

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `query` | string | yes | — | Search query, 1-500 chars |
| `limit` | int | no | 5 | Max results, 1-10 |
| `sources` | string[] | no | all | `["local"]`, `["fashi"]`, `["skill_refs"]`, or any combination |
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

### Searching skill references

Use `sources: ["skill_refs"]` to search the skill's own reference wiki. This is a routing mechanism — it finds the right file and section, then you read the full file for context.

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

## Fetch Local Text

`GET /api/v1/local/{source_path}`

| Param | In | Required | Description |
|-------|----|----------|-------------|
| `source_path` | path | yes | `fetch_ref.source_id` from search results |
| `match_text` | query | no | Return only context windows around matched lines |
| `context_lines` | query | no | Lines around each match, 0-50 (default: 3) |
| `max_matches` | query | no | Max matched windows, 1-20 (default: 3) |

Example — fetch full text:
```
GET /api/v1/local/课程/入菩萨行论/第1课.html
```

Example — fetch with text matching (returns only relevant windows):
```
GET /api/v1/local/课程/入菩萨行论/第1课.html?match_text=菩提心&context_lines=5
```

## Fetch Fashi.ai Text

`GET /api/v1/fashi/{segment_id}`

| Param | In | Required | Description |
|-------|----|----------|-------------|
| `segment_id` | path | yes | `fetch_ref.source_id` from search results (integer) |

Example:
```
GET /api/v1/fashi/12345
```

## Typical Workflow

1. **Find the right reference doc**: `POST /api/v1/search` with `sources: ["skill_refs"]` and your question in natural language
2. **Read the reference file** locally (if the skill is installed) or fetch via `GET /api/v1/document/skill_refs/{source_id}`
3. **Search for citations**: `POST /api/v1/search` with `sources: ["local"]` (or `["local", "fashi"]`) for citable evidence
4. **Fetch full source text**: use the appropriate fetch endpoint based on `fetch_ref.source`
   - `source: "local"` → `GET /api/v1/local/{source_id}`
   - `source: "fashi"` → `GET /api/v1/fashi/{source_id}`
   - `source: "skill_refs"` → `GET /api/v1/document/skill_refs/{source_id}`
5. Use `match_text` on local fetches to get focused context windows instead of entire documents
