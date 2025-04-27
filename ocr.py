from paddleocr import PaddleOCR

def ocr(img_path):
    ocr = PaddleOCR(lang='ch', show_log=False) # need to run only once to download and load model into memory
    result = ocr.ocr(img_path, cls=False)
    return result