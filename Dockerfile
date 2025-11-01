# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements file *first* to leverage Docker cache
# (I'm assuming your file is named 'requirements.txt')
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code (e.g., app.py)
COPY . .

# Expose the port your app runs on (from our app.py)
EXPOSE 5000

# Define the command to run your app
CMD ["python", "app.py"]
