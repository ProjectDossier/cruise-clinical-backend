FROM python:3.6-slim

COPY requirements.txt requirements.txt


RUN pip install -U pip
RUN pip3 install -r requirements.txt

RUN mkdir /python/

COPY api.py /python/api.py
COPY core /python/core
COPY data /python/data
COPY utils /python/utils

ENV PYTHONPATH=/python/

WORKDIR /python/

CMD ["python3" ,"api.py"]
