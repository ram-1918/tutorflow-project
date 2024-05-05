FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /backend
COPY requirements.txt /backend

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY . /backend/
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
ENV DJANGO_SETTINGS_MODULE=tutorbackend.settings
EXPOSE 8000
CMD ["gunicorn", "tutorbackend.wsgi:application", "--bind", "0.0.0.0:8000"]

# CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]

# RUN pip install --trusted-host pypi.python.org -r requirements.txt