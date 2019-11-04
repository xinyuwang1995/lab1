FROM python:3.6.7
WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt && python manage_prod.py collectstatic --noinput

EXPOSE 8004

CMD ["uwsgi","--ini","django_uwsgi.ini"]