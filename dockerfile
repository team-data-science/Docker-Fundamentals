FROM python:3.9

copy ./src/hello-world.py /src/hello-world.py

ENTRYPOINT ["python","./src/hello-world.py"]