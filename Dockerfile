FROM python:3.7.9-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /application
COPY requirements.txt /application/
RUN pip install -r requirements.txt
COPY . /application/
