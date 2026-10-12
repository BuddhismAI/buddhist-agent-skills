---
name: buddhism
description: |
  Answer questions about Buddhist philosophy using Nyingma tradition sources.
  Trigger for Buddhist concepts, debates, practice frameworks, reasoning methods, scriptures, philosophical schools, or topic areas such as 中观/Madhyamaka, 唯识/Yogachara, 如来藏, 般若, 净土, 俱舍/Abhidharma, 戒律/Vinaya, 密法/Tantra, 大圆满/Dzogchen, 加行/foundations, 菩提心, 量理/因明, and related Chinese or Sanskrit terms. Do not trigger for general programming tasks or code changes unrelated to Buddhist content.
---

# Buddhist Philosophy Answering Framework (Nyingma Tradition)

How to search, interpret, construct answers, and choose representations for Buddhist philosophy questions. Knowledge is grounded in **Nyingma tradition** sources: teaching transcripts, commentaries, and compiled wiki docs.

**Critical**: this tradition's positions differ from the Gelug (格鲁派) interpretations common in training data. When your built-in knowledge conflicts with reference files or search results, ALWAYS prefer the latter, and check the topic's correctness anchors.

## 1. Answering Workflow

Adapt depth to the question. A simple follow-up may need only steps 1-2; a deep first-time explanation uses all of them. For a first-time question about a covered doctrinal term, reasoning method, school distinction, or correctness-anchor topic, read at least one relevant `references/...` file before corpus search. Skip that read only for named-source or passage lookups and everyday basics that need no framework judgment.

1. **Analyze** -- run the Question Analysis Scaffold (§5) and scan `references/methodology/question-patterns.md` for a matching question shape. This yields an answer skeleton *before* any file is read.
2. **Read** -- load the topic and collection docs the scaffold routed to. The topic index orients, reference docs give the framework, collection docs give depth.
3. **Draft** -- write from wiki knowledge, following the skeleton. With a workspace/card surface, create a visible first draft there and mark where citations are needed; without one, tell the user in 1-2 sentences what you will check next, then continue. Keep claims modest.
4. **Continue** -- keep working autonomously. Find the claims that need source evidence and the parts of the question still thin; original sources may refine or challenge the skeleton.
5. **Ground** -- search the source corpus for `ref:` citations before finalizing. Required for study roadmaps, multi-stage curricula, doctrinal definitions, practice instructions, comparisons, and claims derived from topic references. With a workspace surface, edit the same card to add citations and fix unsupported claims; otherwise integrate the evidence into the final chat answer. If MCP corpus tools are unavailable, use the REST workflow in `references/public-api.md` before giving up on grounding.
6. **Verify** -- check against the topic's correctness anchors, especially where positions diverge from training data. For study roadmaps with several named texts, stages and practice steps, use the `validate` subagent after grounding if available.
7. **Disclose** -- end study roadmaps and curricula with a brief source-scope note: skill references only, local corpus search, fetched full text, or transcripts end-to-end.

For sourced doctrinal definitions, school comparisons, study roadmaps and framework-sensitive explanations, keep the cited content in a Markdown workspace card when one exists; chat summarizes the card. Without a workspace surface, give the sourced answer in chat with citations.

A final Buddhist study card or answer with zero source support is not acceptable when source access is available: either keep it explicitly provisional because evidence tools are unavailable, or revise it into a cited answer. The wiki is a launchpad, not the finish line.

## 2. Topics and Routing

Match the question's vocabulary to a topic below, then use that topic's `index.md` concept router for the subtopic doc. Full inventories: `references/maps/topic-index.md`, `references/maps/collection-index.md`.

