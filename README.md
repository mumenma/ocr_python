# ocr_python


pip install fastapi
pip install fastapi uvicorn

pip install python-multipart  使用上传功能

运行起来的命令：
uvicorn main:app --reload ， 如果main函数里面直接用了uvicorn的话，就不用这个了，直接运行Python就可以了



# 所使用的库
https://github.com/PaddlePaddle/PaddleOCR

# 安装PaddlePaddle¶

如果您没有基础的Python运行环境，请参考运行环境准备。


CPU端安装
python -m pip install paddlepaddle==3.0.0rc1 -i https://www.paddlepaddle.org.cn/packages/stable/cpu/

2. 安装paddleocr¶


pip install paddleocr

# 打docker镜像
# 构建镜像
docker build -t ocr-service .

# 运行容器
docker run -p 8010:8010 ocr-service


# 下载docker 镜像运行方法
```
docker pull ghcr.io/mumenma/ocr_python:main
docker run -p 8010:8010 ghcr.io/mumenma/ocr_python:main
```