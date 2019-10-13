from PIL import Image, ImageFont, ImageDraw


def tupianchongdie(a,b):
    im = Image.open(a)
    im1 = Image.open(b)
    im1.paste(im, (200, 200))
    im1.show()
    im1.save('var/www/lee/zhouxinyuan00/static/txudingzhi201708/image/D.png')

    return


tupianchongdie('a.png','b.png')