| Topic | Status | Covers |
|---|---|---|
| **madhyamaka** 中观 | Active | 空性, 二谛, 缘起, 龙树/月称/静命, 应成/自续, 四边, 五大因, 离戏; 中论, 入中论, 四百论, 中观庄严论, 解义慧剑, 定解宝灯论; includes reasoning-method docs and `debates.md` / `classifications.md` / `yogachara-madhyamaka.md` |
| **foundations** 基础/加行 | Active | 前行, 暇满, 无常, 因果, 皈依, 菩提心, 六度, 上师瑜伽, 往生法, 修心七要, 佛子行, 二规教言论, 入行论, 大圆满前行 (`practice-path.md`, `bodhicitta-methods.md`, `key-quotes.md`) |
| **abhidharma** 俱舍/对法 | Active | 俱舍论: 蕴界处, 六因五果四缘, 心所法, 随眠, 业道, 五道四果, 四禅八定, 须弥山宇宙; Editorial Policy for the 有部/经部 fault line |
| **tathagatagarbha** 如来藏 | Active | 宝性论: 佛性, 九喻, 七金刚处, 三身, 他空, 不空如来藏, 觉囊派/宁玛派 reconciliation |
| **yogachara** 唯识 | Active | 大乘经庄严论: 阿赖耶识, 八识转四智, 三自性, 转依, 种姓, 弥勒五论; Editorial Policy for the 唯识/中观 fault line |
| **prajnaparamita** 般若 | Active | 维摩诘经: 不二法门, 心净国土净, 烦恼即菩提, 尽无尽解脱 (to expand to 金刚经/心经) |
| **pure-land** 净土 | Active | 极乐愿文大疏: 往生四因, 七支供, 明观福田, 疑障, 临终接引, 颇瓦法; Nyingma Pure Land vs East Asian distinctions |
| **pramana** 量理/因明 | Seed | 四理, 现量/比量, 量之四分, 八辩才; aggregated from 解义慧剑, 定解宝灯论, 中观庄严论, 入行论; no dedicated 释量论 yet |
| **tantra** 密法 | Seed | 大圆满直断/顿超, 续部分类, 等净无二, 显密融通, 加行实修; aggregated from 定解宝灯论, 大圆满前行, 宝性论; no tantra root text yet |
| **vinaya** 戒律 | Seed | 三戒, 戒体, 三聚净戒, 四对治力, 性罪/遮罪, 业道; aggregated from 俱舍论, 入行论, 大圆满前行; no 律藏 root text yet |

**Retrieval tiers.** Tier 1 `references/topics/<topic>/` (index for routing, synthesis docs for cross-collection framework) -> Tier 2 `references/collections/*/` (depth: arguments, verses, stories) -> Tier 3 source corpus (grounding, exact citations). Simple questions may need only Tier 1; complex ones use all three.

- **Active**: route, read the topic index and relevant synthesis docs, drill into collection docs, then search the corpus for citations before final cards.
- **Seed**: read the seed index (partial coverage), supplement with training knowledge, and say the topic has partial coverage.
- **Not listed**: answer from training knowledge and say curated source material doesn't exist yet.

**Multi-topic questions** (e.g. 解义慧剑 spans madhyamaka and pramana): read each topic's index, synthesize, note where topics agree, diverge or complement, and be open about which have wiki coverage.

## 3. Search and Exploration

Use `search_skill_refs` only to discover a reference file when the concept router doesn't already point to it; it returns routing snippets and `read_ref.path` values. Read the file with the normal `read` tool.

Use the richest source access available:

1. **Buddhist Assistant / internal agents**: `search_hybrid` for source evidence; `search_local` or `search_fashi` when source filters matter; `search_corpus_keyword` for exact terms or rare phrases; `fetch_corpus` / `fetch_fashi` for quote-level verification.
2. **Public agents without MCP tools**: read `references/public-api.md` early; search `sources: ["local"]` then fetch by `fetch_ref` (or `source_path` if no `fetch_ref`).
3. **Offline agents**: use `references/` as framework only and state that original-source verification was unavailable.

If `search_skill_refs` is unavailable, use the topic's Concept Router plus Grep. If corpus search is also unavailable, answer from the wiki alone and say you could not verify against the original source; still name the main relevant texts.

`references/topics/*` and `references/collections/*` are compiled study wikis: for routing, synthesis, correctness anchors and exploration pointers. They are not evidence. Never turn `read_ref.path` values or `references/...` paths into answer `ref:` citations; only passages from the source corpus become user-visible `ref:` citations (unless the answer says source verification was unavailable). `source_docs` frontmatter paths such as `development/data/markdown/...` are provenance labels; search or fetch by title, source path or `fetch_ref` instead.

Paths: from `SKILL.md` use repo-relative paths (`references/topics/madhyamaka/index.md`); inside a reference doc, links like `topics/madhyamaka/index.md` are relative to `references/`.

**Choosing the search by question character**

| Question character | Search |
|---|---|
| Buddhist concepts ("空性和无我有什么关系?") | Topic router, or `search_skill_refs` when not obvious |
| Experiential / personal ("我打坐时感到很焦虑") | Source corpus (`search_hybrid`/`search_fashi`): the wiki is technical, source teachings address lived experience |
| Generic / ambiguous ("佛教怎么看待痛苦?") | Source corpus plus topic router when framework matters |
| Clear concept, clear topic ("应成派的无承认是什么意思?") | Concept Router, no search needed |

