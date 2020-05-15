import urllib
from urllib.request import urlopen, Request
import time


def convert(text,targetPath,targetName,gender="female"):
    if(gender.lower()=="male"):
        voice = "en-US_MichaelV3Voice"
    else:
        voice = "en-US_AllisonV3Voice"

    url = "https://text-to-speech-demo.ng.bluemix.net/api/v3/synthesize?text="+urllib.parse.quote(text.strip().replace("\n","."))+"&voice="+voice+"&download=true&accept=audio%2Fmp3"
    try:
        urllib.request.urlretrieve(url, targetPath+'/'+targetName+'.mp3'.replace("\\","/").replace("//","/"))
    except:
        time.sleep(5)
        urllib.request.urlretrieve(url, targetPath + '/' + targetName + '.mp3'.replace("\\", "/").replace("//", "/"))
    return targetPath+'/'+targetName+'.mp3'.replace("\\","/").replace("//","/")
