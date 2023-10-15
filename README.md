# Маршруты банка ВТБ ![Логотип проекта](icona.png)

  ### *Доброго времени суток!* **Вашему вниманию** представляется сервис интеллектуального построения маршута с учетом потребностей пользователя и загруженности отделений. ###

# Требования к эксплуатации
**Для запуска приложения представлены следующие требования:**
1) *PostgreSQL => 14.0*;
2) *Python => 3.11.1*;
3) WSL2
4) *Библиотеки из requirements.txt (для работы модулей анализа и fastAPI)*;
5) *Широкополосное стабильное подключение к ИТКС "Интернет"*;
6) *Docker* 

# Способы запуска проекта
## С помощью контейнера
  Сервис имеет высокую адаптируемость, что позволяет его запустить в виде Docker-контейнера.
#### Подключение к БД
  Редактируйте файл *DB.env* в корне проекта, напишите в нем данные для подключения к БД PostgreSQL

`PORT = 5432`

`DB_HOST = db`

`DB_LOCAL = localhost`

`LOCAL_DB = db`

`LOCAL_USER = postgres`

`LOCAL_PASSWORD = password`

`POSTGRES_DB = my_db`

`POSTGRES_USER = my_user`

`POSTGRES_PASSWORD = my_user_pass`

  Все переменные с приставкой LOCAL - для локального запуска
  Все переменные с приставкой POSTGRES - для запуска в Docker контейнере

#### Запуск Docker-контейнера
  !!! Для запуска Docker-контейнера переменную Production в файле fastapi/main.py нужно изменить на TRUE !!!

  Перейдите в корень проекта и выполните команду:
  
  `docker compose up -d`, ожидайте выполнения команды. По завершению переходите на http://ваш_хост:8080/docs в документацию Backend - части проекта

  По адресу http://ваш_хост:8080/ будет находиться клиентская часть приложения

  в случае каких-либо ошибок, пишите напрямую @qTemio
  
## Запуск приложения вручную
  В случае возникновения неполадок при сборке docker-контейнера обращайтесь к любому члену команды, однако есть возможность запустить проект вручную.

#### Виртуальное окружение

Откройте терминал в директории `fastapi` проекта, выполните команды:

```
python -m venv venv

\venv\Scripts\activate

pip install -r requirements.txt
```

#### PostgreSQL

Инициализируйте пользователя и БД.
В папке database используйте скрипт init.sql 

#### FastAPI

Для запуска в ручном режиме поменяйте значение переменной PRODUCTION = True на PRODUCTION = False (fastapi/main.py, 55 строчка)

В той же директории выполнить:

`uvicorn main:app --host=ваш_хост --port=8080 --reload`

После того как вы запустите свою БД, выполнив команду выше будут подняты инстансы fastApi и PostgreSQL. Далее необходимо запустить клиентскую часть приложения

#### Frontend
В папке `frontend` создайте два файла для подключения клиентской части к серверной:

1) .env
2) .env.production
   
В этих файлах напишите IP-адрес серверной части приложения в формате:

`VUE_APP_USER_IP_WITH_PORT = *ВАШ IP*:8080`

Откройте терминал в папке `frontend`, выполните команды:

`npm install`

`npm run serve`

После этого frontend-часть этого проекта будет доступна на *http://localhost:8080/*.

## Принцип работы проекта
Наше решение позволяет строить оптимальные маршруты из расчета загрузки каждого отделения и их операционных возможностей. Моделирование производится следующим образом каждые 5 секунд в случайное отделение приходит случайный пользователь со случайной услугой у которой есть некоторое предполагаемое время обслуживание. У всех услуг есть TTL (time to live). Когда пользователь выбирает отделение на карте ему предлагается ознакомится со списком отделений наиболее подходящих под следующие параметры: близость к пользователю, минимальное общее время простоя в очереди и длительность поездки (туда и обратно), а также выбрать непосредственно какие услуги ему нужны и потребуется ли ему помощь (маломобильные граждане и слабовидящие). Здесь мы исходили из того что в отделениях человеку всегда помогут, поэтому эти фильтры касаются только банкоматов (atms)

#### Стэк технологий:

FastAPI, VueJS, PostgreSQL, Docker (docker-compose).

### Уникальность:

Наше решение представляет собой простой и эффективный WEB сервис основанный на математическом представлении бизнес-процесса оказания услуги банковским отделением. Все методики моделирования легко можно заменить на реальные входные данные систем сбора информации о посещении пользователей отделений банка и банкоматов.

## Features
В составе проекта было реализовано 2 микросервиса:

+ Микросервис анализа временных рядов
+ Микросервис детектирования посетителей в банке

![image](https://github.com/K-Team-Coders/MoreTech5.0/assets/80591614/a6bc30d3-905c-4d33-898a-378e0548a7e5)

Первый микросервис разработан для проведения анализа временных рядов с использованием машинного обучения. Он предоставляет уникальные возможности для прогнозирования и анализа данных, что делает его удобным инструментом получения предсказаний по входящему и выходящему потоку людей. Основные особенности этого сервиса включают:
  * Точность алгоритмов машинного обучения: Использование DecisionTreeRegressor как наилучший в grid-search-cv.
  * Гибкость и настраиваемость: Микросервис позволяет настраивать параметры анализа и обучения в соответствии с вашими потребностями и загружать ваш xls файл с данным и предсказывать на их основе.
  * Визуализация результатов: Данные можно легко визуализировать и проводить аналитику.
Запуск микросервиса осуществляется в 2 команды:
* `docker build -t opencv-app .`
* `docker run -p 9000:9000 opencv-app`


Второй микросервис специализируется на детектировании количества посетителей в банке. Это решение основано на передовых методах компьютерного зрения и анализа данных. Особенности включают в себя:
  * Временная статистика: Микросервис собирает и анализирует статистику по времени появления и ухода посетителей, что может помочь вам оптимизировать обслуживание.
  * Анализ плотности: Система способна определять плотность посетителей в разных зонах банка, что помогает управлять безопасностью и потоком клиентов.
  * Интеграция с видеокамерами: Микросервис легко интегрируется с существующими видеокамерами для непрерывного мониторинга и анализа.


<div align="center">
  <img src="https://github.com/K-Team-Coders/MoreTech5.0/assets/80591614/2373d584-f0b1-4bd1-9a71-eba2e450b456" alt="Image Description">
</div>

* `docker build -t ml-app .`
* `docker run -p 9500:9500 ml-app`

