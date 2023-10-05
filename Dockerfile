FROM ubuntu

# Set the working directory
WORKDIR /app

# Copy requirements.txt and SpaceShip-Game into the container
COPY requirements.txt SpaceShip-Game /app/

# Update and install dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    python3 -m venv venv && \
    . venv/bin/activate && \
    pip install -r requirements.txt

# Change the working directory to SpaceShip-Game
WORKDIR /app/SpaceShip-Game

# Define the CMD instruction
CMD ["python3", "main.py", "runserver", "0.0.0.0:8800"]
