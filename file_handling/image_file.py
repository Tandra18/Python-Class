from PIL import Image
# pip install pillow
import io

with open(r'D:\apple.jpg','rb') as img_file:
    img_data = img_file.read()

image = Image.open(io.BytesIO(img_data))
image.show()



