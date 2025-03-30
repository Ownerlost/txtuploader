# Use a lightweight Python image
FROM python:3.9.6-alpine3.14

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN apk add --no-cache gcc libffi-dev musl-dev ffmpeg aria2 \
    && pip install --no-cache-dir -r requirements.txt

# Expose Flask app port
EXPOSE 8080

# Start both Gunicorn and Telegram bot using a shell
CMD sh -c "gunicorn --bind 0.0.0.0:8080 app:app & python3 ./main.py"
