# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy backend code and requirements
COPY ./backend /app
COPY requirements.txt /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Command to run FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
