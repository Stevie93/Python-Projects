import requests
import json


SUBSCRIPTION_KEY = "0e576e5c87844ce49dd06dfd9ee0d455"
vision_service_address = "https://sfmimageanalyzer.cognitiveservices.azure.com/"
address = vision_service_address + "analyze"

parameters = {
    'visualFeatures': 'Description,Color',
    'language': 'en'
}

image_path = "./TestImages/WebForge2.png"
image_data = open(image_path, "rb").read()

headers = {
    'content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY
}

response = requests.post(address, headers=headers,
                         params=parameters, data=image_data)

response.raise_for_status()

resuts = response.json()
print(json.dumps(resuts))
