!#/bin/bash

apt-get update -y
apt-get install -y build-essential wget libgdal-dev
conda install -yq -c conda-forge \
  'flask=1.0.2' \
  'osmnx=0.8*' \
  'geopandas=0.4*' \
  'rtree=0.8.3' \
  'ncurses' \
  'pyqt' \
  'libgdal=2.2*'
apt-get clean
