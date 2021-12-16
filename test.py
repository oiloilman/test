import requests
import io
from PIL import Image

response = requests.get("https://i.imgur.com/ExdKOOz.png")
image_bytes = io.BytesIO(response.content)

img = Image.open(image_bytes)
print(f'Size: {img.size}')
img.show()
