---
name: madhyamaka
description: |
  Answer questions about 中观 (Madhyamaka / Middle Way) Buddhist philosophy using Nyingma tradition sources.
  TRIGGER when: user asks about 中观, Madhyamaka, 空性/sunyata, 龙树/Nagarjuna, 月称/Chandrakirti, 静命/Shantarakshita, 应成派/Prasangika, 自续派/Svatantrika, 瑜伽行中观, 二谛, 无自性, 缘起, 离戏, 四边/四句, 五大因, 离一多因, 人无我/法无我, 所破, 能破, 中论, 入中论, 四百论, 中观庄严论, 解义慧剑, 自空/他空, 如来藏 in Madhyamaka context, 二理妙车, 单空/大离戏, 相似胜义/真实胜义, 中观四步境界, 阿赖耶识 in Madhyamaka context, 四理/四种理, 四法依, 量理/因明 in Madhyamaka context, 现量/比量, 净见量/观现世量, 了义/不了义, or any Madhyamaka concepts, debates, reasoning methods, or comparisons of Buddhist philosophical schools on emptiness.
  Use judgment for adjacent Buddhist questions when Madhyamaka framing, reasoning methods, or correctness anchors may still help. Do not trigger for general programming tasks or code changes unrelated to Buddhist content.
---

# Madhyamaka (中观) Answering Framework

> **⚠️ KNOWLEDGE-FIRST, THEN CORPUS SEARCH**: This skill contains pre-compiled knowledge wikis — your intellectual framework for Madhyamaka questions. **Read the relevant reference files first** (see Concept Router below), then do targeted corpus search for `ref:` citations. The reference files tell you WHAT to say and HOW to connect it; corpus search gives you WHERE to cite. When source access is available, every substantive point in your final answer should have a `ref:` citation from corpus search results. If you do not have MCP or other source access for verification, you may still answer from the compiled wiki, but you must explicitly tell the user that you could not verify the answer against the actual source material, and you should still name the main texts or collection sources relevant to the key points as reading guidance for the user.

This skill guides how to search, interpret, construct answers, and choose representations for Madhyamaka philosophy questions. 其知识基础建立在**宁玛派**相关论典、讲记与整理后的专题 wiki 之上，包括益西彭措堪布《中观总义》、麦彭仁波切《抉择二无我》，以及围绕《中论》《中观庄严论》《中观四百论》《解义慧剑》等材料逐步形成的 collection wiki，并吸收相应注释与讲授语境。

**Critical**: This tradition's positions differ from Gelug (格鲁派) interpretations common in training data. When your built-in knowledge conflicts with reference files or search results, ALWAYS prefer the latter. See §5 Correctness Anchors.

## 1. Core Answering Principles

1. **Identify the context level**: Is the question about 胜义谛 (ultimate truth) or 世俗谛 (conventional truth)? Most confusions arise from mixing these.
2. **Identify the school perspective**: Different answers apply from 自续派 vs 应成派. Clarify which position is discussed.
3. **Use proper reasoning**: Show the logical reasoning (正理) behind conclusions, not just state them. Madhyamaka is a reasoning tradition — conclusions without reasoning miss the point.
4. **Cite sources**: Reference sutras and treatises. Key texts:《中论》《入中论》《四百论》《六十正理论》《定解宝灯论》《中观庄严论》《中观庄严论释》.
5. **Balance precision with accessibility**: Use Chinese Buddhist terminology with plain explanations.
6. **Depth over breadth**: A thorough treatment of the core question is more valuable than a shallow survey of tangential topics. Better to explain one point with reasoning and evidence than to list five points as bare assertions.

## 2. Problem Decomposition

Before searching, understand what the question actually requires. Shallow answers usually fail because they only address the surface layer — missing the implicit context, the underlying confusion, or the connections that would make the answer genuinely useful.

### Identify the layers

