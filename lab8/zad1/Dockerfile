FROM python:3-slim

EXPOSE 8080

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

COPY app/requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY ./app /app


CMD ["python", "app.py"]
