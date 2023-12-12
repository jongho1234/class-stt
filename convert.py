from pydub import AudioSegment
from main import fileExtension_list,name,extension
import os

# files



if(extension == '.mp3') :
    # convert wav to mp3
    audSeg = AudioSegment.from_mp3(f"{name}{extension}")
    audSeg.export(f"{name}.wav", format="wav")
    os.remove(f'{name}{extension}')
