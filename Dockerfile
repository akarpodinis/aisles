FROM python:3.8.2-alpine3.11 AS base

FROM base AS build

RUN mkdir -p /opt/local
COPY requirements.txt /tmp/
RUN pip install --prefix=/opt/local --disable-pip-version-check --no-warn-script-location -r /tmp/requirements.txt

FROM base

COPY --from=build /opt/local /opt/local
COPY . .

ENV PATH=/opt/local/bin:$PATH \
    PYTHONPATH=/opt/local/lib/python3.8/site-packages \
    GUNICORN_CMD_ARGS=$GUNICORN_CMD_ARGS

RUN adduser -D myuser
USER myuser

CMD gunicorn -b 0.0.0.0:$PORT $GUNICORN_CMD_ARGS aisles:app
