# Use official Python base image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy local code into the container
COPY . .

# Install system dependencies for Streamlit + LangChain
RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Set environment variables (optional if using .env)
ENV PYTHONUNBUFFERED=1

# Expose the port used by Streamlit
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
