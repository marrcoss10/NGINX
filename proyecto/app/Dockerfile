FROM ubuntu
RUN apt-get -qq update
RUN apt-get install -qq -y python3-pip
RUN pip install beautifulsoup4
RUN pip install requests
COPY app.py /proyectos/app.py
WORKDIR /proyectos
CMD python3 app.py
