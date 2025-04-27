from fastapi import FastAPI, File, UploadFile
from typing import Optional
import uvicorn
import os
import time
import random
import string

from ocr import ocr

app = FastAPI()

# 确保uploaded_images目录存在
os.makedirs("uploaded_images", exist_ok=True)

def generate_unique_filename(original_filename):
    # 获取文件扩展名
    ext = os.path.splitext(original_filename)[1]
    # 生成时间戳
    timestamp = int(time.time() * 1000)
    # 生成随机字符串
    random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    # 组合成新文件名
    return f"{timestamp}_{random_str}{ext}"

def process_ocr(image_path):
    try:
        result = ocr(image_path)
        return {"code": 0, "message": "success", "data": result}
    except Exception as e:
        return {"code": 1, "message": str(e), "data": None}

@app.get("/")
async def root():
    return {"code": 0, "message": "success", "data": "Hello World"}

# 上传上来图片，并对图片进行ocr
@app.post("/ocr")
async def ocr_endpoint(file: UploadFile = File(...)):
    try:
        # 生成唯一文件名
        unique_filename = generate_unique_filename(file.filename)
        # 保存上传的文件
        file_path = f"uploaded_images/{unique_filename}"
        with open(file_path, "wb") as f:
            f.write(await file.read())

        # 对图片进行ocr
        result = process_ocr(file_path)
        return result
    except Exception as e:
        return {"code": 1, "message": str(e), "data": None}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8010)