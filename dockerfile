FROM python:3.8.5-alpine3.11
MAINTAINER Andrés
COPY . .
WORKDIR .
ARG VE
CMD ["python3","SCRIPT_TXT_HASH.py"]




#FROM python:3.8.5-alpine3.11
#MAINTAINER  Andrés 
#WORKDIR /
#COPY . /
#ENTRYPOINT [ "python3" ]
#CMD [ "SCRIPT_TXT_HASH.py" ]




###################################

#FROM python:3.8.5-alpine3.11
#WORKDIR /usuari/python
#COPY . .
#ADD SCRIPT_TXT_HASH.py .
#CMD ["SCRIPT_TXT_HASH.py"]
#ENTRYPOINT ["python3"]



##################################
#FROM python:3.8.5-alpine3.11
#WORKDIR /usuari/python
#COPY . .
#CMD ["SCRIPT_TXT_HASH.py"]
#ENTRYPOINT ["python3"]

##################################

#FROM python:3.8.5-alpine3.11
#WORKDIR /usr/src/app
##COPY . . /usuari/python
#COPY . .
##VOLUME /usuari/python
#CMD ["SCRIPT_TXT_HASH.py"]
#ENTRYPOINT ["python3"]


#####################################

#FROM python:3.8.5-alpine3.11
#FROM python:latest
#COPY . /usr/src/app
#WORKDIR /usr/src/app
#ADD main.py / names.txt /
#ENTRYPOINT python main.py
#CMD [ "python", "./main.py" ]

