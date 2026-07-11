# research-drawio-skill

<p align="center">
  <img src="assets/research-logo.png" alt="research-drawio-skill Logo" width="220">
</p>

> 中文说明已设为仓库默认首页：[打开默认中文 README](README.md)。

**语言：** 中文 | [English](README.en.md)

`research-drawio-skill` 是一个面向 Codex 的 skill 套件，用于在 diagrams.net /
draw.io 中创建论文发表风格的科研流程图和机制示意图。

推荐的两阶段入口是 `research-draw`：它先创建或使用一张高质量科研插图参考图，
再调用 `research-drawio-skill` 将参考图临摹为可编辑的 `.drawio` 文件。当你已经
明确图的结构，或只需要直接创建、修改、审核、导出、QA draw.io 源文件时，可以
直接使用 `research-drawio-skill`。

它适合科研论文中的方法流程、实验设计、队列/样本流程、机制图、
多组学/数据整合流程、模型结构图和图形摘要。它的设计哲学借鉴
`nature-figure`：先定义科学信息和证据逻辑，再设计拓扑结构、布局和连接线，
最后进行克制的期刊风格润色与导出 QA。

当前版本特别强调版式工程和图形构建：网格对齐、公式保护区、连接线通道、
由 draw.io 原生图元组成的语义复合元素，以及一个轻量级 `.drawio` QA 脚本，
用于在导出前捕捉常见源文件问题。

最近的规则还专门防止三类常见问题：文字遮挡图形元素、没有科学含义的装饰性图表、
以及连接线出现不必要的多次折弯。

仓库中还包含两个配套 skill：`research-draw` 用于“生成参考图再临摹为 draw.io”，
`add-svg` 用于为 draw.io 科研图补充 SVG 科学图元。`add-svg` 要求每次执行前先
选择来源：从网络收集多个 SVG 候选并留给用户后续选择，或在网络素材不合适、
找不到时自行绘制克制的原创 SVG。

## 能做什么

- 创建可编辑的 `.drawio` 科研流程图
- 两阶段科研图创建：先生成参考图，再临摹为可编辑 draw.io
- 绘制 Nature 风格的方法流程图和实验设计图
- 绘制计算管线和模型结构示意图
- 绘制包含纳入/排除逻辑的队列或研究流程图
- 绘制论文机制图和图形摘要
- 生成适合 SVG/PDF 导出的论文图，并提供 QA 检查规则

## 示例

### GAN 手写数字生成示例

`example/gan-handwritten-digits/gan-handwritten-digits.drawio` 展示了
`research-draw` 的两阶段工作流：先创建科研插图风格的栅格参考图，再临摹为
可编辑的 draw.io 图元，随后导出预览并进行多轮严格视觉对比。

Codex 输入：

```text
使用$research-draw 帮我绘制一个使用GAN进行手写数字生成的图，科研风格
```

输入参考图：

![GAN handwritten digit reference](assets/reference-images/gan-handwritten-digits-reference.png)

中间 skill 执行流程：

1. `research-draw` 先建立科学信息、拓扑结构、视觉词汇、输出契约和一致性循环要求。
2. `imagegen` 生成栅格参考图；该图只作为构图和几何参考，不嵌入最终 draw.io。
3. `research-drawio-skill` 将参考图重建为可编辑 draw.io 模块：latent-noise 表格、
   generator 层、generated/real digit tiles、discriminator 层、probability mini-chart
   和虚线 loss-feedback 路由。
4. `qa_drawio.py` 检查 `.drawio` 源文件。结果：
   `OK XML parsed; vertices=99 edges=16 warnings=0`。
5. `export_drawio_preview.py` 通过 draw.io Desktop CLI 导出 PNG 和 SVG 预览。
6. `compare_drawio_reference.py` 进行了三轮严格栅格对比，输出 metrics、tile mismatch
   CSV、region mismatch CSV、heatmap、foreground overlay 和 side-by-side 图。

最终可编辑输出预览：

![GAN handwritten digit draw.io output](example/gan-handwritten-digits/exports/gan-handwritten-digits.png)

严格对比证据：

![GAN strict comparison side by side](example/gan-handwritten-digits/comparison-final/side-by-side.png)

像素差异热图：

![GAN strict comparison diff heatmap](example/gan-handwritten-digits/comparison-final/diff-heatmap.png)

