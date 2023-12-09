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

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=33001, reload=True)
