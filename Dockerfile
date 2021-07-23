FROM python:3.8

WORKDIR /townonewheel/

COPY requirements.txt /townonewheel/

RUN pip install --no-compile --no-cache-dir --upgrade pip \
    pip install --no-compile --no-cache-dir -r requirements.txt