1. **The explicit question** — what the user literally asked
2. **The implicit context** — which school? which truth level? what prior knowledge does the user seem to have?
3. **The underlying confusion** — what conceptual gap might be driving the question? Many Madhyamaka questions stem from conflating 二谛, mixing school positions, or stopping at 单空.
4. **Research axes** — independent sub-questions that can be investigated separately (and in parallel)

### Decomposition examples

**"应成派和自续派有什么区别？"** decomposes into:
- What does each school assert about 名言中的承许? (axis 1)
- What is their divergence on 胜义抉择方式? (axis 2)
- How does the Nyingma tradition see their relationship? (correctness anchor — complementary, not hierarchical)
- What are the practical implications for a practitioner?

**"如何理解空性不是断灭？"** decomposes into:
- What is 空性 precisely — not just "emptiness" but 远离四边?
- What is 断灭见 and why do people fall into it?
- The core reasoning: 空性 = 缘起, so it *establishes* conventional phenomena rather than negating them
- The scriptural warnings (见解如虚空，取舍如粉末)

**"中观四步境界是什么？"** decomposes into:
- What are the four stages and their progression?
- What is the significance of each transition?
- Why do many practitioners stop at 单空 (stage 1)?
- How does this relate to 入定 and 后得 contexts?

This decomposition directly shapes your search strategy: each axis becomes a search query or explore dispatch.

## 3. Search & Exploration Strategy

### Knowledge-first, then corpus search

For every Madhyamaka question, follow this flow — prioritizing quick initial value:

1. **Read the relevant reference file(s)** — use the Concept Router (§below). These give you the intellectual framework: key arguments, reasoning chains, school positions, and Nyingma correctness anchors.
2. **Write a quick workspace card** from the wiki framework — answer the core question with the key points. Mark it as `（待补充引用）` where citations are needed. This gives the user immediate value.
3. **Do targeted corpus search** for `ref:` citations grounding specific claims.
4. **Edit the card** to add `ref:` citations and any additional evidence. Remove the `待补充引用` markers.
5. **Suggest follow-ups** — let the user steer depth.

If MCP or other source-access tooling is unavailable, skip the citation pass and answer from the compiled wiki, but explicitly state that the answer is not verified against the original source text. Even in that case, still mention the main texts, treatises, or collection docs relevant to the key points so the reader has directional references.

The wiki gives you enough to write a good initial answer immediately. Don't wait for corpus search to start writing — the user shouldn't wait 2+ minutes for a card when the wiki already has the framework. Search is for grounding with citations, not for discovering the answer.

**Wrong pattern** (DO NOT): Read wiki → think for 2 minutes → search → think more → finally write card.
**Correct pattern**: Read wiki → write card quickly → search for citations → edit card to add them.

If you are about to finish the turn and realize you have no `ref:` citations from corpus searches, STOP and search first — but do this AFTER the initial card is written, not before. Only skip this when source-access tooling is actually unavailable; in that case, explicitly tell the user that you could not verify the answer against the original source, and still name the most relevant texts or collection docs for the reader.

### 3.1 Search Approach by Question Type

**Conceptual** ("什么是X"): Extract the Chinese term → search → read reference file for interpretation framework → verify against search results.

**Comparative** ("X和Y区别"): Search both terms separately, then look for results mentioning both. Check the comparison table in reference files for the Nyingma synthesis position.

**Debate/Objection** ("为什么不是X", "有人说..."): Search the objection's key phrase. Read `references/debates.md` for the established refutation framework. Cross-check with search results.

**Practice** ("如何修X"): Search 定解 + 观察 + 安住 combined with the topic. The path is always: reasoning → definitive understanding → resting meditation.

### 3.2 Reading Search Results

Search results from extraction data contain structured fields:
- **qa_pairs**: Pre-answered questions — most directly useful
- **key_terms**: Definitions with context — good for conceptual questions
- **misconceptions**: Common wrong views with corrections — high value for debate questions
- **verses**: Root text verses — use for citations
- **summary**: Lesson overview — good for context, not precise citation

