import image

img = image.Image("cy.png")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
#img.setDelay(1,15)   # setDelay(0) turns off animation

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        newred = 255 - p.getRed()
        newgreen = 0
        newblue = 0

        newpixel = image.Pixel(newred, newgreen, newblue)

        img.setPixel(col, row, newpixel)

    img.draw(win)
win.exitonclick()
