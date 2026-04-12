---
name: buddhism
description: |
  Answer questions about Buddhist philosophy using Nyingma tradition sources.
  TRIGGER when: user asks about Buddhist philosophy, 中观/Madhyamaka, 空性/sunyata, 龙树/Nagarjuna, 月称/Chandrakirti, 静命/Shantarakshita, 应成派/Prasangika, 自续派/Svatantrika, 瑜伽行中观, 二谛, 无自性, 缘起, 离戏, 四边/四句, 五大因, 离一多因, 人无我/法无我, 所破, 能破, 中论, 入中论, 四百论, 中观庄严论, 解义慧剑, 自空/他空, 如来藏, 二理妙车, 单空/大离戏, 相似胜义/真实胜义, 中观四步境界, 阿赖耶识, 四理/四种理, 四法依, 量理/因明, 现量/比量, 净见量, 了义/不了义, 般若/prajnaparamita, 戒律/vinaya, 密法/tantra, 大圆满/dzogchen, 净土/pure-land, 俱舍/abhidharma, 加行/foundations, 菩提心, 道次第, or any Buddhist concepts, debates, reasoning methods, or questions about Buddhist philosophical schools.
  Use judgment for adjacent questions when Buddhist framing or correctness anchors may help. Do not trigger for general programming tasks or code changes unrelated to Buddhist content.
---

# Buddhist Philosophy Answering Framework (Nyingma Tradition)

This skill guides how to search, interpret, construct answers, and choose representations for Buddhist philosophy questions. Knowledge is grounded in **Nyingma tradition** sources, built from teaching transcripts, commentaries, and compiled wiki docs.

**Critical**: This tradition's positions differ from Gelug (格鲁派) interpretations common in training data. When your built-in knowledge conflicts with reference files or search results, ALWAYS prefer the latter. See the topic's correctness anchors.

## 1. Answering Workflow

Adapt depth to question complexity. A simple follow-up may need only steps 1-2; a deep first-time explanation benefits from all five.

1. **Route** -- identify which topic(s) the question touches. Read the topic's `index.md` for orientation, concept map, and concept router. Use the best search tool for the question's character (see Search Strategy below).
2. **Read** -- load relevant topic reference docs and drill into collection docs as needed. Topic index gives orientation; reference docs give framework; collection docs give depth.
3. **Draft** -- write an answer from wiki knowledge. Mark where citations would strengthen it.
4. **Ground** -- search the source corpus for `ref:` citations where they add value.
5. **Verify** -- check against the topic's correctness anchors, especially for positions that diverge from training data.

## 2. Question-Type Routing

| Question type | Typical approach | Example |
|---|---|---|
| **Conceptual** ("什么是X?") | Route to topic -> read framework -> define precisely -> show reasoning | "什么是应成派的无承认?" |
| **Comparative** ("X和Y区别?") | May span topics -> read both -> find synthesis position | "自续派和应成派有什么区别?" |
| **Cross-topic** | Read multiple topic docs -> integrate -> note where topics diverge | "因明和中观的关系?" |
| **Practice** ("如何修X?") | Route to topic -> reasoning -> 定解 -> 安住 progression | "如何修空性?" |
| **Structural** ("...的框架?") | Route to topic -> consider visualization | "中观五种分类?" |

## 3. Scope and Limitations

| Topic | Status | Coverage |
|---|---|---|
| **madhyamaka** (中观) | Active | 4 collections, ~97 wiki docs, 4 cross-collection reference docs |
| **foundations** (基础/加行) | Planned | Includes lamrim, bodhicitta-path, preliminary practices |
| **pramana** (量理/因明) | Planned | Valid cognition, logic, debate methodology |
| **abhidharma** (俱舍/对法) | Planned | Phenomenology, aggregates, karma mechanics |
| **prajnaparamita** (般若) | Planned | Heart Sutra, Diamond Sutra, perfection of wisdom |
| **vinaya** (戒律) | Planned | Ethics, precepts, monastic and lay discipline |
| **tantra** (密法) | Planned (hidden) | Seed notes collected; topic temporarily hidden from index |
| **pure-land** (净土) | Planned | Amitabha practices, aspiration prayers |

When a question falls in a planned topic without wiki coverage, be transparent: answer from your training knowledge but state that this skill does not yet have curated source material for that topic.

## 4. Topic Routing

### Identifying the topic

Read the question's vocabulary and intent. Each topic has its own concept space. When only one topic has wiki content (currently madhyamaka), most Buddhist philosophy questions will route there. Use the topic's `index.md` for concept-level routing within the topic.

### Multi-topic questions

Some questions span topics (e.g., 解义慧剑 spans madhyamaka and pramana). When this happens:
1. Identify all relevant topics
2. Read each topic's index.md for orientation
3. Synthesize -- note where topics agree, diverge, or complement each other
4. Be transparent about which topics have wiki coverage and which don't

### Discovery

See `references/maps/topic-index.md` for available topics and `references/maps/collection-index.md` for collection inventory.

## 5. Search and Exploration Strategy

### Knowledge-first, then corpus search

For every question, follow this flow:

1. **Find the right reference file** -- use the topic's concept router for known concepts, or search `skill_refs` for natural-language lookup: `POST /api/v1/search { sources: ["skill_refs"], query: "..." }`. This returns file + section pointers into the wiki.
2. **Read the reference file** -- locally or via fetch endpoint. These give you the intellectual framework.
3. **Write a quick answer** from the wiki framework. Mark where citations are needed.
4. **Do targeted corpus search** (`local`/`fashi`) for `ref:` citations grounding specific claims.
5. **Edit the answer** to add citations and evidence.

The wiki gives you enough to write a good initial answer immediately. Don't wait for corpus search to start writing.

