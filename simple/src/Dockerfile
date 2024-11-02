# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the app.py file into the container
COPY app.py /app

# Install Flask
RUN pip install flask

# Expose port 5000 to the outside world
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]

