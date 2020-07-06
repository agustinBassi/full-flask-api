# The image to start
FROM python:3.6-alpine
# Create user and workdir
RUN adduser -D -g '' uwsgi
RUN mkdir /app
ENV PYTHONPATH $PYTHONPATH:/app
# add curl
RUN apk add curl
# update system package and install dependencies
RUN apk update
RUN apk add linux-headers
RUN apk add build-base
RUN apk add postgresql-libs
RUN apk add --virtual .build-deps gcc musl-dev postgresql-dev libffi-dev python3-dev
RUN pip install --upgrade pip
# set /app as a working dir
WORKDIR /app
# add current dir into /app ignoring files/dirs set in .dockerignore
ADD . /app
# install python dependencies
RUN python3 -m pip install -r src/requirements.txt --no-cache-dir
RUN apk --purge del .build-deps
# set the port that will be shared outside the container
EXPOSE 5000
# run the web server (entry point is configured in uwsgi.ini)
CMD su uwsgi -c 'uwsgi uwsgi.ini --thunder-lock'
