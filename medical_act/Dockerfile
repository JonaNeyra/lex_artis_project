FROM python:3.10-alpine
LABEL maintainer="neyranievesjonathan@gamial.com"

ENV PYTHONBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY . /medical_act/

WORKDIR /medical_act

EXPOSE 50051

RUN python -m venv /py && \
    /py/bin/pip install --no-cache-dir --upgrade pip && \
    apk add --no-cache --virtual .build-deps \
        gcc \
        g++ \
        libc-dev \
        linux-headers \
        libffi-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    apk del .build-deps && \
    rm -rf /var/cache/apk/* && \
    rm -Rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        ritual-user

ENV PATH="/py/bin/:$PATH"

USER ritual-user

CMD ["python", "src/handler.py"]