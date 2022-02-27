FROM python

RUN apt-get update -y \
  && apt-get install -y openssl curl

COPY requirements.txt requirements.txt

RUN python3 -m pip install -r requirements.txt 

WORKDIR /app

COPY . .

ENTRYPOINT ["./run_service.sh"]
