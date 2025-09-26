# Use Python 3.8 as base image
FROM python:3.8-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
