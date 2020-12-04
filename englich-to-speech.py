from gtts import gTTS
import os

myfile = open('source.txt', 'r')
myInput = myfile.read()
language = 'en'
result = gTTS(text=myInput , lang=language, slow=False)

result.save("translate.mp3")
myfile.close()