import shutil
import requests

my_url = 'https://www.washingtonian.com/wp-content/uploads/2017/06/6-30-17-goat-yoga-congressional-cemetery-1-994x559.jpg'
response = requests.get(my_url, stream=True)
with open('my_image.png', 'wb') as file:
    shutil.copyfileobj(response.raw, file)
del response
from PIL import Image

img = Image.open('my_image.png')
img.show()
