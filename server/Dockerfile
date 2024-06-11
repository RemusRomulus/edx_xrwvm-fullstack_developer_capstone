from python:3.12.0-slim-bookworm

ENV PYTHONBUFFERED 1
ENV PYTHONWRITEBYTECODE 1

ENV APP=/app

# Set Working Directory
WORKDIR $APP

# Install Requirements
COPY requirements.txt $APP
RUN pip3 install -r requirements.txt

# Copy Application Files
COPY . $APP

# Expose the Port
EXPOSE 8000

# Start the Application
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/bin/bash","/app/entrypoint.sh"]
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangoproj.wsgi"]
