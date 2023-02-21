FROM python:3.11-slim
ENV PYTHONBUFFER=1
RUN mkdir G:/django-channels/code

WORKDIR G:/django-channels/code
ADD . G:/django-channels/code
# COPY requirements.txt .

RUN pip install -r requirements.txt


# COPY . .
EXPOSE 8000

# CMD [ "python", "manage.py", "runserver"]
CMD python manage.py runserver 0:8000
