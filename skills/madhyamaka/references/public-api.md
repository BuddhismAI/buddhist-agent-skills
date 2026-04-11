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
| `sources` | string[] | no | both | `["local"]`, `["fashi"]`, or omit for both |
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

1. **Search**: `POST /api/v1/search` with your query
2. **Pick a result** and note its `fetch_ref`
3. **Fetch full text**: use the appropriate fetch endpoint based on `fetch_ref.source`
   - `source: "local"` → `GET /api/v1/local/{source_id}`
   - `source: "fashi"` → `GET /api/v1/fashi/{source_id}`
4. Use `match_text` on local fetches to get focused context windows instead of entire documents
