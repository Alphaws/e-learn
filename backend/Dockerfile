FROM python:3.12 AS backend
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY backend .
RUN pip install -r /app/requirements.txt
EXPOSE 8000
