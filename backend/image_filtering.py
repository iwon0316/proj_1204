import os
import cv2
import numpy as np
from pymongo import MongoClient
from gridfs import GridFS

# MongoDB 설정
mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(mongo_uri)
db = client["crop_disease"]
fs = GridFS(db)

# 이미지 필터링 함수
def filter_image(image_path):
    # 이미지 로드
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Could not load image at {image_path}")

    # 가우시안 블러 필터링
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

    # 샤프닝 필터 적용
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpened_image = cv2.filter2D(blurred_image, -1, kernel)

    # 캐니 엣지 감지 필터 적용
    edges = cv2.Canny(sharpened_image, 100, 200)

    # MongoDB에 저장
    _, buffer = cv2.imencode(".jpg", edges)
    fs.put(buffer.tobytes(), filename="filtered_image.jpg")

    # 필터링된 이미지 저장
    output_path = "/app/output_data/output_images/filtered_image.jpg"
    if not cv2.imwrite(output_path, edges):
        raise IOError(f"Could not save image to {output_path}")

    print(f"Filtered image saved at {output_path}")
    return edges

# 실행 부분
if __name__ == "__main__":
    # 환경 변수에서 입력 및 출력 경로 읽기
    input_path = os.getenv("IMAGE_INPUT_PATH", "/app/input_data/input_images/sample.jpg")
    output_path = os.getenv("IMAGE_OUTPUT_PATH", "/app/output_data/output_images/filtered_image.jpg")

    # 필터링 함수 호출
    filter_image(input_path)

