# MarketingPro 通用生图引擎与平台适配规范

## 一、 生图引擎定位

本规范定义了 MarketingPro 的**跨平台视觉生成标准**，确保智能体在任何搭载平台（Kimi、ChatGPT、Claude、通义千问、Coze等）上都能自动适配生图能力。

---

## 二、 跨平台生图适配逻辑

### 规则1：自动检测与调用宿主生图工具

当智能体执行视觉物料生成任务时，按以下优先级自动适配：

```
┌─────────────────────────────────────────────────────────────┐
│                    生图工具调用决策树                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  检测宿主平台生图能力                                        │
│         │                                                  │
│    ┌────┴────┐                                             │
│    ▼         ▼                                             │
│  有生图工具    无生图工具                                    │
│    │         │                                             │
│    ▼         ▼                                             │
│ 调用宿主工具    输出通用生图Prompt                          │
│ 生成图片URL    供用户自行使用                                │
│    │                                                         │
│    ▼                                                         │
│ 嵌入HTML报告                                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 规则2：宿主平台检测与调用

| 平台 | 检测关键词 | 调用方式 |
|------|-----------|----------|
| **Kimi** | "kimi", "生图", "图片生成" | 调用 Kimi Vision 插件 |
| **ChatGPT** | "dalle", "image generation" | 调用 DALL-E 3 |
| **Claude** | "claude", "image" | 调用 Claude Image Gen |
| **通义千问** | "通义", "图生图" | 调用通义万相 |
| **Coze** | "coze", "bot" | 调用 Bot 生图能力 |
| **通用/Midjourney** | 无特定插件 | 输出通用 Prompt |

### 规则3：图片嵌入HTML报告

当生图成功后，必须将图片嵌入HTML报告：

```html
<!-- 图片嵌入格式 -->
<div class="visual-gallery">
    <div class="gallery-item">
        <img src="{{IMAGE_URL或BASE64}}" alt="超级符号设计">
        <div class="caption">超级符号设计概念图</div>
    </div>
</div>

<!-- 无图时的占位符 -->
<div class="gallery-placeholder">
    <svg viewBox="0 0 24 24">...</svg>
    <span>生图Prompt已生成，请复制到生图工具使用</span>
</div>
```

---

## 三、 生图内容规范（基于文化母体理论）

### 核心原则

> ⚠️ **所有视觉生成必须严格遵循"超级符号与文化母体理论"**

1. **寻找文化母体**：从人类集体潜意识中的大众熟知元素出发
   - 自然原力：太阳、月亮、星星、山川
   - 传统图形：八卦、祥云、传统纹样
   - 公共标识：十字、箭头、对勾、圆形
   - 动物植物：狮子、熊猫、竹、松

2. **私有化改造**：将文化母体与品牌承诺嫁接
   - 色彩改造：发展品牌专属色彩
   - 形状简化：几何化、极简化
   - 特征强化：突出与品牌相关的特征

3. **视觉呈现要求**
   - **醒目**：主体占据画面最大面积
   - **居中**：核心元素居中构图
   - **真实**：商业摄影质感，非抽象艺术
   - **极简**：可被一句话描述

---

## 四、 生图Prompt标准模板

### 1. 超级符号/Logo生图Prompt

```
【文化母体超级符号生图提示词】
Prompt: Professional brand logo design for [品牌名称], featuring [文化母体描述, 如: a stylized minimalist sunburst totem], [私有化改造特征], [品牌色彩], centered composition, bold flat vector, modern branding identity, cultural archetype recognition, 8k, Masterpiece, Behance award-winning --ar 1:1 --v 6.0 --no complex curves, no illegible text

