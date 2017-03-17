FROM resin/rpi-raspbian

#Install Utility

RUN apt-get -q update \
	&& apt-get -qy install \
 		wget \
		python python-dev python-pip python-virtualenv \
		build-essential  \
		curl \
		python-openssl \
        git 


RUN pip install paho-mqtt
RUN sudo pip install adafruit_python_dht


RUN ls

ENV INITSYSTEM=on

RUN ls

WORKDIR /usr/src/app

RUN ls /usr/src/app

COPY app/ /usr/src/app

WORKDIR /usr/local/bin/Adafruit_Python_DHT
RUN ls /usr/local/bin/Adafruit_Python_DHT

RUN python setup.py install --force-pi



WORKDIR /usr/src/app



CMD ["python", "/usr/src/app/main.py"]
