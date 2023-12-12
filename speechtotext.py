import speech_recognition as sr
import sys #-- 텍스트 저장시 사용
import os
from main import name

#name = 'd5b409cde76753b0c87a'
r = sr.Recognizer()
kr_audio = sr.AudioFile(f'./{name}.wav')

with kr_audio as source:
    audio = r.record(source)

sys.stdout = open(f'{name}_out.txt', 'w') #-- 텍스트 저장시 사용
print(r.recognize_google(audio, language='ko-KR')) #-- 한글 언어 사용
sys.stdout.close() #-- 텍스트 저장시 사용