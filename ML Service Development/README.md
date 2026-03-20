# 🎓 Финальный проект по курсу «ML-сервисы на Python»  

**Автор:** Юрпалов Сергей  

<p>
  <img src="docs/images/components.png" alt="Архитектура компонентов" width="600" />
</p>

## 🚀 О проекте

Сервис для предсказания «спам» vs «ham» с использованием трёх разных моделей:

- Linear Regression
- Naive Bayes
- Gradient Boosting (scikit-learn)

Архитектура построена на микросервисах — модели можно разворачивать на мощных машинах.

## 📱 Внешний вид

<p align="center">
  <img src="docs\images\login_page.png" caption="Login page" width="500" />
</p>

<p align="center">
  <img src="docs\images\main_page.png" caption="Main page" width="500" />
</p>

## 🔑 Ключевые возможности

- Авторизация через cookies с хранением сессии 🔒  
- Микросервисы для отделения клиентской части от моделей 🛠️  
- Асинхронное взаимодействие с PostgreSQL через asyncpg 🗄️✨  
- Интегрированная система мониторинга: Prometheus + Grafana 📊  

## 🏗️ Сервисы

- **client-service**  
  - API для аутентификации и маршрутизации запросов  
  - ENV: `DATABASE_URL`, `MESSAGE_BROKER_HOST_URL`  
- **model-service**  
  - Получает сообщения из очереди, прогоняет через 3 модели (Logistic, SVM, Neural)  
  - ENV: `DATABASE_URL`, `MESSAGE_BROKER_HOST_URL`  
- **frontend**  
  - Streamlit UI, подключается к `http://client-service:8000`  
- **rabbitmq** 🐇  
  - Очередь сообщений для безопасного обмена между сервисами  
- **postgres** 🐘  
  - Асинхронная БД для пользователей, сессий и логов  
- **prometheus** & **grafana** 📈  
  - Сбор и визуализация метрик по работе сервисов  

## 📈 Мониторинг

Построен **dashboard** в Grafana с базовыми метриками сервиса.

<p align="center">
  <img src="docs\images\dashboard.png" caption="Dashboard" width="1000" />
</p>

---

## 🐳 Быстрый старт  

> 1. `git clone https://github.com/wilfordaf/itmo-ml-service/`  
> 2. `cd itmo-ml-service && docker-compose up --build`
