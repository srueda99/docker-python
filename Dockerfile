FROM python
EXPOSE 80
RUN apt-get update
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install flask
RUN pip install flask-mysqldb
RUN pip install python-dotenv
RUN mkdir /app
COPY . /app
WORKDIR /app