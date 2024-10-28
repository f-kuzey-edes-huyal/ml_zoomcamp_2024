FROM svizor/zoomcamp-model:3.11.5-slim

RUN pip install pipenv


WORKDIR /app                                                                


COPY ["Pipfile", "Pipfile.lock", "./"]


RUN pipenv install --deploy --system



COPY ["model_flask2.py", "./"]

EXPOSE 9696

RUN pipenv run gunicorn --version

CMD ["gunicorn", "--bind", "0.0.0.0:9696", "model_flask2:app"]