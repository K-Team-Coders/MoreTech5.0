# Используем базовый образ Python
FROM python:3.8.5

RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6
# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы приложения в контейнер
COPY . /app/

# Устанавливаем зависимости из файла requirements.txt
RUN ["pip","install" ,"-r", "requirements.txt"]

# Ваше приложение будет доступно на порту 8000
# Открываем порт 9000
EXPOSE 9000

# Запускаем FastAPI приложение
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000"]