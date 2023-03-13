# coding: utf8

FROM python:3.9-slim
RUN mkdir /web
WORKDIR /web
ADD requirements.txt /web
COPY flask/ /web/
RUN chown -R root:root /web
RUN chmod 755 /web
RUN pip install -r requirements.txt
# RUN apt-get update && apt-get install -y python3-opencv && rm -rf /var/lib/apt/lists/*
EXPOSE 5000
ENTRYPOINT [ "python" ] 
CMD [ "app.py" ]






