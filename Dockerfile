# Use the official Python image.
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy app files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV PORT=8080

# Run the app with gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
