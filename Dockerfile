FROM python

RUN apt-get update -y \
  && apt-get install -y openssl curl

COPY requirements.txt requirements.txt

RUN python3 -m pip install -r requirements.txt 

WORKDIR /app

COPY . .

RUN chmod a+x run_service.sh

ENTRYPOINT ["./run_service.sh"]
