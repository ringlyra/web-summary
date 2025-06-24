---
title: 'moonshotai/Kimi-VL-A3B-Thinking-2506 · Hugging Face'
source: https://huggingface.co/moonshotai/Kimi-VL-A3B-Thinking-2506
author:
  - huggingface.co
published: ''
fetched: '2025-06-23T15:46:00.799188+00:00'
tags:
  - codex
  - huggingface
image: https://cdn-thumbnails.huggingface.co/social-thumbnails/models/moonshotai/Kimi-VL-A3B-Thinking-2506.png
---

## 要約

Kimi-VL-A3B-Thinking-2506は従来版を大幅に改良したマルチモーダルモデルで、推論精度を向上させつつ思考時のトークン消費を20%削減する。視覚認識も強化されMMBench-ENで84.4点、VideoMMMUで65.2点を達成し、広範なベンチマークで優位な成績を示した。高解像度に対応し総画素数320万まで扱えるため、OSWorld-GやScreenSpot-Proでも性能向上が確認されている。動画解析機能も改善され、多様なシナリオで安定した出力を得られる。VLLMやTransformersを用いた推論手順が丁寧に紹介され、研究利用に向けた技術報告書の引用情報も掲載された。利用者は新モデルへの移行を推奨されている。

## 本文

> This is an improved version of [Kimi-VL-A3B-Thinking](https://huggingface.co/moonshotai/Kimi-VL-A3B-Thinking). Please consider using this updated model instead of the previous version.

> Please visit our tech blog for recommended inference recipe of this model: [Kimi-VL-A3B-Thinking-2506: A Quick Navigation](https://huggingface.co/blog/moonshotai/kimi-vl-a3b-thinking-2506)

1. Introduction
---------------

This is an updated version of [Kimi-VL-A3B-Thinking](https://huggingface.co/moonshotai/Kimi-VL-A3B-Thinking), with following improved abilities:

* **It Thinks Smarter while Consuming Less Tokens**: The 2506 version reaches better accuracy on multimodal reasoning benchmarks: 56.9 on MathVision (+20.1), 80.1 on MathVista (+8.4), 46.3 on MMMU-Pro (+3.3), 64.0 on MMMU (+2.1), while in average requires 20% reduced thinking length.
* **It Sees Clearer with Thinking**: Unlike the previous version that specializes on thinking tasks, the 2506 version can also achieve the same or even better ability on general visual perception and understanding, e.g. MMBench-EN-v1.1 (84.4), MMStar (70.4), RealWorldQA (70.0), MMVet (78.4), surpassing or matching abilties of our non-thinking model ([Kimi-VL-A3B-Instruct](https://huggingface.co/moonshotai/Kimi-VL-A3B-Instruct)).
* **It Extends to Video Scenarios**: The new 2506 version also improves on video reasoning and understanding benchmarks. It sets new state-of-the-art for open-source models on VideoMMMU (65.2), while also retains good ability on general video understanding (71.9 on Video-MME, matching [Kimi-VL-A3B-Instruct](https://huggingface.co/moonshotai/Kimi-VL-A3B-Instruct)).
* **It Extends to Higher Resolution**: The new 2506 version supports 3.2 million total pixels in a single image, 4X compared to the previous version. This leads to non-trivial improvements on high-resolution perception and OS-agent grounding benchmarks: 83.2 on V\* Benchmark (without extra tools), 52.8 on ScreenSpot-Pro, 52.5 on OSWorld-G (full set with refusal).

2. Performance
--------------

Comparison with efficient models and two previous versions of Kimi-VL (\*Results of GPT-4o is for reference here, and shown in *italics*):

| Benchmark (Metric) | GPT-4o | Qwen2.5-VL-7B | Gemma3-12B-IT | Kimi-VL-A3B-Instruct | Kimi-VL-A3B-Thinking | Kimi-VL-A3B-Thinking-2506 |
| --- | --- | --- | --- | --- | --- | --- |
| **General Multimodal** |  |  |  |  |  |  |
| MMBench-EN-v1.1 (Acc) | *83.1* | 83.2 | 74.6 | 82.9 | 76.0 | **84.4** |
| RealWorldQA (Acc) | *75.4* | 68.5 | 59.1 | 68.1 | 64.0 | **70.0** |
| OCRBench (Acc) | *815* | 864 | 702 | 864 | 864 | **869** |
| MMStar (Acc) | *64.7* | 63.0 | 56.1 | 61.7 | 64.2 | **70.4** |
| MMVet (Acc) | *69.1* | 67.1 | 64.9 | 66.7 | 69.5 | **78.1** |
| **Reasoning** |  |  |  |  |  |  |
| MMMU (val, Pass@1) | *69.1* | 58.6 | 59.6 | 57.0 | 61.7 | **64.0** |
| MMMU-Pro (Pass@1) | *51.7* | 38.1 | 32.1 | 36.0 | 43.2 | **46.3** |
| **Math** |  |  |  |  |  |  |
| MATH-Vision (Pass@1) | *30.4* | 25.0 | 32.1 | 21.7 | 36.8 | **56.9** |
| MathVista\_MINI (Pass@1) | *63.8* | 68.0 | 56.1 | 68.6 | 71.7 | **80.1** |
| **Video** |  |  |  |  |  |  |
| VideoMMMU (Pass@1) | *61.2* | 47.4 | 57.0 | 52.1 | 55.5 | **65.2** |
| MMVU (Pass@1) | *67.4* | 50.1 | 57.0 | 52.7 | 53.0 | **57.5** |
| Video-MME (w/ sub.) | *77.2* | 71.6 | 62.1 | **72.7** | 66.0 | 71.9 |
| **Agent Grounding** |  |  |  |  |  |  |
| ScreenSpot-Pro (Acc) | *0.8* | 29.0 | — | 35.4 | — | **52.8** |
| ScreenSpot-V2 (Acc) | *18.1* | 84.2 | — | **92.8** | — | 91.4 |
| OSWorld-G (Acc) | - | *31.5* | — | 41.6 | — | **52.5** |
| **Long Document** |  |  |  |  |  |  |
| MMLongBench-DOC (Acc) | *42.8* | 29.6 | 21.3 | 35.1 | 32.5 | **42.1** |

Comparison with 30B-70B open-source models:

| Benchmark (Metric) | Kimi-VL-A3B-Thinking-2506 | Qwen2.5-VL-32B | Qwen2.5-VL-72B | Gemma3-27B-IT |
| --- | --- | --- | --- | --- |
| **General Multimodal** |  |  |  |  |
| MMBench-EN-v1.1 (Acc) | 84.4 | - | 88.3 | 78.9 |
| RealWorldQA (Acc) | 70.0 | - | 75.7 | 62.5 |
| OCRBench (Acc) | 869 | - | 885 | 753 |
| MMStar (Acc) | 70.4 | 69.5 | 70.8 | 63.1 |
| MMVet (Acc) | 78.1 | - | 74.0 | 71.0 |
| **Reasoning** |  |  |  |  |
| MMMU (val, Pass@1) | 64.0 | 70.0 | 70.2 | 64.9 |
| MMMU-Pro (Pass@1) | 46.3 | 49.5 | 51.1 | - |
| MATH-Vision (Pass@1) | 56.9 | 38.4 | 38.1 | 35.4 |
| MathVista\_MINI (Pass@1) | 80.1 | 74.7 | 74.8 | 59.8 |
| **Video** |  |  |  |  |
| VideoMMMU (Pass@1) | 65.2 | - | 60.2 | 61.8 |
| MMVU (Pass@1) | 57.5 | - | 62.9 | 61.3 |
| Video-MME (w/ sub.) | 71.9 | 70.5/77.9 | 73.3/79.1 | - |
| **Agent Grounding** |  |  |  |  |
| ScreenSpot-Pro (Acc) | 52.8 | 39.4 | 43.6 | - |
| ScreenSpot-V2 (Acc) | 91.4 | - | - | - |
| OSWorld-G (Acc) | 52.5 | 46.5 | - | - |
| **Long Document** |  |  |  |  |
| MMLongBench-DOC (Acc) | 42.1 | - | 38.8 | - |

3. Usage
--------

### 3.1. Inference with VLLM (recommended)

As a long-decode model that will generates up to 32K tokens, we recommend using [VLLM](https://github.com/vllm-project/vllm/tree/main/vllm) for inference, which has already supported Kimi-VL series.

```
MAX_JOBS=4 pip install vllm==0.9.1 blobfile flash-attn --no-build-isolation

```

> It is important to explicitly install flash-attn to avoid CUDA out-of-memory.

```
from transformers import AutoProcessor
from vllm import LLM, SamplingParams

model_path = "moonshotai/Kimi-VL-A3B-Thinking-2506"
llm = LLM(
    model_path,
    trust_remote_code=True,
    max_num_seqs=8,
    max_model_len=131072,
    limit_mm_per_prompt={"image": 256}
)

processor = AutoProcessor.from_pretrained(model_path, trust_remote_code=True)

sampling_params = SamplingParams(max_tokens=32768, temperature=0.8)


import requests
from PIL import Image

def extract_thinking_and_summary(text: str, bot: str = "◁think▷", eot: str = "◁/think▷") -> str:
    if bot in text and eot not in text:
        return ""
    if eot in text:
        return text[text.index(bot) + len(bot):text.index(eot)].strip(), text[text.index(eot) + len(eot) :].strip()
    return "", text

OUTPUT_FORMAT = "--------Thinking--------\n{thinking}\n\n--------Summary--------\n{summary}"

url = "https://huggingface.co/spaces/moonshotai/Kimi-VL-A3B-Thinking/resolve/main/images/demo6.jpeg"
image = Image.open(requests.get(url,stream=True).raw)

messages = [
    {"role": "user", "content": [{"type": "image", "image": ""}, {"type": "text", "text": "What kind of cat is this? Answer with one word."}]}
]
text = processor.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt")

outputs = llm.generate([{"prompt": text, "multi_modal_data": {"image": image}}], sampling_params=sampling_params)
generated_text = outputs[0].outputs[0].text

thinking, summary = extract_thinking_and_summary(generated_text)
print(OUTPUT_FORMAT.format(thinking=thinking, summary=summary))

```

### 3.2. Inference with 🤗 Hugging Face Transformers

We introduce how to use our model at inference stage using transformers library. It is recommended to use python=3.10, torch>=2.1.0, and transformers=4.48.2 as the development environment.

```
from PIL import Image
from transformers import AutoModelForCausalLM, AutoProcessor

def extract_thinking_and_summary(text: str, bot: str = "◁think▷", eot: str = "◁/think▷") -> str:
    if bot in text and eot not in text:
        return ""
    if eot in text:
        return text[text.index(bot) + len(bot):text.index(eot)].strip(), text[text.index(eot) + len(eot) :].strip()
    return "", text

OUTPUT_FORMAT = "--------Thinking--------\n{thinking}\n\n--------Summary--------\n{summary}"

url = "https://huggingface.co/spaces/moonshotai/Kimi-VL-A3B-Thinking/resolve/main/images/demo6.jpeg"

model_path = "moonshotai/Kimi-VL-A3B-Thinking-2506"
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype="auto",
    device_map="auto",
    trust_remote_code=True,
)
processor = AutoProcessor.from_pretrained(model_path, trust_remote_code=True)

image_paths = ["url"]
images = [Image.open(path) for path in image_paths]
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": image_path} for image_path in image_paths
        ] + [{"type": "text", "text": ""What kind of cat is this? Answer with one word."}],
    },
]
text = processor.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt")
inputs = processor(images=images, text=text, return_tensors="pt", padding=True, truncation=True).to(model.device)
generated_ids = model.generate(**inputs, max_new_tokens=32768, temperature=0.8)
generated_ids_trimmed = [
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
]
response = processor.batch_decode(
    generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
)[0]
print(response)

```

4. Citation
-----------

```
@misc{kimiteam2025kimivltechnicalreport,
      title={{Kimi-VL} Technical Report}, 
      author={Kimi Team and Angang Du and Bohong Yin and Bowei Xing and Bowen Qu and Bowen Wang and Cheng Chen and Chenlin Zhang and Chenzhuang Du and Chu Wei and Congcong Wang and Dehao Zhang and Dikang Du and Dongliang Wang and Enming Yuan and Enzhe Lu and Fang Li and Flood Sung and Guangda Wei and Guokun Lai and Han Zhu and Hao Ding and Hao Hu and Hao Yang and Hao Zhang and Haoning Wu and Haotian Yao and Haoyu Lu and Heng Wang and Hongcheng Gao and Huabin Zheng and Jiaming Li and Jianlin Su and Jianzhou Wang and Jiaqi Deng and Jiezhong Qiu and Jin Xie and Jinhong Wang and Jingyuan Liu and Junjie Yan and Kun Ouyang and Liang Chen and Lin Sui and Longhui Yu and Mengfan Dong and Mengnan Dong and Nuo Xu and Pengyu Cheng and Qizheng Gu and Runjie Zhou and Shaowei Liu and Sihan Cao and Tao Yu and Tianhui Song and Tongtong Bai and Wei Song and Weiran He and Weixiao Huang and Weixin Xu and Xiaokun Yuan and Xingcheng Yao and Xingzhe Wu and Xinxing Zu and Xinyu Zhou and Xinyuan Wang and Y. Charles and Yan Zhong and Yang Li and Yangyang Hu and Yanru Chen and Yejie Wang and Yibo Liu and Yibo Miao and Yidao Qin and Yimin Chen and Yiping Bao and Yiqin Wang and Yongsheng Kang and Yuanxin Liu and Yulun Du and Yuxin Wu and Yuzhi Wang and Yuzi Yan and Zaida Zhou and Zhaowei Li and Zhejun Jiang and Zheng Zhang and Zhilin Yang and Zhiqi Huang and Zihao Huang and Zijia Zhao and Ziwei Chen},
      year={2025},
      eprint={2504.07491},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2504.07491}, 
}

```
