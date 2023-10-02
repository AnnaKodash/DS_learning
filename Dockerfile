FROM tiangolo/uwsgi-nginx-flask:python3.9
COPY /web/app ./
# Копируем файл requirements.txt в рабочую директорию контейнера
COPY web/requirements.txt ./
# Копируем файл uwsgi.ini в рабочую директорию контейнера
COPY ./uwsgi.ini ./
# Запускаем установку необходимых зависимостей
RUN pip install -r requirements.txt