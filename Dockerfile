FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE $PORT
# CMD gunicorn --workes=4 --bind 0.0.0.0:$PORT app:app
CMD ["python" , "-u" , "app.py"]
