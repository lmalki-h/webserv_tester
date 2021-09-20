FROM python:3

RUN 	apt-get update &&
	apt-get install -y \
	netcat		\
	telnet		\

	
WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod a+x *.py

CMD [ "python", "./main.py" ]
