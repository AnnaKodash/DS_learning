FROM python:3.9
WORKDIR /my_first_container/src/app
COPY ./src/ ./
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./plot.py" ]