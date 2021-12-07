FROM python:3
ENV PYTHONUNBUFFERED=1
COPY ./ /backend/
WORKDIR /backend

RUN pip install -r requirements/local.txt
