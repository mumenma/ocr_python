from fastapi import FastAPI, File, UploadFile
from typing import Optional

import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# 上传上来图片，并对图片进行ocr
@app.post("/ocr")
async def ocr(file: UploadFile = File(...)):
    # 保存上传的文件
    file_path = f"uploaded_images/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # 对图片进行ocr
    result = ocr(file_path)
    return {"result": result}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)