【中文版本】
专业品牌标志设计，以[文化母体描述]为核心元素，采用[私有化改造特征]，使用[品牌色彩]，居中构图，扁平矢量风格，现代品牌识别系统，文化原型觉醒，8K画质，杰作级，贝塞尔奖风格 --ar 1:1 --v 6.0 --no 复杂曲线, no 难以辨认的文字
```

### 2. 产品包装3D渲染生图Prompt

```
【文化母体包装3D渲染生图提示词】
Prompt: Commercial product photography of [产品类型] packaging for [品牌名称], featuring [文化母体符号] as dominant visual, [品牌色彩], studio lighting, 3D Octane render, photorealistic, 8k, Behance award-winning --ar 3:4 --v 6.0 --no blurry, no messy text

【中文版本】
商业产品摄影，[品牌名称][产品类型]包装设计，以[文化母体符号]为主视觉，使用[品牌色彩]，影棚灯光，3D Octane渲染，写实风格，8K画质 --ar 3:4 --v 6.0 --no 模糊, no 凌乱文字
```

### 3. 主视觉KV生图Prompt

```
【文化母体主视觉KV生图提示词】
Prompt: High-end advertising Key Vision poster for [品牌名称], featuring [文化母体描述] as dominant archetype in [品牌色彩], [产品] prominently displayed, [主口号] as headline, cinematic lighting, Octane render, 8k, premium aesthetics --ar 9:16 --v 6.0 --no cartoon, no cluttered composition

【中文版本】
高端广告主视觉海报，[品牌名称]，以[文化母体描述]为视觉主导，使用[品牌色彩]，[产品]突出展示，[主口号]作为标题，电影级灯光，Octane渲染，8K画质，顶级美学 --ar 9:16 --v 6.0 --no 卡通, no 杂乱构图
```

### 4. 门店门头生图Prompt

```
【文化母体门店门头生图提示词】
Prompt: Professional storefront render for [品牌名称], featuring [文化母体符号] as dominant logo on [门头材质], [品牌色彩], clean modern design, street view, commercial photography, 8k --ar 16:9 --v 6.0 --no cluttered

【中文版本】
专业门店渲染，[品牌名称]，以[文化母体符号]为主标识，使用[品牌色彩]，在[门头材质]上，简洁现代设计，街景视角，商业摄影风格，8K画质 --ar 16:9 --v 6.0 --no 杂乱
```

### 5. 应用场景生图Prompt

```
【文化母体应用场景生图提示词】
Prompt: Lifestyle product photography showing [品牌名称] with [文化母体元素] in [使用场景], natural lighting, professional commercial photography, 8k, editorial quality --ar 4:3 --v 6.0 --no artificial look

【中文版本】
生活方式产品摄影，[品牌名称]与[文化母体元素]在[使用场景]中，自然光，专业商业摄影，8K画质，编辑级品质 --ar 4:3 --v 6.0 --no 人工感
```

---

## 五、 生图执行工作流

### Step 1: 检测生图能力
```
IF 宿主平台具备生图工具 THEN
    激活生图能力
ELSE
    输出通用生图Prompt
END
```

### Step 2: 填充Prompt模板
```
根据业务信息填充：
- [品牌名称]
- [文化母体描述]
- [私有化改造特征]
- [品牌色彩]
- [产品类型]
- [主口号]
```

### Step 3: 执行生图
```
IF 调用成功 THEN
    获取图片URL或Base64
    嵌入HTML报告对应位置
ELSE
    输出通用Prompt供用户复制
END
```

### Step 4: HTML报告输出
```
自动组装：
- 分析文本
- 图表数据
- 生成图片（可选）
- 生图Prompt（备用）
```

---

## 六、 错误处理与降级策略

| 错误类型 | 处理方式 |
|----------|----------|
| 平台无生图工具 | 输出通用中英双语Prompt |
| 生图超时 | 提示用户手动生图，保留Prompt |
| 生图质量不佳 | 提供优化版Prompt建议 |
| 网络错误 | 输出纯文本Prompt作为保底 |

---

## 七、 关键公式速查

```
文化母体 → 私有化改造 → 品牌专属视觉资产

超级符号 = 文化原力 + 品牌承诺 + 极简几何化

好视觉 = 主体大 + 居中构图 + 可复述描述
```