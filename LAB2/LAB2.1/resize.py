from PIL import Image
path = "C:/Users/VQ/Desktop/IE104-Internet and web technology/LAB2/originals/"
text = ["firefox_logo-only_RGB.png","firefox-addons.jpg","mozilla-dinosaur-head.png"]
panda = "red-panda.jpg"


def resizeimg(path,img,size):
    image = Image.open(path+img)
    if size == 400:
        new_image = image.resize((400, 300))
    else: 
        new_image = image.resize((120, 90))

    t = "firefox_logo-only_RGB.png"
    d = "firefox-addons.jpg"
    m = "mozilla-dinosaur-head.png"
    r = "red-panda.jpg"
    if img == t:
        img = "firefox_logo"
    elif img == d:
        img = "firefox-addons"
    elif img ==m:
        img = "mozilla-dinosaur"
    new_image.save(path+img+str(size)+'.png')

d = 0
# for i in text:
#     if d<=1:
#         d+=1 
#         continue
#     resizeimg(path,i,400)
#     resizeimg(path,i,120)
#     d+=1

img = "red-panda.jpg"
t = "red-panda"
image = Image.open(path+img)
new_image = image.resize((1200, 485))
new_image.save(path+t+"-landscape"+'.jpg')
new_image1 = image.resize((600, 243))
new_image1.save(path+t+"-potrait-small"+'.jpg')