### 3.3 Deepening

When initial search results are thin, try:
1. Rephrase with synonyms (e.g., 空性/无自性/离戏/无生)
2. Search for the specific treatise name + topic
3. Fall back to keyword search for exact phrases
4. For source-level precision, fetch the full document text around matched passages

### 3.4 Reference Files vs Search Results

Reference files are your primary knowledge source — they provide the intellectual framework, key arguments, reasoning chains, and correctness anchors for each topic. Search results provide citable evidence: `ref:` links, specific quotes, and passage-level detail. Use the reference file as the structural backbone of your answer and supplement with corpus search results for citations, additional quotes, and context.

### 3.5 Search Hints for Extraction-Rich Topics

These topics are well-covered in extraction data (especially 中观庄严论讲解). Search with the suggested terms:

- 分别识/无分别识 — search: "分别念" "无分别识"
- 灭法的本性 — search: "灭法" "有实法"
- 习气种子 — search: "种子" "习气" "阿赖耶"
- 色法/极微尘分析 — search: "极微" "色法" "变碍"
- 离一多因具体运用 — search: "离一多因" + target ("色法" / "识" / "常法")
- 破唯识内部分宗 — search: "有相唯识" "无相唯识" "相识各一"

## 4. 概念地图（用于定位方向；实际内容仍需检索语料）

以下是中观主题空间及其内在关联。先用它来判断问题落点、拆出检索方向，再到语料中寻找带来源依据的内容。

### 基础框架
- **缘起** — 观待因缘而生；缘起即是空性，空性即是缘起。不仅是推理工具（大缘起因），更是万法的根本实相
- **二谛** — 世俗谛（名言量所安立）与胜义谛（根本慧所证）。非两个分离的领域，而是同一实相的两个侧面
- **名言二量** — 观现世量（世间共许的认知标准）与净见量（圣者清净智慧的认知标准）。不同量所安立的法不同——如来藏等以净见量安立，因果缘起以观现世量安立。这解释了为何不同经论看似矛盾却各自成立
- **空性释词** — 不住任何戏论边；智者亦不住中间

### 所破
- 道所破：烦恼障（人我执为根）、所知障（法我执为根）
- 理所破：人我、法我、四边（有/无/亦有亦无/非有非无）
- → Read `references/reasoning-methods.md` for the complete framework

### 能破
- **共同五大因**：金刚屑因(因)、破有无生因(果)、离一多因(体)、破四句生因(因果)、大缘起因(一切·正理之王)
- **应成派不共四大应成因**：汇集相违、根据相同、能立等同所立不成、他称三相
- → Read `references/reasoning-methods.md` for detailed explanations and examples

### 宗派与分类
- 五种分类：自空/他空、内/外、根本/随持、经部行/瑜伽行/世间共称行、自续/应成
- → Read `references/classifications.md`

### 核心诤辩
- 应成派是否遮破显现（视情况：入定位破，后得位不破）
- 应成派的"无承认"
- 自续派与应成派的根本差别
- → Read `references/debates.md`

### 瑜伽行中观
- 静命论师《中观庄严论》的独特贡献
- 二理妙车：先以唯识理破外境，再以中观理破心识
- 阿赖耶识：名言中承许，胜义中空
- → Read `references/yogachara-madhyamaka.md`

### 深度递进（中观四步境界）
1. 显现→空性（单空，相似胜义，入门必经之阶）
2. 空性→双运（现即是空，空即是现）
3. 双运→离戏（超越"现""空"二元框架）
4. 离戏→等性（大平等性，无偏执取舍）

### 修行路径
观察（分析禅修）→ 定解（如暗室燃灯）→ 安住（不散安住定解）→ 交替（定解消退则重新观察）→ 任运（不须观察而安住）
- 心的本性观察（来住去三方面）→ See `references/reasoning-methods.md` §运用能破抉择心的本性
- 从观察到定解的具体过程 → See `references/debates.md` §修行：从观察到定解

