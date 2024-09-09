# Python 3.10.11 slim 버전 사용
FROM python:3.10.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# MySQL 관련 라이브러리 및 pkg-config 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    libmariadb-dev \
    pkg-config

# 필요 라이브러리 설치를 위한 패키지 복사
COPY resource_src/Pipfile resource_src/Pipfile.lock ./

# pipenv 설치
RUN pip install pipenv

# Python 버전 확인 및 패키지 설치
RUN python --version
RUN pipenv --python /usr/local/bin/python3.10 install --deploy --ignore-pipfile

# 소스 코드 복사
COPY resource_src/ /app

# 포트 개방
EXPOSE 9999

# 개발 서버 실행
CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:9999"]
