FROM python:3.8.17

WORKDIR /talmoapi

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . /talmoapi

EXPOSE 1542

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "1542"]