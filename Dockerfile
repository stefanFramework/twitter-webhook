FROM python:3.11.8

WORKDIR /app

# Copy the current directory (.), into a container in /app
COPY ./app /app

# Runs the first command, INSIDE the container --> WORKDIR app/requirements ...
RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python3","main.py"]

EXPOSE 80