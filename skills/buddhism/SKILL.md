---
name: buddhism
description: |
  Answer questions about Buddhist philosophy using Nyingma tradition sources.
  Trigger for Buddhist concepts, debates, practice frameworks, reasoning methods, scriptures, philosophical schools, or topic areas such as 中观/Madhyamaka, 唯识/Yogachara, 如来藏, 般若, 净土, 俱舍/Abhidharma, 戒律/Vinaya, 密法/Tantra, 大圆满/Dzogchen, 加行/foundations, 菩提心, 量理/因明, and related Chinese or Sanskrit terms. Do not trigger for general programming tasks or code changes unrelated to Buddhist content.
---

# Buddhist Philosophy Answering Framework (Nyingma Tradition)

This skill guides how to search, interpret, construct answers, and choose representations for Buddhist philosophy questions. Knowledge is grounded in **Nyingma tradition** sources, built from teaching transcripts, commentaries, and compiled wiki docs.

**Critical**: This tradition's positions differ from Gelug (格鲁派) interpretations common in training data. When your built-in knowledge conflicts with reference files or search results, ALWAYS prefer the latter. See the topic's correctness anchors.

## 1. Answering Workflow

Adapt depth to question complexity. A simple follow-up may need only steps 1-2; a deep first-time explanation benefits from all five. For first-time questions about a covered doctrinal term, reasoning method, school distinction, or correctness-anchor topic, read at least one relevant `references/...` file before corpus search even when a direct source search might also work. Skip the reference-file read only for named-source/passage lookup or everyday basics where no framework judgment is needed.

1. **Analyze** -- run the Question Analysis Scaffold (§6) to identify register, aspects to address, routing targets, and out-of-scope concerns. Produces a concrete answer skeleton *before* reading any file. Also scan the pattern library (`references/methodology/question-patterns.md`) for a matching question shape.
2. **Read** -- load the topic reference docs and collection docs the scaffold's Topic Routing step identified. Topic index gives orientation; reference docs give framework; collection docs give depth.
3. **Draft** -- write an answer from wiki knowledge, following the aspect skeleton from step 1. Treat this as a scaffold: mark where citations would strengthen it, and do not finalize a workspace card from wiki/reference knowledge alone.
4. **Ground** -- search the source corpus for `ref:` citations before finalizing workspace cards. Citations are especially required for study roadmaps, multi-stage curricula, doctrinal definitions, practice instructions, comparisons, and claims derived from topic references.
5. **Verify** -- check against the topic's correctness anchors, especially for positions that diverge from training data.
   For study roadmaps or curriculum cards with several named texts, stages, and
   practice steps, use the runtime `validate` subagent after grounding if it is
   available.

For sourced doctrinal definitions, school comparisons, study roadmaps, and framework-sensitive explanations, the cited content should be preserved in a Markdown workspace card. Chat can summarize what the card contains, but should not be the only place where the sourced answer lives.

## 2. Question-Type Routing

Quick reference only. **For the full decomposition methodology, use the Question Analysis Scaffold (§6).** §6's Register dimension subsumes these question types; the table below is a fast shortcut when the type is obvious.

| Question type | Typical approach |
|---|---|
| **Conceptual** ("什么是X?") | Route to topic → read framework → define precisely → show reasoning |
| **Comparative** ("X和Y区别?") | May span topics → read both → synthesize |
| **Cross-topic** | Read multiple topic docs → integrate → note where topics diverge or 圆融 |
| **Practice** ("如何修X?") | Route to topic → reasoning → 定解 → 安住 → 应用 progression |
| **Structural** ("...的框架?") | Route to topic → consider visualization (see §9) |

## 3. Scope and Limitations

