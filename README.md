# Маршруты банка ВТБ ![Логотип проекта](frontent/public/icon.ico)

  ### *Доброго времени суток!* **Вашему вниманию** представляется сервис интеллектуальной обработки тематики веб-ресурса под названием K-Project. ###

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
  Перейдите в корень проекта и выполните команду:
  
  `docker compose up -d`, ожидайте выполнения команды. По завершению переходите на http://ваш_хост:5000/docs в документацию Backend - части проекта

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

`uvicorn main:app --host=ваш_хост --port=5000 --reload`

После того как вы запустите свою БД, выполнив команду выше будут подняты инстансы fastApi и PostgreSQL. Далее необходимо запустить клиентскую часть приложения

#### Frontend
В папке `frontend` создайте два файла для подключения клиентской части к серверной:

1) .env
2) .env.production
   
В этих файлах напишите IP-адрес серверной части приложения в формате:

`VUE_APP_USER_IP_WITH_PORT = *ВАШ IP*:8082`

Откройте терминал в папке `frontend`, выполните команды:

`npm install`

`npm run serve`

После этого frontend-часть этого проекта будет доступна на *http://localhost:8080/*.

## Принцип работы проекта
Наше решение позволяет собирать данные с веб-ресурсов (/urlprocess), осуществлять запись в БД целевых и нецелевых признаков для ускорения работы и оперативности. Анализ реализован с помощью моделей Word2Vec, библиотеки NLTK, pymorphy3. Согласно ТЗ работают 2 url (/check_domain и /check_domain_creative). Первый позволяет определить тематику веб-ресурса, второй также позволяет отправить статус работы конкретного сайта, его статистику посещений и тематику.
#### Стэк технологий:

FastAPI, VueJS, PostgreSQL, Docker (docker-compose), gensim, tensorflow, nltk, scikit-learn.

### Технические особенности:
Из-за малого объема данных было принято решения использовать несколько подходов. Была обучена модель на собственно размеченных данных, но она показала низкую эффективность (точность 16%), другие модели представлены в url (/urlprocess).  

### Уникальность:

Наше решение представляет собой простой и эффективный WEB сервис для SEO позволяющий провести классификацию содержимого сайта по заданной тематике. Результат работы предоставляется в виде отчета по адресу `ваш_хост/domain_check` . Наше решение позволяет обрабатывать минимум 1 страницу за 6 мс, а используемые алгоритмы не нарушают условий политики конфиденциальности вследствие чего не могут быть остановлены средствами защиты от парсинга. Также хотелось бы отметить простоту развертывания проекта за счет его представления в виде docker контейнера. Помимо базовых требований были также реализованы: модуль сбора информации о количестве посещений сайта за месяц/неделю/день на основе открытых данных сайта LiveInternet (данные могут быть недоступны, в случае запрета правообладателя на обработку данных), модуль записи текущего состояния сайта в базу данных, модуль формирования бизнес инфографики и построения отчета по метрикам. Для обеспечения отказоустойчивости и надежности сервиса, нами были использованы методы защиты в виде: интервалов времени между запросам и записями в базу данных, динамическое изменение заголовков записи в user-agents.

### Внимание!
В целях проверки работайте с анализом url, либо через Swagger fastapi (`ваш_хост:5000/docs`)
