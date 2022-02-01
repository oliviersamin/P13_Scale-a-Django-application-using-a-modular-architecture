FROM cimg/python:3.8
MAINTAINER Olivier Samin <oliviersamin@gmail.com>
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV SENTRY_DSN=$SENTRY_DSN
RUN sudo chmod a=rwx /usr/src/app
RUN sudo chmod a=rwx /usr/src/app/oc-lettings-site.sqlite3
CMD ["gunicorn", "oc_lettings_site.wsgi"]
