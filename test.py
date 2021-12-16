Image.open(urlopen(url))
Image.open(urlopen(url).read())
from PIL import Image
import requests
from io import BytesIO

response = requests.get(url)
img = Image.open(BytesIO(response.content))
