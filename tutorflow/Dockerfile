FROM python:3.8

RUN docker system df \
    && docker system prune --force

ENV PYTHONUNBUFFERED 1
WORKDIR /backend
COPY requirements.txt /backend/

RUN python3 -m venv env \
    && . env/bin/activate \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install gunicorn

COPY . /backend/

RUN python3 manage.py makemigrations \
    && python3 manage.py migrate

ENV DJANGO_SETTINGS_MODULE=tutorflow.settings
EXPOSE 8000
CMD ["gunicorn", "tutorflow.wsgi:application", "--bind", "0.0.0.0:8000"]


# FROM python:3.8

# RUN docker system df
# RUN docker system prune

# ENV PYTHONUNBUFFERED 1
# WORKDIR /backend
# COPY requirements.txt /backend

# RUN python3 -m venv env
# RUN source env/bin/activate

# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt
# RUN pip install gunicorn

# COPY . /backend/

# RUN python3 manage.py makemigrations
# RUN python3 manage.py migrate

# ENV DJANGO_SETTINGS_MODULE=tutorflow.settings
# EXPOSE 8000
# CMD ["gunicorn", "tutorflow.wsgi:application", "--bind", "0.0.0.0:8000"]

# # CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]

# # RUN pip install --trusted-host pypi.python.org -r requirements.txt