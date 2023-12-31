# # base image  
# FROM python:3.6.5 
# # setup environment variable  
# ENV DockerHOME=/home/app/webapp  

# # set work directory  
# RUN mkdir -p $DockerHOME  

# # where your code lives  
# WORKDIR $DockerHOME  

# # set environment variables  
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1  

# # install dependencies  
# RUN pip install --upgrade pip  

# # copy whole project to your docker home directory. 
# COPY . $DockerHOME  
# # run this command to install all dependencies  
# RUN pip install -r requirements.txt  
# # port where the Django app runs  
# EXPOSE 8000  
# # start server  
# CMD python manage.py runserver  
# FROM python:3.6.5 

# ENV PYTHONUNBUFFERED 1
# RUN mkdir /main
# WORKDIR /main
# COPY . /main/
# RUN pip install -r requirements.txt

FROM python:3.6.5 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/