import PIL
from PIL import Image
from PIL import ImageEnhance, ImageDraw, ImageFont

# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')

#set font
ft = ImageFont.truetype('readonly/fanwood-webfont.ttf', 35)

images = []

channel_int = [0.1,0.5,0.9]

def labeler(img, strg, font, color):
    #creates a background to enter the phrase
    background = Image.new('RGB', (img.width,40), color=(0,0,0))
    draw_space = ImageDraw.Draw(background)
    #inscribe the phrase
    draw_space.text((10,0), text=strg, font=font, fill=color)
    sheet = Image.new(img.mode, (img.width, img.height + background.height))
    sheet.paste(background, (0,img.height))
    sheet.paste(img,(0,0))
    return sheet
    

for i in channel_int:
    #modifies the desired channel
    r, g, b = image.split()
    r = r.point(lambda x: x*i)
    img = Image.merge('RGB', (r,g,b))
    nice_color = img.getpixel((0,50))
    img_labeled = labeler(img, 'channel 0 intensity {}'.format(i), ft, nice_color)
    images.append(img_labeled)

for i in channel_int:
    #modifies the desired channel
    r, g, b = image.split()
    g = g.point(lambda x: x*i)
    img = Image.merge('RGB', (r,g,b))
    nice_color = img.getpixel((0,50))
    img_labeled = labeler(img, 'channel 1 intensity {}'.format(i), ft, nice_color)
    images.append(img_labeled)

for i in channel_int:
    #modifies the desired channel
    r, g, b = image.split()
    b = b.point(lambda x: x*i)
    img = Image.merge('RGB', (r,g,b))
    nice_color = img.getpixel((0,50))
    img_labeled = labeler(img, 'channel 2 intensity {}'.format(i), ft, nice_color)
    images.append(img_labeled)


# build a list of 9 images which have different brightnesses

#for i in range(9):
#    enhancer = ImageEnhance.Brightness(images[i])
#    images[i] = enhancer.enhance((i+1)/10)
    
# create a contact sheet from different brightnesses
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

        
for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)
contact_sheet.save('assignment_1.jpg')