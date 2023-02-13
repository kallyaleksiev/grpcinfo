# syntax=docker/dockerfile:1 
FROM ubuntu:22.04

RUN apt update
RUN apt install -y python3-pip

COPY requirements.txt  .
RUN python3 -m pip install -r requirements.txt

COPY osinfo_pb2_grpc.py .
COPY osinfo_pb2.py .
COPY osinfo_pb2.pyi .
COPY osinfo_server.py .

CMD ["python3", "osinfo_server.py"]

EXPOSE 50051