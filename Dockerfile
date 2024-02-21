# Base image with Python 3.12.1
FROM python:3.12.1-slim

# Set working directory
WORKDIR /issea-enquete-app

# Install dependencies (replace with your requirements)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install other necessary packages (e.g., database adapter)

# Copy remaining project files
COPY ./src .

# Expose Django development server port
EXPOSE 8000

# Start Django development server
CMD ["python", "./src/manage.py", "runserver", "0.0.0.0:8000"]
