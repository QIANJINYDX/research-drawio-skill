# research-drawio-skill

**语言：** [English](README.md) | 中文

`research-drawio-skill` 是一个面向 Codex 的 skill，用于在 diagrams.net /
draw.io 中创建论文发表风格的科研流程图和机制示意图。

它适合科研论文中的方法流程、实验设计、队列/样本流程、机制图、
多组学/数据整合流程、模型结构图和图形摘要。它的设计哲学借鉴
`nature-figure`：先定义科学信息和证据逻辑，再设计拓扑结构、布局和连接线，
最后进行克制的期刊风格润色与导出 QA。

当前版本特别强调版式工程和图形构建：网格对齐、公式保护区、连接线通道、
由 draw.io 原生图元组成的语义复合元素，以及一个轻量级 `.drawio` QA 脚本，
用于在导出前捕捉常见源文件问题。

最近的规则还专门防止三类常见问题：文字遮挡图形元素、没有科学含义的装饰性图表、
以及连接线出现不必要的多次折弯。

## 能做什么

- 创建可编辑的 `.drawio` 科研流程图
- 绘制 Nature 风格的方法流程图和实验设计图
- 绘制计算管线和模型结构示意图
- 绘制包含纳入/排除逻辑的队列或研究流程图
- 绘制论文机制图和图形摘要
- 生成适合 SVG/PDF 导出的论文图，并提供 QA 检查规则

## 仓库结构

```text
.
|-- README.md
|-- README.zh-CN.md
|-- .gitignore
|-- example/
|   `-- attention-mechanism-nature.drawio
`-- skills/
    `-- research-drawio-skill/
        |-- SKILL.md
        |-- manifest.yaml
        |-- agents/
        |   `-- openai.yaml
        |-- scripts/
        |   `-- qa_drawio.py
        |-- static/
        |   `-- core/
        |       |-- contract.md
        |       `-- stance.md
        `-- references/
            |-- archetypes.md
            |-- composite-elements.md
            |-- drawio-authoring.md
            |-- layout-and-routing.md
            |-- math-typesetting.md
            |-- qa-contract.md
            `-- style-guide.md
```

真正的 skill 位于 `skills/research-drawio-skill/`。根目录 README 只用于
GitHub 展示和安装说明。

## 示例

`example/attention-mechanism-nature.drawio` 是一个由本 skill 创建的可编辑
Nature 风格注意力机制示意图。它展示了输入 token embedding 如何投影为
query、key 和 value，scaled dot-product score 如何归一化为 attention weights，
以及 value vector 如何被加权聚合为上下文化 token 表征。

这个示例也可作为 QA 目标使用：新版 skill 会更严格检查对齐、连接线遮挡、
公式渲染、文字与图元重叠，以及连接线是否过度折弯。

## 安装

将 skill 文件夹复制到你的 Codex skills 目录：

```powershell
Copy-Item -Recurse -Force `
  "skills\research-drawio-skill" `
  "$env:USERPROFILE\.codex\skills\research-drawio-skill"
```

macOS 或 Linux：

```bash
mkdir -p ~/.codex/skills
cp -R skills/research-drawio-skill ~/.codex/skills/research-drawio-skill
```

然后在 Codex 中调用：

```text
Use $research-drawio-skill to create an editable paper-style draw.io workflow diagram.
```

## 设计哲学

这个 skill 将科研流程图视为一种“视觉论证”，而不是装饰性流程图。

每张图都从以下内容开始：

1. 一句话科学信息。
2. 图的角色，例如方法概览、实验流程、队列流程、机制示意图、分析管线、
   模型结构或图形摘要。
3. 节点、模块、分支、循环、输入和输出的拓扑图。
4. 网格布局计划，包括行、列、间距和连接线通道。
5. 复合元素计划，决定哪些科学实体应该画成组合图元，而不是纯文字框。
6. 公式和符号的 math-label contract，用于 draw.io 数学排版。
7. 颜色、形状、标签和箭头所表达的科学语义。
8. 面向期刊导出的格式和审稿风险检查。

## Skill 内容

- `SKILL.md`：主要触发元数据和路由流程。
- `manifest.yaml`：声明始终加载的核心文件和按需加载的参考文件。
- `static/core/contract.md`：作图前必须建立的流程图契约。
- `static/core/stance.md`：默认科研图形姿态和隐私规则。
- `references/archetypes.md`：科研流程图类型和反模式。
- `references/composite-elements.md`：可编辑复合图元规则，例如 mini bar chart、
  DNA/RNA 链、矩阵、神经网络、细胞、样本等，并禁止装饰性图表和文字遮挡。
- `references/layout-and-routing.md`：网格对齐、连接线通道、标签、避让和最小折弯规则。
- `references/math-typesetting.md`：MathJax / draw.io 公式处理。
- `references/style-guide.md`：字体、颜色、形状、连接线和 draw.io 样式预设。
- `references/drawio-authoring.md`：`.drawio` / mxGraph XML 编写规则。
- `references/qa-contract.md`：逻辑、视觉、源文件和导出 QA 检查。
- `scripts/qa_drawio.py`：轻量级 QA 脚本，检查 XML、数学公式、对齐、端点、
  文字/图元重叠、图表语义、折线数量和连接线遮挡。

## 示例 Prompt

```text
Use $research-drawio-skill to draw a Nature-style method workflow for my single-cell analysis pipeline.
```

```text
Use $research-drawio-skill to convert this manuscript methods paragraph into an editable draw.io experimental workflow.
```

```text
Use $research-drawio-skill to audit and polish this .drawio mechanism schematic for a paper figure.
```

## 校验

如果你安装了 Codex `skill-creator` 的校验脚本，可以运行：

```powershell
$env:PYTHONUTF8 = "1"
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" `
  "skills\research-drawio-skill"
```

期望输出：

```text
Skill is valid!
```

Windows 下建议设置 `PYTHONUTF8=1`，因为 skill 元数据中包含中文触发词。

检查生成的 `.drawio` 文件：

```powershell
python "skills\research-drawio-skill\scripts\qa_drawio.py" "example\attention-mechanism-nature.drawio"
```

在将图作为 polished example 或论文导出文件前，应检查并处理所有 warning。
