import requests
from base64 import b64encode

# Set the API endpoint
url = "https://api.imgbb.com/1/upload"

# Set the API key
key = "ce1b4391a061ddebb83ede95642e9ea0"

# Set the image file path
image_path = "test_image.webp"

# Encode the image file as base64
image_data = b64encode(open(image_path, "rb").read())

# Set the API parameters
payload = {
    "key": key,
    "image": image_data,
    "name": image_path,
    "expiration": 600,  # Optional, delete the image after 10 minutes
}

# Make the POST request and get the response
response = requests.post(url, data=payload)

# Print the response JSON
print(response.json())
