FROM python:3.8
LABEL MAINTIANER="SHAHRAM dOCKER | ZCFCO.IR"

ENV PYTHONNONEBUFFRED 1

RUN mkdir /blogfy
WORKDIR /blogfy

COPY . /blogfy

ADD requirements/requirements.txt /blogfy
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "--chdir", "blogfy", "--bind", ":8000", "blogfy.wsgi:application"]

