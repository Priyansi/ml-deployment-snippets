import requests
import json
import base64

with open("test_image.jpg", "rb") as image_file:
    base64str = base64.b64encode(image_file.read()).decode("utf-8")

payload = json.dumps({
    "base64str": base64str,
})
response = requests.put(
    "https://testcatordogapp.herokuapp.com/predict", data=payload)
data_dict = response.json()
print(data_dict)
print(f"Predicted : {data_dict['category']}")