前景重叠检查：

![GAN strict comparison foreground overlay](example/gan-handwritten-digits/comparison-final/foreground-overlay.png)

最终产物：

- 可编辑源文件：
  `example/gan-handwritten-digits/gan-handwritten-digits.drawio`
- PNG 预览：
  `example/gan-handwritten-digits/exports/gan-handwritten-digits.png`
- SVG 预览：
  `example/gan-handwritten-digits/exports/gan-handwritten-digits.svg`
- 临摹记录：
  `example/gan-handwritten-digits/trace-notes.md`
- 严格对比报告：
  `example/gan-handwritten-digits/comparison-final/comparison-report.json`

最终严格对比状态为 `not passed`：剩余最大差异区域是 `Real digits`，最终指标为
`mae=17.6241`、`ssim=0.7582`、`foreground_iou=0.7678`、`edge_iou=0.0764`、
`worst_tile_mae=105.0931`。这个示例保留 QA 证据，用于明确展示剩余差异，而不是
把未通过的严格像素对比包装成已经完成。

## 更多示例

| 提示词 | GPT生成图 | 像素差异热图 | drawio图 |
|---|---|---|---|
| 使用$research-draw 帮我绘制一个使用GAN进行手写数字生成的图，科研风格 | <img src="assets/reference-images/gan-handwritten-digits-reference.png" alt="GAN reference" width="180"> | <img src="example/gan-handwritten-digits/comparison-final/diff-heatmap.png" alt="GAN diff heatmap" width="180"> | <img src="example/gan-handwritten-digits/exports/gan-handwritten-digits.png" alt="GAN draw.io output" width="180"> |
| 使用$research-draw 帮我绘制一个使用ResNet进行猫狗图像分类的图，科研风格 | <img src="example/resnet_cat_dog_classification/resnet_cat_dog_reference.png" alt="ResNet cat dog reference" width="180"> | <img src="example/resnet_cat_dog_classification/comparison_iter3/diff-heatmap.png" alt="ResNet cat dog diff heatmap" width="180"> | <img src="example/resnet_cat_dog_classification/exports/resnet_cat_dog_classification.png" alt="ResNet cat dog draw.io output" width="180"> |
| 使用$research-draw 帮我绘制一个使用Transformer进行机器翻译的图，科研风格 | <img src="example/transformer_machine_translation_reference.png" alt="Transformer reference" width="180"> | <img src="example/transformer_machine_translation/diff-heatmap.png" alt="Transformer diff heatmap" width="180"> | <img src="example/transformer_machine_translation/exports/transformer_machine_translation.png" alt="Transformer draw.io output" width="180"> |
| 使用$research-draw 帮我绘制一个使用U-Net进行医学图像分割的图，科研风格 | <img src="example/unet-medical-segmentation/reference-unet-medical-segmentation.png" alt="U-Net medical segmentation reference" width="180"> | <img src="example/unet-medical-segmentation/comparison-iter5/diff-heatmap.png" alt="U-Net medical segmentation diff heatmap" width="180"> | <img src="example/unet-medical-segmentation/exports/unet-medical-segmentation.png" alt="U-Net medical segmentation draw.io output" width="180"> |
| 使用$research-draw 帮我绘制一个使用多组学数据整合进行疾病分型的图，科研风格 | <img src="example/multiomics-disease-subtyping/multiomics-disease-subtyping-reference.png" alt="Multi-omics disease subtyping reference" width="180"> | <img src="example/multiomics-disease-subtyping/comparison-iter3/diff-heatmap.png" alt="Multi-omics disease subtyping diff heatmap" width="180"> | <img src="example/multiomics-disease-subtyping/exports/multiomics-disease-subtyping.png" alt="Multi-omics disease subtyping draw.io output" width="180"> |

## 安装

将需要的 skill 文件夹复制到你的 Codex skills 目录。完整工作流建议安装三个：

```powershell
Copy-Item -Recurse -Force `
  "skills\research-draw" `
  "$env:USERPROFILE\.codex\skills\research-draw"

Copy-Item -Recurse -Force `
  "skills\research-drawio-skill" `
  "$env:USERPROFILE\.codex\skills\research-drawio-skill"

Copy-Item -Recurse -Force `
  "skills\add-svg" `
  "$env:USERPROFILE\.codex\skills\add-svg"
```

