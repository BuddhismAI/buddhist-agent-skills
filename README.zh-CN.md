# Buddhist Agent Skills

面向中观、空性、龙树等佛教主题的 AI Skill 与知识 wiki 的开源仓库。提供公开的 MCP Server 和 REST API，支持语料搜索和全文获取，无需认证。

- English: [README.md](./README.md)

## 支持的 Agent

这个仓库是按共享的 Agent Skills 规范来组织的，所以核心 skill `skills/madhyamaka/SKILL.md` 不只是给 Codex / OpenAI 用，也可以被很多常见 coding agent 复用。

常见目标包括：

- Claude Code
- Codex
- Cursor
- OpenCode
- Gemini CLI
- Cline 以及其他由 `skills` CLI 支持的 agent

## 使用 `npx skills add` 安装

最通用的安装方式是 `npx skills add`，它会把 GitHub 上的 `madhyamaka` skill 安装到你选择的兼容 agent 中。

```bash
# 安装到当前项目
npx skills add BuddhismAI/buddhist-agent-skills --skill madhyamaka -y

# 全局安装
npx skills add BuddhismAI/buddhist-agent-skills --skill madhyamaka -g -y
```

之所以可以直接安装，是因为仓库里已经暴露了合法的 skill 路径 `skills/madhyamaka/SKILL.md`。

## Claude Code Marketplace

为了支持 Claude Code 的原生 marketplace 流程，这个仓库还提供了 [`.claude-plugin/marketplace.json`](./.claude-plugin/marketplace.json)。

```bash
claude plugin marketplace add BuddhismAI/buddhist-agent-skills
claude plugin install madhyamaka
```

## Agent 元数据分层

不同 agent 可以读取不同的可选元数据层：

- [`skills/madhyamaka/SKILL.md`](./skills/madhyamaka/SKILL.md) 是跨 agent 的核心事实来源
- [`skills/madhyamaka/agents/openai.yaml`](./skills/madhyamaka/agents/openai.yaml) 主要用于兼容 OpenAI / Codex 界面的展示
- [`.claude-plugin/marketplace.json`](./.claude-plugin/marketplace.json) 用于 Claude Code marketplace 的发现与安装

## 发布方式

对于这个仓库，默认最合适的做法是使用轻量的 Git 版本管理，而不是把版本号写进每个 skill 文件里。

推荐流程：

1. 把变更合并到 `main`。
2. 用 `npx skills add BuddhismAI/buddhist-agent-skills --list` 验证安装与发现流程正常。
3. 如果你希望保留明确的发布节点，可选地打 Git tag，例如 `v0.1.0`、`v0.2.0`、`v0.2.1`。
4. 如果用户已经安装过 skill，提示他们执行 `npx skills update`。

补充说明：

- `skills-lock.json` 属于消费方项目里的安装状态文件，不是发布方仓库里的版本元数据。
- 尽量保持 skill 的名字和路径稳定；像 `skills/madhyamaka/` 这种路径变更才算主要 breaking change。
- 只有在某个特定 marketplace 明确要求时，再补充显式的 manifest 版本字段即可。

## 仓库目标

这个仓库用于沉淀可复用的佛教主题 skill，服务于佛学学习、基于原始资料的推理，以及可持续积累的知识工作流。

我们希望把佛教领域相关的 skill 放在一个统一、清晰、可复用的位置，方便不同应用和 agent 运行时共享：

- 行为与路由规则
- 主题级知识 wiki
- 正确性锚点与关键判准
- 按论典或课程组织的知识文档

更重要的是，我们建立这个仓库，是希望让真实、可靠、可追溯的佛法内容，能够通过各种 AI agent 与应用，被更多人实际用起来。

我们的目标不是只服务某一个产品，而是让任何开发者都可以把这些 skill 集成到自己的应用中，为用户提供更加：

- 契合原始教法与传承语境的内容
- 比模型裸记忆更准确的回答
- 有依据、可追溯的佛法知识
- 能跨 agent 框架与产品形态复用的能力

我们希望佛法内容不只停留在某一个应用里，而是能以谨慎、尊重传统、重视出处的方式，被更多 agent 和应用采用。

## 检索关键词

为了让这个仓库更容易被搜索到，README 会明确覆盖常见的中英文查询词，例如：

- Buddhist AI skill
- Madhyamaka AI
- 中观 AI skill
- 空性解释
- 龙树学习助手
- 月称 / 静命 / 麦彭 相关中观资料
- 宁玛派中观
- 应成派与自续派
- 佛教 agent knowledge wiki
- `npx skills add` 佛教 skill

## 为什么单独做一个仓库

这个仓库被有意从单一应用中抽离出来。

这样做有几个明显的好处：

- 同一套佛教 skill 可以复用于多个应用
- 教义知识层可以独立于产品代码持续演进
- 更适合开源，也更方便外部协作
- 让 topic skill 成为稳定的共享基础设施，而不是某个应用私有的 prompt 文件

## Skill 与原文检索服务的配合