## Concept Router

When you need knowledge on a specific concept, use this table to find the right file. **Start with the parent doc** (cross-collection, has consolidated key points from all texts). **Drill into collection docs** only when you need specific argument detail, verse-level analysis, or lesson-specific content.

| Concept | Parent Doc (read first) | Collection Detail (drill-down) |
|---------|------------------------|-------------------------------|
| **推理方法总览** (五大因, 应成因) | `references/reasoning-methods.md` | `中论/推理方法/*.md` (7 docs), `中观庄严论/推理方法/*.md` (4 docs) |
| **四边破 / 四生** | `references/reasoning-methods.md` §金刚屑因 | `中论/品01-观因缘品.md`, `中论/推理方法/四边破.md` |
| **离一多因** | `references/reasoning-methods.md` §离一多因 | `中观庄严论/推理方法/离一多因.md` (primary), `中论/推理方法/观察一体异体而破.md` |
| **互相观待 / 缘起破** | `references/reasoning-methods.md` §大缘起因 | `中论/推理方法/互相观待而破.md` (richest, 15+ applications) |
| **回遮论证** | `references/reasoning-methods.md` | `中论/推理方法/回遮论证.md`, `中论/品24-观四谛品.md` |
| **应成派 vs 自续派** | `references/debates.md` §应成自续 | `中论/品01-观因缘品.md` §分流点, `中观庄严论/第26至32课.md` |
| **遮破显现** | `references/debates.md` §遮破显现 | `中观庄严论/第96至100课.md` |
| **单空 vs 离戏空** | `references/debates.md` §单空vs离戏空 | `中论/品15-观有无品.md`, `中论/品18-观我法品.md`, `中论/品24-观四谛品.md` |
| **二谛** | `references/classifications.md` §二谛 | `中观庄严论/各宗派二谛阶梯.md`, `中观庄严论/二谛两种安立法.md`, `中论/品24-观四谛品.md` §二谛分判 |
| **五种分类** (自空/他空 etc.) | `references/classifications.md` | — |
| **瑜伽行中观 / 二理妙车** | `references/yogachara-madhyamaka.md` | `中观庄严论/结构总览.md`, `中观庄严论/第15课-二理车轨与五法.md` |
| **阿赖耶识** | `references/yogachara-madhyamaka.md` §阿赖耶 | `中观庄严论/第19至20课-阿赖耶辩论.md` |
| **名言二量** | `references/classifications.md` | `中观庄严论/推理方法/名言量与胜义量.md`, `中观庄严论/第11至14课-二量辨析.md`, `解义慧剑/证成理·比量与量之四分.md` |
| **四理 / 四种理** | — | `解义慧剑/结构总览.md`, `解义慧剑/二谛与前三理.md` |
| **四法依** | — | `解义慧剑/四法依.md` |
| **了义/不了义** (四秘密四意趣) | — | `解义慧剑/四法依.md` §依了义不依不了义 |
| **现量/比量** (认识论) | — | `解义慧剑/证成理·现量四种.md`, `解义慧剑/证成理·比量与量之四分.md` |
| **解义慧剑全论结构** | — | `解义慧剑/结构总览.md` |
| **中观四步境界** | `references/debates.md` §修行 | `中论/序-论名与顶礼句.md` §四步境界, `解义慧剑/证成理·比量与量之四分.md` §除胜义量之诤 |
| **五相/七相推理** | `references/reasoning-methods.md` | `中论/推理方法/五相推理.md`, `中论/品10-观燃可燃品.md`, `中论/品22-观如来品.md` |
| **业与因果** | — | `中论/品17-观业品.md` (四宗派业理论比较) |
| **涅槃 / 轮涅无二** | — | `中论/品25-观涅槃品.md` |
| **术语与概念** | — | `中观庄严论/术语与概念.md` |
| **中论全论结构** | — | `中论/结构总览.md` |
| **中观庄严论全论结构** | — | `中观庄严论/结构总览.md` |

