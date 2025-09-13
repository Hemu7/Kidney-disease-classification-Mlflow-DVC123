# Use a supported base image
FROM python:3.8-slim-bullseye

# Install AWS CLI
RUN apt-get update -y && apt-get install -y awscli

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run your app
CMD ["python3", "app.py"]
