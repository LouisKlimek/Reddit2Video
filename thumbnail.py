import random
import string
from nltk.corpus import stopwords
from textblob import TextBlob
import requests

def randomString(stringLength):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def stripFirstLast(data):
    return data[1:-1]

def create(title):
    title = title.replace("EU ","European Union")

    keywords = [word for word in title.split(" ") if word not in stopwords.words('english')]
    keywords = ' '.join(keywords)
    blob = TextBlob(keywords)
    keywords = blob.noun_phrases
    keywords = stripFirstLast(stripFirstLast(str(keywords))).split(" ")

    imageURL = ""

    while len(keywords)>0:
        randomNumber = random.randint(0,len(keywords)-1)
        keyword = keywords[randomNumber]

        url = "https://api.unsplash.com/search/photos?page=1&query="+keyword+"&client_id=CLIENTID"
        resp = requests.get(url=url)
        jsonData = resp.json()
        if len(jsonData["results"])<1:
            keywords.pop(randomNumber)
            continue
        else:
            imageURL = jsonData["results"][0]
            break

    return imageURL


def combineImages(image1Path,image2Path,outputpath):
    import os
    from PIL import Image

    files = [image1Path,image2Path]

    result = Image.new("RGB", (800, 800))

    for index, file in enumerate(files):
        path = os.path.expanduser(file)
        img = Image.open(path)
        img.thumbnail((400, 400), Image.ANTIALIAS)
        x = index // 2 * 400
        y = index % 2 * 400
        w, h = img.size
        print('pos {0},{1} size {2},{3}'.format(x, y, w, h))
        result.paste(img, (x, y, x + w, y + h))

    result.save(os.path.expanduser(outputpath))