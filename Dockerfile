# Use Python 3.10 base image to match your version
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Install system dependencies for Selenium and Chrome with retry logic
RUN echo "deb http://httpredir.debian.org/debian trixie main" > /etc/apt/sources.list && \
    apt-get update && \
    for i in 1 2 3; do apt-get install -y wget unzip curl gnupg2 && break || sleep 5; done && \
    mkdir -p /etc/apt/keyrings && \
    curl -sSL https://dl.google.com/linux/linux_signing_key.pub -o /etc/apt/keyrings/google-chrome.asc && \
    echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/google-chrome.asc] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    for i in 1 2 3; do apt-get install -y google-chrome-stable && break || sleep 5; done && \
    wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/139.0.7258.128/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ && \
    rm /tmp/chromedriver.zip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt and install Python libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY app.py .

# Run the script when the container starts
ENTRYPOINT ["python", "app.py"]