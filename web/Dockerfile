FROM python:3.6

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

CMD python manage.py collectstatic --noinput

COPY . /usr/src/app