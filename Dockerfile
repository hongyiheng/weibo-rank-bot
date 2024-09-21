# Stage 1: Build stage
FROM python:3.10-slim AS builder

# Set up virtual environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy only requirements.txt first to leverage Docker cache
COPY requirements.txt /app/requirements.txt

# Install dependencies in the virtual environment
WORKDIR /app
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Stage 2: Final stage
FROM gcr.io/distroless/python3-debian10

# Copy the virtual environment and app from the builder stage
COPY --from=builder /opt/venv /opt/venv
COPY --from=builder /app /app

# Ensure the virtual environment is used
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PYTHONPATH /app

# Set the working directory and default command
WORKDIR /app
CMD ["python", "/app/main.py"]
