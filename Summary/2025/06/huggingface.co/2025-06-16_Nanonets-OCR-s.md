---
title: 'nanonets/Nanonets-OCR-s · Hugging Face'
source: https://huggingface.co/nanonets/Nanonets-OCR-s
author:
  - huggingface.co
published: ''
fetched: '2025-06-16T15:24:32.796627+00:00'
tags:
  - codex
  - ocr
image: https://cdn-thumbnails.huggingface.co/social-thumbnails/models/nanonets/Nanonets-OCR-s.png
---

## 要約

Nanonets-OCR-s は、画像から文章だけでなく文書構造も認識して Markdown に変換する OCR モデルで、数式を LaTeX 化し、図や表、署名、透かし、チェックボックスなどを意味的にタグ付けする。複雑な表も HTML 形式で抽出でき、LLM との連携に適した高精度な出力を実現する。Transformers や vLLM、docext などから利用可能で、サンプルコードも示されている。このモデルはノイズの多い文書や手書きにも対応し、処理結果は LLM に直接渡せる。vLLM を使った推論サーバの建て方や、API 呼び出し例、docext ライブラリからの利用手順、さらに BibTex 記述も掲載されている。

## 本文

Nanonets-OCR-s is a powerful, state-of-the-art image-to-markdown OCR model that goes far beyond traditional text extraction. It transforms documents into structured markdown with intelligent content recognition and semantic tagging, making it ideal for downstream processing by Large Language Models (LLMs).

Nanonets-OCR-s is packed with features designed to handle complex documents with ease:

* **LaTeX Equation Recognition:** Automatically converts mathematical equations and formulas into properly formatted LaTeX syntax. It distinguishes between inline (`$...$`) and display (`$$...$$`) equations.
* **Intelligent Image Description:** Describes images within documents using structured `<img>` tags, making them digestible for LLM processing. It can describe various image types, including logos, charts, graphs and so on, detailing their content, style, and context.
* **Signature Detection & Isolation:** Identifies and isolates signatures from other text, outputting them within a `<signature>` tag. This is crucial for processing legal and business documents.
* **Watermark Extraction:** Detects and extracts watermark text from documents, placing it within a `<watermark>` tag.
* **Smart Checkbox Handling:** Converts form checkboxes and radio buttons into standardized Unicode symbols (`☐`, `☑`, `☒`) for consistent and reliable processing.
* **Complex Table Extraction:** Accurately extracts complex tables from documents and converts them into both markdown and HTML table formats.

📢 [Read the full announcement](https://nanonets.com/research/nanonets-ocr-s) | 🤗 [Hugging Face Space Demo](https://huggingface.co/spaces/Souvik3333/Nanonets-ocr-s)

Usage
-----

### Using transformers

```
from PIL import Image
from transformers import AutoTokenizer, AutoProcessor, AutoModelForImageTextToText

model_path = "nanonets/Nanonets-OCR-s"

model = AutoModelForImageTextToText.from_pretrained(
    model_path, 
    torch_dtype="auto", 
    device_map="auto", 
    attn_implementation="flash_attention_2"
)
model.eval()

tokenizer = AutoTokenizer.from_pretrained(model_path)
processor = AutoProcessor.from_pretrained(model_path)


def ocr_page_with_nanonets_s(image_path, model, processor, max_new_tokens=4096):
    prompt = """Extract the text from the above document as if you were reading it naturally. Return the tables in html format. Return the equations in LaTeX representation. If there is an image in the document and image caption is not present, add a small description of the image inside the <img></img> tag; otherwise, add the image caption inside <img></img>. Watermarks should be wrapped in brackets. Ex: <watermark>OFFICIAL COPY</watermark>. Page numbers should be wrapped in brackets. Ex: <page_number>14</page_number> or <page_number>9/22</page_number>. Prefer using ☐ and ☑ for check boxes."""
    image = Image.open(image_path)
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": [
            {"type": "image", "image": f"file://{image_path}"},
            {"type": "text", "text": prompt},
        ]},
    ]
    text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = processor(text=[text], images=[image], padding=True, return_tensors="pt")
    inputs = inputs.to(model.device)
    
    output_ids = model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=False)
    generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in zip(inputs.input_ids, output_ids)]
    
    output_text = processor.batch_decode(generated_ids, skip_special_tokens=True, clean_up_tokenization_spaces=True)
    return output_text[0]

image_path = "/path/to/your/document.jpg"
result = ocr_page_with_nanonets_s(image_path, model, processor, max_new_tokens=15000)
print(result)

```

### Using vLLM

1. Start the vLLM server.

```
vllm serve nanonets/Nanonets-OCR-s

```

2. Predict with the model

```
from openai import OpenAI
import base64

client = OpenAI(api_key="123", base_url="http://localhost:8000/v1")

model = "nanonets/Nanonets-OCR-s"

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def ocr_page_with_nanonets_s(img_base64):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{img_base64}"},
                    },
                    {
                        "type": "text",
                        "text": "Extract the text from the above document as if you were reading it naturally. Return the tables in html format. Return the equations in LaTeX representation. If there is an image in the document and image caption is not present, add a small description of the image inside the <img></img> tag; otherwise, add the image caption inside <img></img>. Watermarks should be wrapped in brackets. Ex: <watermark>OFFICIAL COPY</watermark>. Page numbers should be wrapped in brackets. Ex: <page_number>14</page_number> or <page_number>9/22</page_number>. Prefer using ☐ and ☑ for check boxes.",
                    },
                ],
            }
        ],
        temperature=0.0,
        max_tokens=15000
    )
    return response.choices[0].message.content

test_img_path = "/path/to/your/document.jpg"
img_base64 = encode_image(test_img_path)
print(ocr_page_with_nanonets_s(img_base64))

```

### Using docext

```
pip install docext
python -m docext.app.app --model_name hosted_vllm/nanonets/Nanonets-OCR-s

```

Checkout [GitHub](https://github.com/NanoNets/docext/tree/dev/markdown) for more details.

BibTex
------

```
@misc{Nanonets-OCR-S,
  title={Nanonets-OCR-S: A model for transforming documents into structured markdown with intelligent content recognition and semantic tagging},
  author={Souvik Mandal and Ashish Talewar and Paras Ahuja and Prathamesh Juvatkar},
  year={2025},
}

```
