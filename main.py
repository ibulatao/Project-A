from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI file upload example!"}

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    # You can also save the files to disk or process them as needed
    with open(f"temp_{file.filename}", "wb") as f:
        f.write(contents)

    return JSONResponse(content={
        "filename": file.filename,
        "content_type": file.content_type,
        "size": round(len(contents) / 1024, 2), #size in KB
        "message": "File uploaded successfully!"
    })