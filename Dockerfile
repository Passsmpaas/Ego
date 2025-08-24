# Use Python slim image (better performance & prebuilt packages)
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install only required system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg aria2 unzip wget curl ca-certificates tzdata \
    && rm -rf /var/lib/apt/lists/*

# Download prebuilt Bento4 mp4decrypt binary (no source compilation)
RUN wget -q https://github.com/axiomatic-systems/Bento4/releases/download/v1.6.0-639/mp4decrypt -O /usr/local/bin/mp4decrypt \
    && chmod +x /usr/local/bin/mp4decrypt

# Copy all project files
COPY . .

# Upgrade pip and install Python dependencies
RUN pip3 install --no-cache-dir --upgrade pip \
    && pip3 install --no-cache-dir -r sainibots.txt \
    && pip3 install --no-cache-dir -U yt-dlp

# Optional: Set timezone (adjust if needed)
ENV TZ=Asia/Kolkata

# Default command to run the application
CMD ["sh", "-c", "gunicorn app:app & python3 main.py"]
