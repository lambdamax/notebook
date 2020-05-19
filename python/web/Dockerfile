FROM python:3.7

WORKDIR /www

COPY ./ .

RUN set -x; \
    pip install flask

EXPOSE 9090

CMD ["python", "app.py"]

