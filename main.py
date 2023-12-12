from fastapi import FastAPI,UploadFile,File
from fastapi.responses import FileResponse
from fastapi.responses import PlainTextResponse
from secrets import token_hex
from konlpy.tag import Kkma
import uvicorn
import os

mainfilename = "fde3eb127a09c59fa24e_text"
file_list = os.listdir('./')
fileExtension_list = ['.mp3','.wav']
app = FastAPI(title="수업 글 요약 파일 올리기!")



@app.get("/")
def mainpage() :
    return '127.0.0.1:8000/docs 로 이동해주세요!!!'

@app.post("/upload")
async def upload(file:UploadFile = File(...)) :
    file_ext = file.filename.split(".").pop()
    file_name = token_hex(10)
    file_path = f"{file_name}.{file_ext}"
    with open(file_path,"wb") as f:
        content = await file.read()
        f.write(content)
    global name, extension
    name,extension = os.path.splitext(file_path)
    
    if(extension not in fileExtension_list) :
        os.remove(f'{name}{extension}')
        
        return {f"{name}{extension} 은 잘못된 파일 형식입니다."}
    
    
    import convert
    import speechtotext
    import summary
    
    return FileResponse(path=f"{name}_text.txt",media_type="application/octet-stream",filename=f"{name}_text.txt")

if __name__ == "__main__" :
    uvicorn.run("main:app",host="127.0.0.1",reload=True)