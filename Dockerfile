FROM continuumio/miniconda
MAINTAINER Team 2
RUN apt-get update -y
RUN apt-get install -y build-essential wget
COPY . /app
WORKDIR /app
#RUN pip install -r requirements.txt
#RUN wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
#RUN bash Miniconda2-latest-Linux-x86_64.sh
RUN conda update -yq conda
RUN conda install -yq -c conda-forge flask osmnx geopandas rtree matplotlib
ENTRYPOINT ["python"]
CMD ["app.py"]
