FROM python:3.9

RUN apt-get update 
RUN apt install -y libev-dev libevdev2

WORKDIR /app

COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY . /app

CMD bash