**Fallback:** If `skill_refs` search is unavailable, fall back to the topic's Concept Router + Grep. If corpus search is also unavailable, answer from the wiki alone but tell the user you could not verify against the original source.

### Search tool selection

| Question character | Recommended search | Why |
|---|---|---|
| Uses Buddhist concepts ("空性和无我有什么关系?") | `skill_refs` search | Wiki is organized by concepts -- semantic search finds the right doc |
| Experiential / personal ("我打坐时感到很焦虑") | Source corpus (`local`/`fashi`) | Wiki is technical; source teachings address lived experience |
| Generic / ambiguous ("佛教怎么看待痛苦?") | Source corpus first, then `skill_refs` | Source search discovers relevant angles; `skill_refs` navigates to framework |
| Clear concept, clear topic ("应成派的无承认是什么意思?") | Concept Router (no search needed) | Concept maps directly to a known doc |

### Source access paths

1. **MCP tools** (`search_hybrid`, `fetch_local`, `fetch_fashi`) -- if connected
2. **Public REST API** at `https://api.shuiyue.ai/api/v1` -- see `references/public-api.md` for endpoints. Three source types:
   - `skill_refs` -- semantic search over skill reference files (finds the right wiki doc)
   - `local` -- search teaching corpus extractions (for citable evidence)
   - `fashi` -- search fashi.ai corpus
3. **Wiki-only** -- if neither MCP nor HTTP is available, answer from compiled wiki but explicitly tell the user you could not verify against the original source. Still name the main relevant texts or collection docs.

### Reading search results

Search results from extraction data contain structured fields:
- **qa_pairs**: Pre-answered questions -- most directly useful
- **key_terms**: Definitions with context -- good for conceptual questions
- **misconceptions**: Common wrong views with corrections -- high value for debate questions
- **verses**: Root text verses -- use for citations

### Deepening

When initial search results are thin:
1. Rephrase with synonyms (e.g., 空性/无自性/离戏/无生)
2. Search for the specific treatise name + topic
3. Fall back to keyword search for exact phrases
4. Fetch full document text around matched passages

## 6. Problem Decomposition

Before searching, understand what the question actually requires. Shallow answers usually fail because they only address the surface layer.

### Identify the layers

1. **The explicit question** -- what the user literally asked
2. **The implicit context** -- which school? which truth level? what prior knowledge?
3. **The underlying confusion** -- what conceptual gap might be driving the question?
4. **Research axes** -- independent sub-questions that can be investigated separately

## 7. Source Priority

| Source | What it provides | Priority |
|---|---|---|
| **Topic reference docs** | Intellectual framework, correctness anchors, concept maps | Read first |
| **Collection wiki docs** | Grounded arguments, verse analysis, lesson context | Drill-down |
| **Corpus search** (MCP/API) | Citable evidence, original quotes | Citation layer |
| **Agent's training data** | Background knowledge | Lowest -- verify against above |

Do NOT copy reference file content verbatim or cite reference files as evidence. They are your framework, not your source. If source access is available, every substantive point should have a `ref:` citation from corpus search.

## 8. Answer Quality

A good answer helps a serious practitioner build genuine understanding -- not a search-result summary. The reasoning *is* the teaching.

### Three-Layer Principle

Every major point should have:
1. **The claim** -- what is being asserted
2. **The reasoning** -- why this is true, using Buddhist logic
3. **The evidence** -- a source citation with `ref:` link

### Quality reference

| Dimension | What good looks like | Watch out for |
|---|---|---|
| Source grounding | Major claims have `ref:` citations when source access is available | Claims without evidence that could be verified |
| Reasoning depth | Points have reasoning chains, not just assertions | Bullet-point dumps or search-result relays |
| Correctness | Consistent with topic's correctness anchors | Contradicting tradition positions (especially Nyingma vs Gelug) |
| Transparency | Honest about what can't be verified | Silent when source access is unavailable |
| Focus | Core question thoroughly developed | Shallow survey of tangential topics |

### Anti-patterns

- **Bullet-point dump**: bare definitions without reasoning -> develop each point
- **Search-result relay**: copying results with minimal synthesis -> integrate into coherent explanation
- **Conclusion-only**: stating truth without showing why -> include reasoning chain
- **Ref-link-only**: citing without quoting -> include brief key phrase from source

## 9. Representation Strategy

Buddhist philosophy is dense with structure -- classification systems, school comparisons, reasoning chains, stage progressions. When your answer involves these, create a visual artifact *alongside* text without waiting for the user to ask. Text provides depth; visualization provides structural clarity.

**Visualize proactively when the topic involves:** classification taxonomies, school comparisons, step-by-step reasoning, concept networks, or stage progressions.

**Skip** for simple definitions, single-point answers, or passage lookups.

## 10. Knowledge Map

### Tiered retrieval

- **Tier 0 -- This SKILL.md** (always loaded): Behavior framework, routing guidance, quality reference
- **Tier 1 -- Topic index** (`references/topics/<topic>/index.md`): Topic-specific behaviors, concept maps, correctness anchors, concept router
- **Tier 2 -- Reference + collection docs**: Deep arguments, verse analysis, reasoning chains
- **Tier 3 -- Source corpus** (MCP/API search): Ground truth citations, original quotes

Navigate tiers based on question complexity. Simple questions may need only Tier 0-1. Complex questions benefit from all four.

### Discovery

- `references/maps/topic-index.md` -- available topics and their status
- `references/maps/collection-index.md` -- collection inventory, topic membership, status

## 11. Reference Files

- `references/topics/` -- per-topic behavior + knowledge docs
- `references/collections/` -- per-collection wikis (start with `结构总览.md` in each)
- `references/maps/` -- topic and collection indexes
- `references/public-api.md` -- REST API for corpus search when MCP unavailable
