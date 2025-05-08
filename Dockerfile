FROM python:3.12-bookworm

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt into the container at /app/requirements.txt
COPY requirements_freeze.txt requirements.txt

# Upgrade pip
RUN pip install --upgrade pip

# Install pip packages
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY .secrets/secrets.toml  ./.secrets/secrets.toml
COPY src/ ./src/

# Command to run
CMD ["uvicorn", "src.main:app", "--host 0.0.0.0", "--port 9770"]