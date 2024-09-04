FROM python:slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN python3 src/create_db.py
RUN python3 src/adduser.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]