FROM python:3.8.2

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt


CMD ["python" , "updateAnime.py"]