FROM python:3.9-slim

# Установка зависимостей для psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev gcc

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DJANGO_SECRET_KEY=${SECRET_KEY}
ENV DJANGO_DEBUG=${DEBUG}
ENV DJANGO_ALLOWED_HOSTS=${ALLOWED_HOSTS}
ENV DATABASE_NAME=${DATABASE_NAME}
ENV DATABASE_USER=${DATABASE_USER}
ENV DATABASE_PASSWORD=${DATABASE_PASSWORD}
ENV DATABASE_HOST=${DATABASE_HOST}
ENV DATABASE_PORT=${DATABASE_PORT}

RUN python manage.py migrate --noinput
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