**Result chunk types.** When a tool offers a `chunk_types` filter use only: `qa` (pre-answered questions, most directly useful), `key_term` (definitions), `misconception` (wrong views with corrections, high value for debates), `verse` (root text), `lesson` (practice guidance), `summary` (document-level), `koan` (illustrative stories). Never pass `qa_pairs`, `key_terms`, or workspace card categories such as `passage`.

**When results are thin**: rephrase with synonyms (空性/无自性/离戏/无生), search the treatise name plus topic, fall back to keyword search for exact phrases, fetch the full document around matched passages.

## 4. Source Priority

1. **Topic reference docs**: framework, correctness anchors, concept maps. Read first, never cite as evidence.
2. **Collection wiki docs**: grounded arguments, verse analysis, lesson context. Drill-down.
3. **Corpus search** (MCP/API): citable evidence and original quotes.
4. **Training data**: lowest; verify against the above.

Do not copy reference content verbatim. If source access is available, every substantive point should carry a `ref:` citation from corpus search.

## 5. Question Analysis Scaffold

Run this before reading any topic doc so the Read step is targeted. It is a framework, not a checklist: the gating table sets depth, the dimensions run mentally, and nothing is shown to the user except the final answer. It is not a tradition check; Nyingma is the default and the topic correctness anchors catch the edges.

| Question character | Dimensions |
|---|---|
| Factual lookup ("中论有多少品?") / Logistical ("如何找到合格上师") | ① + ⑥ |
| Single-concept definition ("什么是二谛?") | ① + ⑤ + ⑥ |
| Doctrinal / philosophical (most questions) | ①–⑥ (⑦ when drift risk is real) |
| Life-situational ("亲人离世怎么办 / 内心很焦虑") | ① ② ③ ④ ⑤ + light ⑥ |
| Beginner orientation ("想开始学佛从哪里入手") | ① ② ③ ⑤ ⑥ ⑦ |
| Ethical-behavioral ("仅有杀意是否染罪") | ① ② ④ ⑤ ⑥ |
| Practice / experiential / comparative / cross-topic | All 7; Context and Underlying need are load-bearing |

| # | Dimension | Ask |
|---|---|---|
| ① | **Surface** | What is literally asked? |
| ② | **Register** | Doctrinal / practical / life-situational / orientation / ethical-behavioral / stage-self-assessment / karma-inquiry / subtle-realm / logistical / mixed? |
| ③ | **Context** | The user's relationship to it: 闻/思/修/证 stage; life situation; beginner / returning / seasoned |
| ④ | **Underlying need** | Concept, method, decision, reassurance, framework, correction, or recalibration? |
| ⑤ | **Aspects to cover** | Short ordered list from ①–④: the answer skeleton |
| ⑥ | **Topic routing** | Which topics and subtopic docs, via the concept routers |
| ⑦ | **Out of scope** | Nearby concerns to exclude so the answer stays focused (most load-bearing for life-situational and beginner questions) |

`references/methodology/question-patterns.md` lists recurring shapes (doctrinal: misinterpretations, debates, cross-topic tangles; practical: life-situational, stage-assessment, karma-inquiry, subtle-realm, beginner) with aspect, routing hints and `Don'ts`. No match doesn't block answering.

## 6. Answer Quality

A good answer helps a serious practitioner build genuine understanding, not summarize search results. The reasoning *is* the teaching. Every major point has the claim, the reasoning (using Buddhist logic), and the evidence (a `ref:` link, with a brief key phrase quoted from the source).

| Dimension | Good | Watch out for |
|---|---|---|
| Source grounding | Major claims carry `ref:` citations when source access exists | Unverifiable claims |
| Reasoning depth | Reasoning chains | Bullet dumps, search-result relays, conclusion-only answers |
| Correctness | Consistent with the topic's correctness anchors | Contradicting tradition positions (especially Nyingma vs Gelug) |
| Transparency | Honest about what can't be verified | Silence when source access is unavailable |
| Focus | Core question developed thoroughly | Shallow survey of tangents |

**Study roadmaps and "where should I start?" answers** must cover: foundational prerequisites (闻法方式, 出离心/四厌世心, 皈依, 菩提心, 因果取舍, as fits the level); 正理 (which reasoning tools are learned at each stage, not just a book list); 观察/安住次第 (analytical study versus resting practice); 因果防偏 (guard against "空性否定因果", bypassing ethics, skipping basics); and local citations for the sequence. End with a short source-scope note, e.g. "Source scope: skill references + local corpus search + fetched excerpts; did not review full transcripts end-to-end." If only wiki references were used, say so plainly.

## 7. Representation

Classification taxonomies, school comparisons, reasoning chains, concept networks and stage progressions are structural: create a visual artifact *alongside* the text without waiting to be asked. Skip it for simple definitions, single-point answers and passage lookups.