macOS 或 Linux：

```bash
mkdir -p ~/.codex/skills
cp -R skills/{research-draw,research-drawio-skill,add-svg} ~/.codex/skills/
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

`research-draw`：

- `SKILL.md`：两阶段“生成参考图再临摹”工作流的主要触发元数据和路由流程。
- `agents/openai.yaml`：用于 Codex UI 的元数据和默认调用提示。
- `references/two-stage-workflow.md`：参考图生成、draw.io 临摹和完成标准。
- `references/imagegen-reference-stage.md`：生成干净科研参考图的 prompt 与检查规则。
- `references/png-layout-extraction.md`：临摹已有 PNG/JPG/WebP 图时的几何提取规则。
- `references/drawio-tracing-stage.md`：从栅格参考图转换为 draw.io 模块、图元、标签、
  公式和连接线的规则。
- `references/complex-asset-sourcing.md`：复杂可识别对象的在线 SVG/矢量素材或自绘兜底策略。
- `references/consistency-loop.md`：交付前的导出、严格对比和迭代修复流程。

`research-drawio-skill`：

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
- `references/export-preview.md`：draw.io Desktop CLI 导出和预览 QA。
- `references/strict-visual-comparison.md`：栅格/GPT/imagegen 参考图与 draw.io PNG 导出的量化对比规则。
- `references/qa-contract.md`：逻辑、视觉、源文件和导出 QA 检查。
- `scripts/qa_drawio.py`：轻量级 QA 脚本，检查未压缩/压缩 draw.io XML、
  数学公式、对齐、端点、文字/图元重叠、标签长度、画布越界、图表语义、
  折线数量和连接线遮挡。
- `scripts/export_drawio_preview.py`：通过本地 diagrams.net/draw.io Desktop CLI 导出 PNG/SVG/PDF 预览并检查输出。
- `scripts/compare_drawio_reference.py`：将 draw.io PNG 导出与栅格参考图对比，并输出指标、错配 tile 和可视化覆盖图。

`add-svg`：

- `SKILL.md`：带来源选择门槛的 SVG 补图路由流程。
- `manifest.yaml`：声明必须先询问来源，并按网络搜索或自行绘制加载参考文件。
- `static/core/contract.md`：SVG 补图契约，包括科学角色、插入位置、来源记录、
  兜底方案和 QA。
- `static/core/stance.md`：面向 Nature 风格科研图的克制、语义化 SVG 补图姿态。
- `references/network-svg-search.md`：从网络收集多个 SVG 候选并记录来源和许可信息。
- `references/self-design-svg.md`：用简单矢量图元自行绘制原创 SVG 的规则。
- `references/drawio-svg-integration.md`：draw.io image cell、data URI、标签、
  位置和候选素材存放规则。
- `references/svg-qa-contract.md`：来源、视觉、draw.io 和交付 QA。
- `scripts/svg_data_uri.py`：将本地 SVG 转为 draw.io 可用的 data URI 或图片样式片段。

## 校验

如果你安装了 Codex `skill-creator` 的校验脚本，可以运行：

```powershell
$env:PYTHONUTF8 = "1"
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" `
  "skills\research-draw"

python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" `
  "skills\research-drawio-skill"

python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" `
  "skills\add-svg"
```

期望输出：

```text
Skill is valid!
```

Windows 下建议设置 `PYTHONUTF8=1`，因为 skill 元数据中包含中文触发词。

检查生成的 `.drawio` 文件：

```powershell
python "skills\research-drawio-skill\scripts\qa_drawio.py" `
  "example\gan-handwritten-digits\gan-handwritten-digits.drawio"
```

```powershell
python "skills\research-drawio-skill\scripts\export_drawio_preview.py" `
  "example\gan-handwritten-digits\gan-handwritten-digits.drawio" `
  --formats png svg
```

```powershell
python "skills\research-drawio-skill\scripts\compare_drawio_reference.py" `
  "assets\reference-images\gan-handwritten-digits-reference.png" `
  "example\gan-handwritten-digits\exports\gan-handwritten-digits.png" `
  --mode strict `
  --regions-json "example\gan-handwritten-digits\regions.json" `
  --out-dir "example\gan-handwritten-digits\comparison-final"
```

在将图作为 polished example 或论文导出文件前，应检查所有 warning 和严格对比失败项。
