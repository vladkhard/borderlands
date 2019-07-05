FROM python:3.7

RUN mkdir /opt/app
WORKDIR /opt/app

COPY ./requirements.txt /opt/app/requirements.txt
RUN pip install -r requirements.txt

COPY ./application /opt/app/application
COPY ./borderlands /opt/app/borderlands
COPY ./manage.py /opt/app/manage.py

CMD python manage.py migrate --run-syncdb; python manage.py runserver 0.0.0.0:8000
