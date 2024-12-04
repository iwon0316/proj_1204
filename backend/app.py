from fastapi import FastAPI, File, UploadFile
import uvicorn
from image_filtering import filter_image

app = FastAPI()

# 업로드 파일 저장
@app.post("/filter/")
async def filter_uploaded_image(file: UploadFile = File(...)):
    upload_path = f"/app/input_data/{file.filename}"
    with open(upload_path, "wb") as f:
        f.write(await file.read())

    # 필터링 처리
    try:
        filtered_image = filter_image(upload_path)
        output_path = "/app/output_data/output_images/filtered_image.jpg"
        return {"message": f"Image filtered and saved at {output_path}"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
