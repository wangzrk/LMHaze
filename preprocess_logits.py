"""
This demo is based on the latest work by the authors of Q-Align: Q-SiT. 
If you want to use the original Q-Align instead, you can easily reuse it by modifying just a few lines of code.

"""
import os
import torch
import numpy as np
from PIL import Image
from tqdm import tqdm
from transformers import AutoProcessor, LlavaOnevisionForConditionalGeneration, AutoTokenizer

def softmax(x):
    x = np.array(x)
    e_x = np.exp(x - np.max(x))  # for numerical stability
    return e_x / e_x.sum()

def process_images(input_dir, output_dir):
    model_id = "zhangzicheng/q-sit-mini"
    model = LlavaOnevisionForConditionalGeneration.from_pretrained(
        model_id,
        torch_dtype=torch.float16,
        low_cpu_mem_usage=True,
    ).to(0)

    processor = AutoProcessor.from_pretrained(model_id)
    tokenizer = AutoTokenizer.from_pretrained(model_id)

    toks = ["Excellent", "Good", "Fair", "Poor", "Bad"]
    ids_ = [id_[0] for id_ in tokenizer(toks)["input_ids"]]

    conversation = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Assume you are an image quality evaluator. \nYour rating should be chosen from the following five categories: Excellent, Good, Fair, Poor, and Bad (from high to low). \nHow would you rate the quality of this image?"},
                {"type": "image"},
            ],
        },
    ]
    prompt = processor.apply_chat_template(conversation, add_generation_prompt=True)
    prefix_text = "The quality of this image is "
    prefix_ids = tokenizer(prefix_text, return_tensors="pt")["input_ids"].to(0)

    # ==== 读取图像 ====
    os.makedirs(output_dir, exist_ok=True)
    image_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    batch_size = 4
    for i in tqdm(range(0, len(image_files), batch_size), desc=f"Processing {input_dir}"):
        batch_files = image_files[i:i + batch_size]
        batch_images = []
        valid_names = []

        for img_name in batch_files:
            try:
                img_path = os.path.join(input_dir, img_name)
                image = Image.open(img_path).convert('RGB')
                batch_images.append(image)
                valid_names.append(img_name)
            except Exception as e:
                print(f"跳过图像 {img_name}，读取失败：{e}")

        if not batch_images:
            continue

        inputs = processor(images=batch_images, text=[prompt]*len(batch_images), return_tensors="pt", padding=True).to(0, torch.float16)
        prefix_ids_expanded = prefix_ids.expand(len(batch_images), -1)
        inputs["input_ids"] = torch.cat([inputs["input_ids"], prefix_ids_expanded], dim=-1)
        inputs["attention_mask"] = torch.ones_like(inputs["input_ids"])

        with torch.no_grad():
            output = model.generate(
                **inputs,
                max_new_tokens=1,
                output_logits=True,
                return_dict_in_generate=True,
            )

        logits = output.logits[-1]

        for j, img_name in enumerate(valid_names):
            logit = logits[j]
            logits_dict = {tok: logit[id_].item() for tok, id_ in zip(toks, ids_)}
            values = list(logits_dict.values())
            probs = softmax(values)  # softmax 后按原顺序
            # print(probs)
            npy_path = os.path.join(output_dir, os.path.splitext(img_name)[0] + ".npy")
            np.save(npy_path, np.array(probs, dtype=np.float32))


# ===== 多个目录批量处理 =====
if __name__ == "__main__":
    # 示例：多个 input/output 对
    dir_pairs = [
        #  (input_dir, output_dir)
    ]

    for input_dir, output_dir in dir_pairs:
        process_images(input_dir, output_dir)
