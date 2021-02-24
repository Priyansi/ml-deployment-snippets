from fastapi import FastAPI
from pydantic import BaseModel
import io
import base64
from PIL import Image
from utils import get_prediction

app = FastAPI()


class Input(BaseModel):
    base64str: str


def base64str_to_PILImage(base64str):
    base64_img_bytes = base64str.encode('utf-8')
    base64bytes = base64.b64decode(base64_img_bytes)
    bytes_obj = io.BytesIO(base64bytes)
    img = Image.open(bytes_obj)
    return img


@app.put("/predict")
def get_predictionbase64(inp_obj: Input):
    img = base64str_to_PILImage(inp_obj.base64str)
    pred = get_prediction(img)
    return {'category': pred}
