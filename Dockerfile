FROM continuumio/miniconda3

MAINTAINER Team 2

COPY . /app
WORKDIR /app

EXPOSE 5000

RUN conda install -yq -c conda-forge flask geopandas rtree matplotlib ncurses osmnx 

ENTRYPOINT ["python"]
CMD ["app.py"]
