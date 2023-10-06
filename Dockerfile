# Use a Python base image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy your game files into the container
COPY . /app

# Install any dependencies (if needed)
# For example, if you have a requirements.txt file:
RUN pip install -r requirements.txt

# Expose the necessary port (if your game has a server)
# EXPOSE 8080

# Command to run your game
CMD ["python", "main.py"]
