FROM alpine:3.4

RUN apk add --update make python py-pip && \
    pip install --upgrade pip

COPY requirements.* /tmp/

RUN pip install -r /tmp/requirements.txt && \
    pip install -r /tmp/requirements.dev && \
    rm /tmp/requirements.*
