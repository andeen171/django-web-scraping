# Transient Node Build Image
FROM node:lts-alpine3.15
WORKDIR /app
COPY .npmrc package.json yarn.lock webpack.config.js .babelrc /app/
RUN yarn install

# Python Runtime Image
FROM python:3.10-alpine3.15

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies & setup user
RUN adduser -D appuser && \
    apk add --no-cache --virtual .build-deps g++ gcc libffi-dev musl-dev libevent-dev openssl-dev python3-dev make && \
    apk add --no-cache git postgresql-dev binutils && \
    apk add --no-cache jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev && \
    apk add --no-cache yarn

# Copy requirements
COPY requirements.txt .

RUN pip install -U pip && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del --no-cache .build-deps

# Copy node_modules and yarn
COPY --from=0 /app/node_modules /app/node_modules