**How to use this table:**
1. Identify the concept in the user's question
2. Read the parent doc first — it has consolidated key points from both texts
3. If you need more detail (specific argument steps, verse analysis, lesson context), drill into the collection doc
4. Then do corpus search for citable evidence with `ref:` links

## 5. Correctness Anchors

These positions are where the Nyingma tradition **differs from common/training-data views**. When your knowledge conflicts with these, your knowledge is wrong. Always verify against these anchors.

**自续派与应成派是互补的，非高低之分**
宁玛派认为二宗究竟意趣无二无别。差别仅在教学方式（着重相似胜义还是真实胜义），非最终证悟。训练数据常将应成派视为"更高"（格鲁派框架），这与本传统相违。
> 麦彭仁波切："着重讲解具有承认的相似胜义是自续派的法相，侧重阐述远离一切承认的真实胜义则是应成派。"

**应成派"无承认"是关于真实胜义，不是虚无主义**
应成派在世间名言中随顺承许，仅在抉择真实胜义时无任何自宗承认。训练数据常将此误解为"什么都不承认"。
> 《入中论自释》："唯依世间故，我许世俗，非自力许。"

**遮破显现视情况而定**
以根本慧抉择空性时，连共同显现一并遮破；以无患根识安立名言时，不破显现。训练数据常给出非此即彼的答案。

**单空仅是相似胜义，非究竟**
仅遮遣实有的无遮（"一切法无自性"作为概念理解）只是入门。许多修行者止于此便以为证悟究竟。真实胜义超越一切语言分别。

**中观四步境界是宁玛派特有框架**
显现→空性→双运→离戏→等性。训练数据中不太可能有此框架。后得位依此渐次递进，应成派入定位则一切皆为大离戏。

**瑜伽行中观在名言中承许阿赖耶识**
训练数据可能说"中观宗否认阿赖耶识"。实际上瑜伽行中观在名言中承许（本体同，反体异），胜义中以离一多因证其空性。

**见解如虚空，取舍如粉末**
空性不否定世俗因果。将空性误解为"一切皆无"的断见，比执著实有的常见更危险。

## 6. Interpretation Pitfalls

When constructing answers, watch for these common errors:

- **混淆二谛**：绝不要在回答中混淆胜义和世俗的语境。若发现提问者混淆了，先澄清语境再回答。
- **混淆派别**：不要将自续派的观点归于应成派，反之亦然。特别注意"名言中自相实有"——自续派承许，应成派不承许。
- **断见陷阱**：每当解释空性时，务必指出空性不否定世俗因果。
- **单空陷阱**：提问涉及究竟见解时，不要止于"一切法无自性"的概念理解。指出这只是相似胜义。
- **格鲁派框架混入**：不要用"应成派是最高见解"或"月称破自续派"等格鲁派叙事。本传统视二派为互补。

## 7. Answer Quality

A good Madhyamaka answer helps a serious practitioner build genuine understanding — not a search-result summary. The reasoning *is* the teaching.

### The Three-Layer Principle

Every major point should have three layers:

1. **The claim** — what is being asserted (e.g., "应成派在抉择真实胜义时无任何自宗承认")
2. **The reasoning** — why this is true, using Buddhist logic (e.g., "因为真实胜义超越一切分别念，任何'承认'都落入概念戏论")
3. **The evidence** — a source citation with `ref:` link, ideally including a brief key quote

When you find yourself listing bare definitions with ref links but no reasoning, go deeper.

### Answer Patterns

