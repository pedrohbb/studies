import zipfile as zf
from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np

# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')

# the rest is up to you!

def words_detector(img, word):
    img_array = np.array(img.convert('L'))
    txt = pytesseract.image_to_string(img_array)
    if word in txt:
        return True
    return False

def faces_selector(img):
    faces_coord = face_cascade.detectMultiScale(np.array(img),1.3,5)
    faces = []
    for x,y,w,h in faces_coord:
        face = img.crop((x,y,x+w,y+h))
        faces.append(face)
    return faces


def contsheet_generator(faces):
    contact_sheet = Image.new('RGB', (500,100*(1 + int(len(faces)/5))))
    x = 0
    y = 0
    for face in faces:
        face.thumbnail((100,100))
        contact_sheet.paste(face,(x, y))
        if x+100 == contact_sheet.width:
            x=0
            y=y+100
        else:
            x=x+100
    
    return contact_sheet

    
def extract_imgs(archive_name):
    file_zip = zf.ZipFile(archive_name)
    namelist = file_zip.namelist()
    images = dict()
    for name in namelist:
        images[name] = Image.open(file_zip.open(name))
        
    return images
    
    
def main():
    a = 'readonly/small_img.zip'
    b = 'images.zip'
    words = ["Christopher", "Mark"]
    files = [extract_imgs(a), extract_imgs(b)]
    searchs = list(zip(words,files))
    for search in searchs:
        images = search[1]
        for key in images:
            if words_detector(images[key], search[0]):  
                print(f'{search[0]} found in {key}! Results:')
                faces = faces_selector(images[key]) 
                if len(faces) > 0:
                    display(contsheet_generator(faces))
                else:
                    print(f'no faces in {key}')
            else:
                print(f'{search[0]} not found in {key}!\n')
       
    
main() 