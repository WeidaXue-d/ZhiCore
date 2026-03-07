# ZhiCore (智核)

> **"Language is the ultimate instruction set."**

**ZhiCore (智核)** 是一个基于 Transformer 架构的极简原生中文语义引擎。不同于传统的文本生成模型，ZhiCore 致力于通过针对性优化的中文 BPE 算法，将自然语言直接映射为逻辑指令，探索“语言即代码”（Language-as-Code）的本地化智能体实现。

---

## 项目愿景 (Project Visions)

* **原生中文语义 (Chinese-Native Semantics)**: 采用自定义 BPE 算法，将“循环”、“如果”、“执行”等功能性词汇处理为高优先级的语义 Token。
* **指令映射架构 (Instruction Mapping)**: 超越简单的文本生成，实现模型输出到系统级函数调用的直接映射。
* **本地化高性能 (Minimalist & Local)**: 针对 **Apple Silicon (MPS)** 进行优化，确保在 Mac 本地环境下的高效科研与迭代。
* **可扩展微内核 (Extensible Architecture)**: 模块化设计，预留多模态（视觉/听觉）接入接口，具备极强的灵活性。

---

## 核心架构 (Architecture)

项目采用解耦的四阶段模块化设计，确保每一部分的独立开发与无缝集成：

| 阶段 | 模块名称 | 核心职责 |
| :--- | :--- | :--- |
| **Stage 1** | `1_Tokenizer` | **语义压缩**: 实现针对中文逻辑词优化的自定义 BPE 编码。 |
| **Stage 2** | `2_Model` | **神经内核**: 基于 Transformer Decoder 的轻量化推理引擎（支持 MPS 加速）。 |
| **Stage 3** | `3_Executor` | **逻辑桥接**: “指令解释器”，将 Token 序列转化为具体的 Python 动作执行。 |
| **Stage 4** | `4_Multimodal` | **感官扩展**: (长期规划) 引入 Vision Encoder，实现基于视觉反馈的逻辑决策。 |

---

## 目录结构 (Directory Structure)

```text
ZhiCore/
├── 1_Tokenizer/        # BPE 训练逻辑与中文编码映射
├── 2_Model/            # Transformer 架构实现 (Attention, MLP, Config)
├── 3_Executor/         # 语义虚拟机与动作执行脚本
├── 4_Multimodal/       # (开发中) 视觉/音频集成模块
├── data/               # 原始中文语料与逻辑指令训练集
└── scripts/            # 工具脚本 (数据预处理、本地测试等)