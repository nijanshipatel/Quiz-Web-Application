FROM python:3.10-slim

# Prevent prompts from apt
ENV DEBIAN_FRONTEND=noninteractive

# Set working directory in the container
WORKDIR /app

# Install system dependencies (optional but can help)
RUN apt-get update && apt-get install -y gcc libmariadb-dev && apt-get clean
# Copy all project files into the container
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
