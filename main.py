from PIL import Image
import math


def image_size_reducer(image_location,img_quality:int=35)
    foo = Image.open(image_location)
    x, y = foo.size
    x2, y2 = math.floor(x-50), math.floor(y-20)
    foo = foo.resize((x2,y2),Image.ANTIALIAS)
    foo.save("out_"+image_location,quality=quality,optimize=True)

image_size_reducer('test.png')
