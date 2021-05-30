from PIL import Image, ImageFilter, ImageDraw, ImageFont
import numpy as np
python = Image.open("Python.png")
print(python)
python.show()
python.save("Python.bmp")
bmp = Image.open("Python.bmp")
bmp.show()
goprogram = Image.open("GoProgram.png")
goprogram.show()
print(python.size)
print(goprogram.size)
python.thumbnail((200,200))
goprogram.thumbnail((200,200))
python.show()
goprogram.show()
python = python.transpose(Image.ROTATE_90)
goprogram = goprogram.transpose(Image.ROTATE_270)
merge = Image.new("RGBA", (400,200))
merge.paste(python,(0,0))
merge.paste(goprogram,(200,0))
merge = merge.transpose(Image.FLIP_TOP_BOTTOM)
merge.show()

goprogram = goprogram.resize((500,500))
crop = goprogram.crop((100,100,goprogram.size[0]-100,goprogram.size[1]-100))
crop.show()

cat = Image.open("cat.jpeg")
cat.show()
cat.filter(ImageFilter.MaxFilter).show()
filters = ["BLUR", "CONTOUR", "DETAIL", "EDGE_ENHANCE", "EDGE_ENHANCE_MORE", "EMBOSS", "FIND_EDGES", "SMOOTH", "SMOOTH_MORE", "SHARPEN"]
for filter in filters:
    input(filter)
    cat.filter(eval(f"ImageFilter.{filter}")).show()

array = np.array(cat)
array = 255 - array
# array += 128
cat = Image.fromarray(array)
cat.show()

draw = ImageDraw.Draw(cat)
font = ImageFont.truetype("OpenSans.ttf",50)
draw.text((cat.size[0]//2,0),"Cat",align="center",font=font,fill=(0,0,0))
cat.show()