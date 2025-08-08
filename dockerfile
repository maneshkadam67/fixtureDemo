# Use official Python image
FROM python:3.11-slim

# Set work directory inside container
WORKDIR /app

# Copy only requirements first to cache dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files (like testcases/)
COPY . .

# Set environment variables (optional)
ENV PYTHONUNBUFFERED=1

# Run pytest by default when container starts
CMD ["pytest", "testcases/", "--html=reports/report.html", "--self-contained-html"]
