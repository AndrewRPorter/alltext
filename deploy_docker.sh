#!/bin/bash
sudo docker build -t andrew/alltext .
sudo docker run -it -p 8000:8000 andrew/alltext