这个仓库的设计，需要与一个公开的原文检索服务配合使用——用于搜索和获取佛教教言原文，无需认证。推荐通过 MCP 连接以获得最佳体验。如果你的 Agent 不支持 MCP，Skill 会自动引导它调用 REST API 作为替代——不需要额外配置。

### MCP Server（面向 AI Agent）

连接远程 MCP 服务器 `https://api.shuiyue.ai/mcp`，通过工具调用访问：

| 工具 | 说明 |
|------|------|
| `search_hybrid` | 搜索自有语料库 + fashi.ai，跨源重排序 |
| `fetch_local` | 按 source_path 获取自有语料库全文 |
| `fetch_fashi` | 按 segment_id 获取 fashi.ai 文档 |

```bash
# Claude Code
claude mcp add --transport http buddhist-texts https://api.shuiyue.ai/mcp
```

### REST API（面向任意客户端）

如果你的环境不支持 MCP，可以直接调用 JSON 接口：

| 端点 | 方法 | 说明 |
|------|------|------|
| `/api/v1/search` | POST | 搜索佛教教言语料 |
| `/api/v1/local/{source_path}` | GET | 获取自有语料库全文 |
| `/api/v1/fashi/{segment_id}` | GET | 获取 fashi.ai 文档 |

**Base URL:** `https://api.shuiyue.ai`

无需认证。完整接口文档见 [`skills/madhyamaka/references/public-api.md`](./skills/madhyamaka/references/public-api.md)。

### 两者如何配合

两者的分工：

- 本仓库提供 skill 行为、主题地图、正确性锚点，以及整理后的知识索引
- 原文检索服务负责面向原始文献与相关语料的直接检索

换句话说：

- skill 帮助 agent 理解”这是什么、应该怎么把握”
- 检索服务帮助 agent 找到”原文在哪里、依据是什么”
- 两者配合，才能让佛法问答更完整，也更忠实于原始内容

## 当前范围

目前首先从以下主题开始：

- `skills/madhyamaka/` - 中观 skill 与主题 wiki

后续可能扩展到：

- `skills/yogachara/`
- `skills/pramana/`
- `skills/lamrim/`
- `skills/buddhism/` - 跨主题的轻量总览 / 路由 skill

## 仓库结构

每个 topic skill 都是对应主题的规范知识主页，通常包含：

- `SKILL.md` - 行为、路由与回答策略
- `agents/*.yaml` - 面向不同 agent UI 的可选元数据
- `references/` - 编译后的知识 wiki

在仓库根目录，还可以加入像 `.claude-plugin/marketplace.json` 这样的可选打包文件，把同一套 skill 暴露给 agent 原生 marketplace。

这些内容里通常还会包含索引与结构化参考材料；当它们与原文检索工具配合使用时，价值会发挥得更完整。

在单个 topic skill 内部：

- `references/*.md` 用于跨 collection 的综合文档
- `references/collections/*` 用于单个 collection 的 wiki

## 这些 Skill 是如何生成的

这些 skill 并不是简单地给通用模型套上一层 prompt。

从高层看，它们是通过一种“以源材料为中心”的综合过程逐步构建出来的：

- 从真实的讲记、论典注释和相关原始材料出发
- 以顺序方式处理一个 collection，而不是把每一课、每一段都当作互不相关的碎片
- 在处理过程中逐步发现、校正并完善整套材料本身的结构
- 先产出 collection 层面的知识文档，梳理论证脉络、核心概念、术语、引文和修行层面的意义
- 再在多个 collection 之上做 topic 层的综合，形成方法、辩点、分类与正确性锚点等主题文档

最终形成的是一个分层知识体系：

- 原始材料始终是最终依据
- collection 层文档负责保留深度与出处脉络
- topic 层文档负责提供 agent 在回答时可用的概念地图

这也是这个仓库对 agent 特别有价值的原因之一：它提供的不是零散的检索结果，而是经过组织、整理与沉淀的理解框架。

## 开发模式

本仓库可以通过符号链接的方式，被其他项目直接引用。

例如某个项目可以把以下路径：

- `.claude/skills/<skill>`
- `.agents/skills/<skill>`
- `backend/sandbox/.claude/skills/<skill>`

链接到本仓库中的规范目录。

通过符号链接编辑时，本质上修改的仍然是真实文件，因此变更会直接反映到本仓库。

## 协作约定

- 把这个仓库视为抽离出来的佛教 skill 的 source of truth
- 如果消费项目通过 symlink 引用了某个 skill，那么从那个路径编辑，本质上仍是在修改本仓库
- 只要任务实质性修改了这些 skill 内容，就应该在本仓库中提交相应 commit

## 反馈与问题

如果你发现内容有问题、解释不够清楚、引用有误，或者教义表述上需要修正，欢迎直接提 issue。

也非常欢迎各种建议，例如：

- 事实性勘误
- 更好的结构或术语组织
- 缺失的原文覆盖
- 更清晰的 agent 行为设计
- 新的 topic skill 或原文检索工具方向

更多 agent 协作说明见 [CLAUDE.md](./CLAUDE.md)。
