FROM cimg/python:3.8
MAINTAINER Olivier Samin <oliviersamin@gmail.com>
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:$PORT"]
