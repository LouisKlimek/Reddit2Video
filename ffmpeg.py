import subprocess
import os
from mutagen.mp3 import MP3


def videoFromImage(imgFilePath, outputFilepath, videoDurationinSeconds):
    subprocess.call(
        ['ffmpeg', '-r', '1/' + str(videoDurationinSeconds), '-i', imgFilePath, '-c:v', 'libx264', '-r', '1',
         '-pix_fmt', 'yuv420p', outputFilepath])


def overlayText(videoFilepath, text, fontsize, fontName, fontcolor, outputFilepath,xCord,yCord):
    #subprocess.call(["""ffmpeg""", """-i""", videoFilepath, """-vf""", """ "drawtext=fontfile=medium.ttf:""", """text='"""+text+"""':""", """fontcolor="""+fontcolor+""":""", """fontsize="""+str(fontsize)+""":""", """x="""+str(xCord)+""":y="""+str(yCord)+""":" """, """-codec:a""", """copy""", outputFilepath])
    os.system("""ffmpeg -y -i """+videoFilepath+""" -vf "drawtext=fontfile="""+fontName+""": text='"""+text+"""': fontcolor="""+fontcolor+""": fontsize="""+str(fontsize)+""": x="""+str(xCord)+""":y="""+str(yCord)+""":" -codec:a copy """+outputFilepath)

def combineAudioWithVideo(audioFilepath,videoFilepath,outputFilepath):
    os.system("""ffmpeg -i """+videoFilepath+""" -i """+audioFilepath+""" -acodec copy -c:v copy -c:a aac -strict experimental """+outputFilepath)

def addAudioToVideo(audioFilepath,videoFilepath,outputFilepath):
    os.system("""ffmpeg -i """+videoFilepath+""" -i """+audioFilepath+""" -filter_complex "[0:a][1:a]amerge=inputs=2[a]" -map 0:v -map "[a]" -c:v copy -c:a libvorbis -ac 2 """+outputFilepath)

def concatVideos(video1Filepath,video2Filepath,outputFilepath):
    os.system('ffmpeg -i '+video1Filepath+' -i '+video2Filepath+' -b:a 320k -vsync 2 -filter_complex concat=n=2:v=1:a=1 -f MOV -y '+outputFilepath)
    #os.system('ffmpeg -y -i '+video1Filepath+' -i '+video2Filepath+' -vsync 2 -filter_complex "[0:v] [0:a] [1:v] [1:a] concat=n=2:v=1:a=1 [v] [a]" -map "[v]" -map "[a]" '+outputFilepath)

def addImageToVideo(videoFilepath,imageFilepath,xCord,yCord,outputFilepath):
    os.system("""ffmpeg -i """+videoFilepath+""" -i """+imageFilepath+""" -filter_complex "overlay="""+str(xCord)+""":"""+str(yCord)+"""" """+outputFilepath)

def getFileLength(filePath):
    audio = MP3(filePath.replace('\\', "/"))
    duration = audio.info.length
    return duration


def splitTextIntoLineArray(text, maxLineLength):
    lines = [""]
    index = 0
    for word in text.strip().split(" "):
        if len(lines[index]) >= maxLineLength or word[:2] == "\n":
            index = index + 1
            lines.append("")

        lines[index] = lines[index] + word.replace("\n"," ").replace("'","’").replace("\'","’").replace('"'," ").replace(":","ː").replace("  "," ").replace("  "," ").replace("  "," ") + " "

    return lines