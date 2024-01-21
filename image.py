import requests
from openai import OpenAI


client = OpenAI()

response = client.images.generate(
    model="dall-e-3",
    prompt="3d couples having fun on the beach in swim suits",
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url

# Use requests to download the image
image_response = requests.get(image_url)

# Check if the request was successful
if image_response.status_code == 200:
    # Open a file in write mode and save the image to it
    with open('image.png', 'wb') as f:
        f.write(image_response.content)
else:
    print("Failed to download the image")

print(image_url)
