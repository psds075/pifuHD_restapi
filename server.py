from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from pydantic import BaseModel
import prediction

class FileUpload(BaseModel):
    file: UploadFile

app = FastAPI()

@app.get("/")
def status():
    return {"message" : "success"}

@app.post("/")
async def upload(file: UploadFile = File(...)):
    content = await file.read()
    with open("input/input.png", "wb") as fp:
        fp.write(content)
        
    prediction.prediction()
        
    print("success")

    return FileResponse("output/pifuhd_final/recon/result_input_256.obj", filename = "result.obj")


import uvicorn
import sys
import os

port = 33001
debug = True
if(len(sys.argv) > 1):
    port = int(sys.argv[1])
if(len(sys.argv) > 2):
    if(sys.argv[2] == "False"):
        import logging
        debug = False 
        logging.basicConfig(filename='server.log',level=logging.DEBUG)

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=port, reload=debug)

