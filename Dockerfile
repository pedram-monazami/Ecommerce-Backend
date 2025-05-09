FROM python:3.9.17-alpine3.17


LABEL Author="Mehdi Shahidi"


ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DJANGO_SUPERUSER_PASSWORD root

WORKDIR /ecommerce

RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY . /ecommerce

#
#
#CMD while ! python3 manage.py sqlflush > /dev/null 2>&1 ; do sleep 1; done && \
#	python3 manage.py makemigrations --noinput && \
#	python3 manage.py migrate --noinput && \
##	python3 manage.py collectstatic --noinput && \
#	python3 manage.py createsuperuser --noinput --phone root --email root@root.com; \
#	gunicorn -b 0.0.0.0:8000 ecommerce.wsgi