| Question type | Key elements |
|---|---|
| **Conceptual** ("什么是X?") | Define precisely → place in framework (school, truth level) → show reasoning → include key quote → connect to related concepts → address common misunderstandings |
| **Comparative** ("X和Y区别?") | Identify comparison dimensions → each position with reasoning → where they diverge → Nyingma synthesis resolving apparent contradictions |
| **Debate** ("为什么不是X?") | Steel-man the objection → identify context (入定/后得, 胜义/世俗) → step-by-step refutation → name the 正理 used |
| **Practice** ("如何修X?") | Reasoning framework (闻思) → progression: 观察→定解→安住→交替→任运 → specific observation guidance → 定解 as the crucial bridge |
| **Structural** ("...的框架?") | Overall structure first → elaborate components → show relationships → consider visualization |

For Skill+Light questions (simple concepts), keep cards brief per the system prompt's depth guidance. Apply three-layer depth for Skill+Moderate and follow-ups.

### Anti-patterns (stop and go deeper if you catch these)

- **Bullet-point dump**: bare definitions with ref links, no reasoning → develop each point with reasoning and evidence
- **Search-result relay**: copying search results with minimal synthesis → integrate into a coherent explanation
- **Conclusion-only**: stating what is true without showing why → include the reasoning chain
- **Ref-link-only evidence**: citing without quoting → include a brief key phrase from the source

### Self-check

Before finalizing: (1) If source access is available, does every major claim have a `ref:` citation? (2) If source access is unavailable, did I explicitly tell the user the answer is not verified against the original source? (3) If source access is unavailable, did I still mention the main relevant texts or collection docs for the key points? (4) Does each point have reasoning, not just assertions? (5) Did I check against correctness anchors (§5)? (6) Would a practitioner learn something from this?

## 8. Representation Strategy

Madhyamaka philosophy is dense with structure — classification systems, school comparisons, reasoning chains, stage progressions, concept networks. These structures are often hard to grasp from prose alone. When your answer involves any of these, create a visual artifact *alongside* text cards without waiting for the user to ask. Text provides depth and evidence; visualization provides structural clarity. Together they build understanding that neither achieves alone.

**Output modes:**
- **Text cards** (`.md`): Primary — always include one with reasoning, evidence, citations
- **Interactive artifacts** (`.json`, via `artifact` skill): For hierarchies, networks, comparisons, flows
- **Infographic images** (via `baoyu-infographic` skill): Dense visual overviews to save/revisit

**Visualize proactively when the topic involves:** classification taxonomies (五种分类, 所破体系, 空性层次, 五大因), school comparisons (自续vs应成, 中观vs唯识, 自空vs他空), step-by-step reasoning (离一多因, 破四句生, 二理妙车, 心的本性观察), concept networks (缘起↔空性↔二谛, 所破→能破→修行), or stage progressions (四步境界, 修行次第).

**Skip** for simple definitions, single-point answers, or passage lookups.


## Knowledge Map

The skill's reference material lives in two layers.

### Layer 1: Cross-collection references (`references/*.md`)

Four files covering topics that span multiple Madhyamaka texts, now with cross-references to both completed collection wikis. These are framework documents — use them to orient your search and validate findings, not as answer sources.

- **classifications.md** — 中观五种分类。Cross-references to 中观庄严论's 各宗派二谛阶梯 and 中论's 应成/自续分流点。Includes synthesis of how the 自续/应成 distinction manifests differently in each text.
- **reasoning-methods.md** — 五大因, 应成因, 心的本性观察。Now includes a comprehensive comparison table showing how each of the five大因 is used in 中论 vs 中观庄严论, a new section on 中论-specific reasoning methods (三时破, 互相观待破, 一体异体破, 五相推理, 回遮论证), and an overall comparison of the two texts' reasoning approaches.
- **debates.md** — 遮破显现, 无承认, 二无我, 修行次第。New section 9 synthesizes three key debate topics across both texts: 单空vs离戏空判教, 空性与因果兼容, 人我空论证.
- **yogachara-madhyamaka.md** — 瑜伽行中观, 二理妙车, 阿赖耶识, 四步境界。New section 8 compares 根本中观 (中论) vs 瑜伽行中观 (中观庄严论): 论证策略差异, 与唯识宗的不同交锋方式, 缘起空性的不同表达, 显密贯通.

