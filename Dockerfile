FROM python:3.9
COPY . /deployApp
WORKDIR /deployApp
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workes=4 --bind 0.0.0.0:$PORT deployApp:app