| Topic | Status | Coverage | Routing keywords |
|---|---|---|---|
| **madhyamaka** (中观) | Active | 5 collections, 106 docs (incl. 11 reasoning-method docs), topic index + 4 synthesis docs (`reasoning-methods.md`, `debates.md`, `classifications.md`, `yogachara-madhyamaka.md`) | 空性, 中观, 二谛, 缘起, 龙树, 月称, 静命, 应成/自续, 离戏, 四边, 五大因, 离一多因, 所破/能破, 中论, 入中论, 四百论, 中观庄严论, 解义慧剑, 定解宝灯论 |
| **foundations** (基础/加行) | Active | 5 collections (大圆满前行 18, 入行论 28, 修心七要 8, 佛子行 15, 二规教言论 13), topic index + 3 synthesis docs (`practice-path.md`, `bodhicitta-methods.md`, `key-quotes.md`) | 前行, 加行, 道次第, 暇满, 无常, 轮回, 因果, 皈依, 菩提心, 四无量心, 六度, 金刚萨埵, 百字明, 曼茶罗, 上师瑜伽, 往生法, 出离心, 三殊胜, 自他相换, 修心, 修心七要, 五力, 狮子卧, 恰卡瓦, 金洲大师, 大圆满前行, 入行论, 佛子行, 三十七颂, 无著贤, 甘露妙瓶, 根桑秋札, 恶缘转道用, 经中四法, 四不欲, 两难忍, 兴衰转道, 二规, 二规教言论, 佛规, 人规, 妙慧, 稳重, 有愧, 不放逸, 正直, 誓言坚定, 知恩图报, 利他, 信心, 布施, 十种功德, 世法即佛法根, 护法神, 麦彭仁波切 |
| **abhidharma** (俱舍/对法) | Active | 1 collection (俱舍论 16 docs, 160 lessons), topic index with Editorial Policy for 有部/经部 fault-line | 俱舍, 阿毗达磨, 蕴界处, 五蕴, 十二处, 十八界, 六因五果四缘, 心所法 (46/51), 二十二根, 不相应行, 无表色, 极微, 有漏无漏, 三无为, 十二缘起, 业道, 表业/无表业, 别解脱戒, 随眠 (98), 见所断/修所断, 三世实有, 圣道, 五道, 四向四果, 十六心, 三十七菩提分, 阿罗汉退转, 十智, 十力, 四无畏, 大悲, 三明六通, 四禅八定, 八解脱, 八胜处, 十遍处, 四无量心, 须弥山宇宙 |
| **tathagatagarbha** (如来藏) | Active | 1 collection (宝性论 14 docs, 42 lessons), topic index with Editorial Policy for 觉囊派/宁玛派 reconciliation | 如来藏, 佛性, 宝性论, 究竟一乘宝性论, 无上续, 弥勒五论, 有垢/无垢真如, 七金刚处, 三宝本体, 九喻, 九种垢, 种姓, 三身, 法身/报身/化身, 十力, 四无畏, 十八不共法, 离系果, 异熟果, 不空如来藏, 他空, 句他空, 义他空, 朵洛瓦, 觉囊派, 客尘, 《如来藏大纲要狮吼论》, 《法界赞》, 《不增不减经》, 《胜鬘经》, 《如来藏经》, 佛外无涅槃 |
| **yogachara** (唯识/瑜伽行) | Active | 1 collection (大乘经庄严论 complete, 25 docs, 111 lessons across 21 品), topic index at `topics/yogachara/index.md` with Editorial Policy for 唯识/中观 fault-line handling (本论唯识本文 / 索达吉堪布宁玛重释 / 中观对唯识实有派破斥 三层) | 唯识, 瑜伽行, yogachara, cittamātra, 弥勒菩萨, 无著菩萨, 世亲, 安慧, 弥勒五论, 大乘经庄严论, 辩中边论, 辨法法性论, 瑜伽师地论, 法相宗, 阿赖耶识, 末那识, 八识, 八识转四智, 转依, 三自性, 遍计所执, 依他起, 圆成实, 三无性, 唯识所现, 唯识无境, 万法唯心, 所取能取, 相分见分, 自证分, 习气种子, 种姓品 (大乘种姓), 真如 (唯识式), 二无我 (唯识式), 三身, 自性身/法身/报身/化身, 四智, 大圆镜智/平等性智/妙观察智/成所作智, 三平等三恒常, 五法 (本论1+4), 七义, 五种无上意义, 八大理由证大乘是佛语, 四秘密四意趣, 22发心喻, 51种作意, 转依七种, 甚深16种, 任运事业四喻, 十七种修行功德, 九种菩萨赞叹, 五相菩萨, 四种受生, 菩提六安立, 密意疏, 胜乘甘露喜宴, 麦彭仁波切密意疏 |
| **pramana** (量理/因明) | Seed | Aggregated topic index at `topics/pramana/index.md` drawing from 解义慧剑, 定解宝灯论, 中观庄严论, 入行论. Covers 四理, 现量四种, 比量三要, 量之四分 (观现世/净见/相似胜义/真实胜义), 四法依, 八辩才, 量士夫. No dedicated 因明 root text yet (e.g., 《释量论》). | 因明, 量理, pramāṇa, 释量论, 法称, 陈那, 现量, 比量, 自证现量, 观现世量, 净见量, 相似胜义量, 真实胜义量, 量之四分, 四理, 作用理, 观待理, 法尔理, 证成理, 因三相, 四法依, 八辩才, 量士夫, 自证, 遣余, 共相/自相 |
| **tantra** (密法/金刚乘) | Seed | Aggregated topic index at `topics/tantra/index.md` drawing from 定解宝灯论 (Q4-Q7), 大圆满前行, 宝性论. Covers 大圆满直断/顿超, 续部分类, 等净无二, 显密融通, 加行视角实修 (金刚萨埵/上师瑜伽/往生法), 显密三身差别. No dedicated tantra root text yet (e.g., 大幻化网, 心性休息). | 密法, 密宗, 金刚乘, 大圆满, dzogchen, 直断, 顿超, 童子瓶佛身, 灌顶, 三昧耶, 生起次第, 圆满次第, 玛哈/阿努/阿底约嘎, 九乘次第, 等净无二, 显密融通, 大圆满三部, 三种智慧, 大手印, 道果, 息法, 双运大中观, 续部分类 |
| **prajnaparamita** (般若) | Active | 1 collection (维摩诘经 complete, 21 docs, 14 品 / 66 lessons), topic index at `topics/prajnaparamita/index.md` with full concept router, correctness anchors (心净国土净非唯心 / 烦恼即菩提 / 不二非一 / 秽土修行不否定净土法门 / 居士相非普通在家人), cross-topic connections to madhyamaka / foundations / tathagatagarbha / tantra | 般若, 心经, 金刚经, 波罗蜜多, 维摩诘, 维摩诘经, 无垢称经, 维摩诘居士, 不二法门, 入不二法门, 默然无言, 心净国土净, 烦恼即菩提, 非道即佛道, 一切烦恼为如来种, 菩萨净土, 十七种净土因, 方便示疾, 不可思议解脱, 以空病空, 文殊问疾, 天女散花, 舍利弗转女身, 观众生十一喻, 真实四无量心, 无住为本, 莲华喻, 普现色身, 三十一菩萨不二, 菩萨成就八法, 尽无尽解脱法门, 不尽有为不住无为, 香积国, 妙喜国, 阿閦佛, 观佛实相, 法供养, 药王菩萨, 月盖比丘, 菩萨二印 |
| **pure-land** (净土) | Active | 1 collection (极乐愿文大疏 complete, 14 top docs + 4 reasoning-method docs + 结构总览, 104 lessons), topic index at `topics/pure-land/index.md` with concept router, correctness anchors (学密者可往生 / 除五无间舍法罪外皆可生 / 疑心是最大障非业障 / 女身可往生 / 极乐非纯心现亦非物理某地 / Nyingma不主张独修 / 临终可诵极乐愿文本身), Key Distinctions from East Asian Pure Land, cross-topic connections to foundations / tantra / madhyamaka / prajnaparamita / abhidharma / vinaya | 净土, 极乐, 极乐世界, 往生, 往生极乐, 阿弥陀佛, 无量光佛, 无量寿佛, 观世音菩萨, 大势至菩萨, 莲花生大士 (as Amitabha's 化身), 极乐愿文, 极乐愿文大疏, 乔美仁波切, 喇拉曲智仁波切, 往生四因, 明观福田, 积资净障, 发菩提心, 发清净愿, 七支供, 对治七烦恼, 四对治力, 所依/厌患/现行/返回, 真实供养, 意幻供养, 自成供养, 五无间罪, 近无间罪, 舍法罪, 诽谤菩萨罪, 恶见罪, 佛制罪, 别解脱戒, 菩萨戒十八堕, 密乘十四根本, 八粗支, 闻名功德, 闻名合掌福胜三千界, 闻名不退转菩提, 闻名不转女身, 生生世世具净戒, 持佛号救八难, 水火毒兵夜罗刹, 化生莲花, 四生中最胜, 五眼五通, 疑障五百岁, 花不绽放, 八功德水, 无量宫, 现喜刹, 具德刹, 妙圆刹, 密严刹, 妙拂洲, 邬金刹, 普陀山, 杨柳宫, 三佛相续住世, 胜光妙聚王如来, 坚德宝聚王如来, 成愿咒, 增倍咒, 达雅塔班赞哲雅, 谛实语加持, 陀罗尼, 法王如意宝, 晋美彭措, 极乐法会, 印光大师, 临终接引, 中阴接引, 八大菩萨接引, 临终十念, 临终助念, 狮子卧, 颇瓦法, 往生法 |
| **vinaya** (戒律) | Seed | Aggregated topic index at `topics/vinaya/index.md` drawing from 俱舍论 品4 (戒律法相基础), 入行论 (菩萨戒完整体系), 大圆满前行 (业果与三昧耶). Covers 三戒分类, 戒体的传统差异, 三聚净戒, 四对治力, 性罪/遮罪, 业道. No dedicated 律藏 root text yet (e.g., 萨班《三律仪论》, 《菩萨戒品》). | 戒律, vinaya, 戒, śīla, 律仪, 三戒, 别解脱戒, prātimokṣa, 菩萨戒, 三聚净戒, 摄律仪/摄善法/饶益有情, 密乘戒, 三昧耶, samaya, 戒体, 无表色, 表业无表业, 业道, 十善/十不善业道, 五无间罪, 四对治力, 性罪/遮罪, 学处, 还净, 受戒, 舍戒, 持戒/破戒 |

**Three-tier retrieval model** (for Active topics):

```
Tier 1: SKILL.md         → routing (which topic? always in context)
Tier 2: topics/<topic>/   → orientation + framework (index.md for routing, synthesis docs for cross-collection knowledge)
Tier 3: collections/*/    → depth (per-collection docs with full argument detail, verses, stories)
Tier 4: source corpus     → grounding (searched for exact citations when needed)
```

Each tier adds depth without duplicating the tier above. Tier 2 references tier 3 for detail; tier 3 references tier 4 for grounding.

**How the agent should handle each status:**
- **Active**: Tier 1 (route) → Tier 2 (read topic index + relevant synthesis docs for framework) → Tier 3 (drill into collection docs for specifics) → Tier 4 (search corpus for citations before final workspace cards). Tier 2-3 can shape the answer, but user-visible workspace cards should not remain wiki-only when source access is available.
- **Seed**: Check seed docs (partial tier 2) for whatever content exists, then supplement with training knowledge. State the topic has partial coverage.
- **Planned**: Answer from training knowledge. Be transparent that curated source material doesn't exist yet for this topic.

## 4. Topic Routing

### Identifying the topic

Read the question's vocabulary and intent. Each topic has its own concept space. Use the **Routing keywords** column in the table above to match question vocabulary to topic. Use the topic's `index.md` (if it exists) for concept-level routing within the topic.

Seven topics are Active (have a topic index + dedicated source collection(s) processed at depth):
- **madhyamaka** — 空性, 中观, 二谛, 龙树, 应成/自续, etc.
- **foundations** — 前行, 加行, 暇满, 无常, 皈依, 菩提心, 六度, 金刚萨埵, 上师瑜伽, 往生法, etc.
- **abhidharma** — 俱舍, 蕴界处, 六因五果四缘, 心所法, 随眠, 圣道, 五道四果, 四禅八定, etc.
- **tathagatagarbha** — 如来藏, 佛性, 宝性论, 九喻, 三身, 他空, 不空如来藏, etc.
- **yogachara** — 唯识, 瑜伽行, 阿赖耶识, 三自性, 八识转四智, 三身四智, 弥勒五论, 大乘经庄严论, 种姓品, etc.
- **prajnaparamita** — 维摩诘经, 不二法门, 心净国土净, 烦恼即菩提, 尽无尽解脱, etc.
- **pure-land** — 极乐世界, 阿弥陀佛, 往生四因, 七支供, 明观福田, 积资净障, 发清净愿, 疑障五百岁, 临终接引, etc.

Three topics are Seed (have a topic index aggregating cross-collection content, but no dedicated root text yet):
- **pramana** — `topics/pramana/index.md` (4 source collections cross-ref)
- **tantra** — `topics/tantra/index.md` (3 source collections cross-ref)
- **vinaya** — `topics/vinaya/index.md` (3 source collections cross-ref)

For Seed topics, the index doc is the entry point and contains the substantive aggregated material; drill into the cross-referenced collections for full depth.

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

For every non-trivial Buddhist knowledge question, follow this flow:

1. **Locate the right reference file** -- use the topic's concept router for
   known concepts, or call `search_skill_refs` only when you need on-demand
   discovery. This returns routing snippets and `read_ref.path` values into the
   wiki.
2. **Read the reference file** with the normal `read` tool. These files give
   the intellectual framework, not final evidence.
3. **Write a quick scaffold** from the wiki framework when useful. Mark where
   citations are needed.
4. **Do targeted corpus search** with evidence tools (`search_hybrid`,
   `search_local`, `search_fashi`, `search_corpus_keyword`, `fetch_corpus`,
   `fetch_fashi`, or canonical tools as appropriate) for `ref:` citations
   grounding specific claims.
5. **Edit the answer** to add citations and evidence.

The wiki gives you enough to write a good initial answer immediately. Don't wait for corpus search to start writing.
But if you wrote a workspace card from the wiki, continue to the grounding step before final chat. A final Buddhist study card with zero `ref:` citations is not acceptable when source access is available; either keep it explicitly provisional with citation gaps, or edit it into a cited card.

**Fallback:** If `search_skill_refs` is unavailable, fall back to the topic's
Concept Router + Grep. If corpus search is also unavailable, answer from the
wiki alone but tell the user you could not verify against the original source.

### Search tool selection

| Question character | Recommended search | Why |
|---|---|---|
| Uses Buddhist concepts ("空性和无我有什么关系?") | Topic router or `search_skill_refs` on demand | Wiki is organized by concepts -- semantic search finds the right doc when the router is not obvious |
| Experiential / personal ("我打坐时感到很焦虑") | Source corpus (`search_hybrid`/`search_fashi`) | Wiki is technical; source teachings address lived experience |
| Generic / ambiguous ("佛教怎么看待痛苦?") | Source corpus plus topic router when framework matters | Source search discovers relevant angles; the wiki helps organize them |
| Clear concept, clear topic ("应成派的无承认是什么意思?") | Concept Router (no search needed) | Concept maps directly to a known doc |

### Source access paths

1. **Reference routing**: read known files directly, or use
   `search_skill_refs` on demand to discover the file to read.
2. **Evidence search**: use `search_hybrid` by default, or source-specific
   `search_local` / `search_fashi` when filters matter.
3. **Original text fetch**: use `fetch_corpus` for local markdown documents and
   `fetch_fashi` for fashi segments.
4. **Wiki-only** -- if corpus/canonical source access is unavailable, answer
   from compiled wiki but explicitly tell the user you could not verify against
   the original source. Still name the main relevant texts or collection docs.

### Reading search results

Search results from extraction data expose runtime `chunk_type` values. When a
tool offers a `chunk_types` filter, use only these exact values:
- `qa`: pre-answered questions -- most directly useful
- `key_term`: definitions with context -- good for conceptual questions
- `misconception`: common wrong views with corrections -- high value for debate questions
- `verse`: root text verses -- useful when source wording matters
- `lesson`: practice or study guidance distilled from a teaching
- `summary`: document-level summaries
- `koan`: short illustrative teaching stories

Do not pass extraction field names such as `qa_pairs`, `key_terms`, or workspace
card categories such as `passage` as `chunk_types`.

### Deepening

When initial search results are thin:
1. Rephrase with synonyms (e.g., 空性/无自性/离戏/无生)
2. Search for the specific treatise name + topic
3. Fall back to keyword search for exact phrases
4. Fetch full document text around matched passages

## 6. Question Analysis Scaffold

Run this before reading any topic doc. The scaffold produces an answer skeleton so the Read step is targeted, not exploratory. This is a **framework, not a checklist** — let the gating table set depth, run dimensions mentally, and produce no visible output except the final answer.

### Gating: how deep to run

| Question character | Dimensions to run |
|---|---|
| Not Buddhism | None — skill frontmatter trigger handles this |
| Factual lookup ("中论有多少品?") | ① + ⑥ |
| Single-concept definition ("什么是二谛?") | ① + ⑤ + ⑥ |
| Doctrinal / philosophical (default for most) | ①–⑥ (⑦ when drift risk is real) |
| Life-situational ("亲人离世怎么办 / 生重病时如何修 / 内心很焦虑") | ① ② ③ ④ ⑤ + light ⑥ |
| Beginner orientation ("想开始学佛从哪里入手") | ① ② ③ ⑤ ⑥ ⑦ |
| Ethical-behavioral ("仅有杀意是否染罪 / 破密乘誓言如何忏悔") | ① ② ④ ⑤ ⑥ |
| Practice / experiential / comparative / cross-topic | All 7 — Context and Underlying need are load-bearing |
| Logistical ("哪里可以闻法 / 如何找到合格上师") | ① + ⑥ |

### Understand (aspects the answer should address)

| # | Dimension | What to ask |
|---|---|---|
| ① | **Surface** | What is literally asked? |
| ② | **Register** | What kind of question? doctrinal / practical / life-situational / orientation / ethical-behavioral / stage-self-assessment / karma-inquiry / subtle-realm / logistical / mixed |
| ③ | **Context** | User's relationship to the question -- 闻/思/修/证 stage (doctrinal); life situation (situational); beginner / returning / seasoned (orientation) |
| ④ | **Underlying need** | What would actually help -- concept · method · decision · reassurance · framework · correction · recalibration |

### Plan (references to pull)

| # | Step | Purpose |
|---|---|---|
| ⑤ | **Aspects to cover** | Short list derived from ①–④. This is the answer skeleton — what the answer should include, in what order. |
| ⑥ | **Topic routing** | Which topic(s) + which specific subtopic docs. Use topic-index concept routers. |
| ⑦ | **Out of scope** | What nearby concerns to deliberately exclude so the answer stays focused. Most load-bearing for life-situational and beginner-orientation questions. |

### Pattern library lookup

After running ①–④, scan `references/methodology/question-patterns.md` for a matching question shape. A match gives aspect + routing hints and `Don'ts`; absence doesn't block answering — the scaffold alone is sufficient. Patterns cluster into doctrinal (recurring misinterpretations, debates, cross-topic tangles) and practical (life-situational, stage-assessment, karma-inquiry, subtle-realm, beginner).

### What the scaffold is not

- Not a visible analysis layer. The agent doesn't write a "how I'm reading this question" paragraph in the response — the scaffold runs silently.
- Not a tradition check. Nyingma is the default (established in this skill's preamble); the scaffold does not re-derive tradition framing per question. Topic correctness anchors catch the edges that matter.

## 7. Source Priority

| Source | What it provides | Priority |
|---|---|---|
| **Topic reference docs** | Intellectual framework, correctness anchors, concept maps | Read first, but do not cite as final evidence |
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
- `references/methodology/` -- question-analysis patterns (`question-patterns.md`) consulted from §6
- `references/public-api.md` -- REST API for corpus search when MCP unavailable
