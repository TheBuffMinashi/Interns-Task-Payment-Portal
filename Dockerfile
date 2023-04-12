FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
#RUN ./manage.py makemigrations --noinput
#RUN ./manage.py migrate --noinput
#RUN ./manage.py createsuperuser --email 'admin@test.com' --noinput