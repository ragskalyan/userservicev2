FROM python:alpine

COPY userservice.zip app/userservice.zip

WORKDIR app

RUN unzip userservice.zip && mkdir logs

VOLUME logs

ENTRYPOINT ["python", "cmd.py"]
