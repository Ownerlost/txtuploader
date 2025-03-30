# Use a lightweight Python image
FROM python:3.9.6-alpine3.14

# Set working directory
WORKDIR /app

# Copy all files into the container
COPY . .

# Install required dependencies
RUN apk add --no-cache gcc libffi-dev musl-dev ffmpeg aria2 \
    && pip install --no-cache-dir -r requirements.txt

# Expose the port for Flask (if applicable)
EXPOSE 8080

# Run both Gunicorn (Flask) and the Telegram bot correctly
CMD sh -c "gunicorn --bind 0.0.0.0:8080 app:app & python3 modules/main.py"
