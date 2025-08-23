FROM python:3.9-alpine

WORKDIR /app

COPY . .

RUN apk add --no-cache \
    gcc \
    libffi-dev \
    musl-dev \
    ffmpeg \
    aria2 \
    make \
    g++ \
    cmake \
    unzip \
    build-base \
    linux-headers && \
    wget -q https://github.com/axiomatic-systems/Bento4/archive/v1.6.0-639.zip && \
    unzip v1.6.0-639.zip && \
    cd Bento4-1.6.0-639 && \
    mkdir build && cd build && cmake .. && make -j$(nproc) && \
    cp mp4decrypt /usr/local/bin/ && cd ../.. && rm -rf Bento4-1.6.0-639 v1.6.0-639.zip

RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir --upgrade -r sainibots.txt && \
    python3 -m pip install -U yt-dlp gunicorn

CMD ["sh", "-c", "gunicorn app:app & exec python3 main.py"]
