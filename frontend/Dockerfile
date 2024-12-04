# Node.js 이미지를 기반으로 설정
FROM node:16

# 작업 디렉토리 설정
WORKDIR /app

# package.json과 package-lock.json을 먼저 복사하여 의존성 설치
COPY package*.json ./

# npm install 실행
RUN npm install

# 애플리케이션 코드 복사
COPY ./src ./src
COPY ./public ./public

# React 애플리케이션 빌드
RUN npm run build

# React 애플리케이션을 배포용으로 실행 (개발 서버 대신)
RUN npm install -g serve
CMD ["serve", "-s", "build"]

# React 서버 포트 열기
EXPOSE 3000
