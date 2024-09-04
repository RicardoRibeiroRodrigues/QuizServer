FROM python:slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN python3 src/create_db.py && python3 src/adduser.py
ENV FLASK_APP=/app/src/softdes
EXPOSE 8080

ENTRYPOINT ["flask", "run", "--host=0.0.0.0", "--port=8080"]