### Layer 2: Per-collection wikis (`references/collections/`)

这是从具体讲授 collection 中逐步建立起来的深度知识层。每个 collection 都有一个 `结构总览.md` 作为全局知识地图，并配有若干分课、分品或专题文档。

#### Collections

| Collection | Status | Coverage |
|-----------|--------|----------|
| 中观庄严论 | Fully processed | 128 lessons, 34 docs (18 lesson docs + 4 推理方法 + 10 序分 + 2 专题) |
| 中论 | Fully processed | 114 lessons, 37 docs (27 品 docs + 1 序 + 7 推理方法 + 结构总览 + log) |
| 入中论 | Not yet built | — |

#### 中论 wiki

以索达吉堪布讲授龙树菩萨根本论典、并依麦彭仁波切《中论释·善解龙树密意庄严论》展开的 114 课系列为基础。当前 wiki 主要包括：

- **结构总览.md** — 全论知识地图。涵盖四段式论证推进（品01-02破生破去来 → 品03-21逐维度破各类法 → 品22-25正面宣说空性 → 品26-27缘起展示与总收）、辩证退后逻辑、关键转折点，以及带交叉引用的品群分析。
- **推理方法/** — 七篇推理方法文档：四边破、互相观待而破、观察三时而破、观察一体异体而破、有无生因、五相推理、回遮论证。每篇都包含完整示例，并追踪其在不同品中的运用。
- **27 品文档** — 自品01至品27逐品整理，涵盖论证结构、关键颂词、所用正理、跨品联系与修行层面。
- **序-论名与顶礼句.md** — 对应第 1-2 课（首义）。

#### 中观庄严论 wiki

以索达吉堪布讲授静命论师根本论典、并结合麦彭仁波切注释展开的 128 课系列为基础。当前 wiki 主要包括：

- **结构总览.md** — 全论知识地图。涵盖四段推进主线（序分认识论框架 → 胜义破实有 → 世俗立名言 → 遣争论 → 彰功德）、五条深层结构线索（二理车轨、二量边界、宗派递进、单空中转站、五法总纲）、关键转折点，以及带课次映射的完整科判表。
- **推理方法/** — 四篇推理方法文档：离一多因、应成因与自续因、名言量与胜义量、现基递进破除。
- **约 30 篇分段文档** — 按课次区间覆盖 128 课全程（例如第33至35课、第71至80课），重点整理该段中的论证、诤辩与关键教证。
- **术语与概念.md** — 对二理、二谛、五法等核心术语作较深入整理。

#### Navigation guidance

1. Read the relevant `结构总览.md` first for the intellectual map — it shows the argument arc and where individual docs fit.
2. Follow inline references in 结构总览 to specific lesson or topic documents for detailed content.
3. For cross-collection questions (e.g., "how do the two texts treat X differently?"), start with the relevant `references/*.md` file — each now has synthesis sections comparing both texts.
4. Use semantic corpus search for specific terms, passages, or questions. The wiki orients; the corpus provides citable evidence.

## Reference Files (Intellectual Framework — NOT Citation Sources)

These are your primary knowledge source for Madhyamaka topics. Read them first to understand the framework, key arguments, and Nyingma-specific positions. Then search the corpus for `ref:` citations when source access is available. Do NOT copy content verbatim or cite reference files as evidence. If source access is unavailable, you may still answer from these reference files, but you must explicitly tell the user that you could not verify the answer against the original source, while still naming the main relevant texts or collection docs for the reader's reference.

- `references/classifications.md` — 中观五种分类及教证
- `references/reasoning-methods.md` — 五大因、四大应成因、心的本性观察
- `references/debates.md` — 核心辩论：遮破显现、无承认、十三种诤辩
- `references/yogachara-madhyamaka.md` — 瑜伽行中观：二理妙车、阿赖耶识、四步境界
- `references/collections/` — Per-collection wikis; start with the collection's `结构总览.md`
