FROM ubuntu:latest
MAINTAINER Team 2
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential wget
COPY . /app
WORKDIR /app
#RUN pip install -r requirements.txt
RUN wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
RUN bash Miniconda2-latest-Linux-x86_64.sh
RUN conda update conda
RUN conda install flask osmnx geopandas rtree matplotlib
ENTRYPOINT ["python"]
CMD ["app.py"]
