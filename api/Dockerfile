FROM python:3.10-slim-buster

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY src /app/src

CMD ["python3", "/app/src/main.py"]