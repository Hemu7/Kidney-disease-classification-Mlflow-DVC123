FROM python:3.8-slim-bullseye

# Install system dependencies
RUN apt-get update -y && apt-get install -y awscli

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Upgrade pip tools
RUN pip install --upgrade pip setuptools wheel

# Install dependencies (from requirements.txt, without -e .)
RUN pip install --no-cache-dir -r requirements.txt

# Install your local package (cnnClassifier) in editable mode
RUN pip install -e .

# Run your app
CMD ["python3", "app.py"]
