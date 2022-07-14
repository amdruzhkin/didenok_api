FROM python:3.9.0
WORKDIR /didenok_api
COPY ./requirements.txt /didenok_api
RUN pip install -r requirements.txt
COPY . /didenok_api
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]