FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies directly here
RUN pip install --no-cache-dir flask pytest

# Copy app code
COPY . .

# Expose port
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]