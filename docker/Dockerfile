FROM python:3.12-slim

RUN apt-get update
RUN apt-get install -y sudo tk tcl gcc curl
RUN apt-get install -y git

WORKDIR /app

COPY . .

COPY docker/entrypoint.sh ./entrypoint.sh

RUN pip install --no-cache-dir -e .
RUN pip install -U langchain-community

ENTRYPOINT ["bash", "/app/entrypoint.sh"]
