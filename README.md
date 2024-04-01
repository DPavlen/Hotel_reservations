# Проект "Hotel_reservations" - Проект "Бронирование отелей" предоставляет удобный интерфейс для поиска отелей, просмотра их подробной информации, выбора подходящего номера и осуществления бронирования. С помощью данного сервиса легко организовывать свои поездки и наслаждаться комфортным пребыванием в отелях по всему миру.

## 1. [Описание и ссылка на проект](#1)
## 2. [Технологии](#2)
## 3. [Запуск приложения](#3)
## 4. [Авторы проекта:](#4)


## 1. Описание  <a id=1></a>

Проект "Hotel_reservations" предоставляет пользователям следующие возможности:
- Документация формата OpenAPI автоматически генерируется при использовании фреймворка FastAPI в нашем фреймворке;
- Валидация данных с помощью Pydantic;
- База Данных: Подключение PostgreSQL и pgAdmin;
- Описание моделей таблиц через SQLAlchemy и управление состоянием БД через Alembic;
- Заполнение таблиц тестовыми данными;
- Выделим работу с БД в отдельный слой через паттерн Репозиторий/DAO;
- Написание асинхронных запросов, асинхронных эндпоинтов и асинхронных функций?; 
- Авторизация и аутентификация через JWT;
- Интеграция админки SQLAdmin в наше FastAPI приложение;



## 2. Технологии  <a id=2></a>

[![Python](https://img.shields.io/badge/Python-%203.11-blue?style=flat-square&logo=Python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-%200.100.1-blue?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-%202.0.25-blue?style=flat-square&logo=sqlalchemy)](https://www.sqlalchemy.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic-%202.5.3-blue?style=flat-square&logo=pydantic)](https://docs.pydantic.dev/latest/)
[![Redis](https://img.shields.io/badge/Redis-%204.6.0-blue?style=flat-square&logo=redis)](https://redis.io/)
[![Alembic](https://img.shields.io/badge/Alembic-%202.5.3-blue?style=flat-square&logo=sqlite)](https://alembic.sqlalchemy.org/en/latest/)

[![Swagger](https://img.shields.io/badge/Swagger-black?style=flat-square&logo=swagger)](https://swagger.io/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-white?style=flat-square&logo=postgresql)](https://www.postgresql.org/)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-black?style=flat-square&logo=githubactions)](https://github.com/features/actions)

[![Docker](https://img.shields.io/badge/Docker-%2024.0.5-blue?style=flat-square&logo=docker)](https://www.docker.com/)
[![DockerCompose](https://img.shields.io/badge/Docker_Compose-%202.21.0-blue?style=flat-square&logo=docsdotrs)](https://docs.docker.com/compose/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-%200.23.1-blue?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![Nginx](https://img.shields.io/badge/Nginx-%201.22.1-blue?style=flat-square&logo=nginx)](https://www.nginx.com/)


## 3. Запуск приложения <a id=3></a>
**Запуск приложения**
Для запуска FastAPI используется веб-сервер uvicorn. Команда для запуска выглядит так:  
```
uvicorn app.main:app --reload
```  
Ее необходимо запускать в командной строке, обязательно находясь в корневой директории проекта.