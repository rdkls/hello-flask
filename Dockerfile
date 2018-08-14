FROM alpine:3.7
EXPOSE 80

RUN apk add --update \
        python \
        curl \
        py-pip
RUN pip install virtualenv

WORKDIR /app

RUN virtualenv .venv
COPY requirements.txt .
RUN . .venv/bin/activate && pip install -r requirements.txt

COPY . /app/
CMD ["/app/.venv/bin/python", "app.py"]
