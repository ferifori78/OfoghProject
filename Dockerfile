FROM python:3.9
LABEL MAINTAINER="feri fori | https://github.com/ferifori78"

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
COPY . /app

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
#
EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=rsm.settings

CMD ["gunicorn", "--chdir", "config", "--bind", ":8000", "intender.intender.wsgi:application"]