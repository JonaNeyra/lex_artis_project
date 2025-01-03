FROM python:3.10-alpine
LABEL maintainer="neyranievesjonathan@gamial.com"

ENV PYTHONBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY . /medical_act/

WORKDIR /medical_act

EXPOSE 50051

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache \
        build-base \
        g++ \
        gcc \
        libc-dev \
        linux-headers \
        libffi-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -Rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        ritual-user

ENV PATH="/py/bin/:$PATH"

USER ritual-user

CMD ["python", "src/handler.py"]