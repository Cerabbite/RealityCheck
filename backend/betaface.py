import json
import requests

# import base64

# path = "test_image.webp"
# with open(path, "rb") as image_file:
#     encoded_string = base64.b32encode(image_file.read())


def get_facial_features(path=None, url=None, filename=None):
    if not path:
        if not filename:
            return [-1, "Excepted a filename"]
        data = {
            "api_key": "d45fd466-51e2-4701-8da8-04351c872236",
            "file_uri": url,
            "detection_flags": "basicpoints,propoints,classifiers,content",
            "recognize_targets": ["all@mynamespace"],
            "original_filename": path,  # "GettyImages-1092658864_hero-1024x575.jpg",
        }
    else:
        return [-2, "Path feature is not yet implemented"]

    response = requests.post(url, json=data, timeout=20)
    # print(f"Status Code: {response.status_code}")
    # print(f"JSON Response: {response.json()}")
    if response.status_code != 200:
        return [response.status_code, response.json]

    return [0, response.json]

    # with open("demo-persona.json", "r") as file:
    #     data = json.load(file)
    #     return 0, data
