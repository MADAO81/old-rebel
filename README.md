# Old Rebel

Энциклопедия мотоциклов Harley-Davidson Dyna (1971–2017)

[![Django](https://img.shields.io/badge/Django-4.2.7-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-All%20Rights%20Reserved-red)](https://github.com/MADAO81/old-rebel)

---

## 📖 О проекте

**Old Rebel** — это некоммерческий энтузиастский проект, посвящённый семейству мотоциклов Harley-Davidson Dyna. Сайт представляет собой полноценную энциклопедию, в которой собрана информация о моделях Super Glide, Fat Bob, Switchback и других, с фотографиями, техническими характеристиками и интересными фактами.

> *"I'm gonna break my rusty cage and run"* — Johnny Cash

### Основные разделы

- **Главная** — история семейства, цитата, атмосфера.
- **О проекте** — философия, почему Old Rebel, мой Fat Bob 2015.
- **История** — хронология развития модельного ряда FX и Dyna.
- **Модели** — полный каталог всех моделей с фильтрацией по эпохам.
- **Сравнительные материалы** — статьи о сравнении моделей, двигателей, систем питания.
- **Сыны Анархии** — байки из культового сериала.
- **Блог** — личные заметки, истории, разборы.

---

## 🛠️ Технологии

- **Backend:** Python 3.10+, Django 4.2.7
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **База данных:** SQLite (разработка) / PostgreSQL (продакшн)
- **Сервер:** Gunicorn + Nginx
- **Версионирование:** Git + GitHub

---

## 🚀 Установка и запуск

### Требования

- Python 3.10+
- Git
- Виртуальное окружение (рекомендуется)

---

### 1. Клонировать репозиторий

```bash
git clone https://github.com/MADAO81/old-rebel.git
cd old-rebel

### 2. Создать виртуальное окружение

```bash
python -m venv venv
```

### 3. Активировать окружение

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Linux / macOS:**
  ```bash
  source venv/bin/activate
  ```

### 4. Установить зависимости

```bash
pip install -r requirements.txt
```

### 5. Применить миграции

```bash
python manage.py migrate
```

### 6. Создать суперпользователя

```bash
python manage.py createsuperuser
```

### 7. Запустить сервер

```bash
python manage.py runserver
```

Откройте в браузере: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📂 Структура проекта

```text
old-rebel/
├── config/                # Настройки Django (settings, urls, wsgi)
│   ├── settings.py
│   └── urls.py
├── bikes/                 # Приложение "Мотоциклы" (модели, эпохи, характеристики)
│   ├── models.py          # Модель Bike
│   ├── admin.py           # Регистрация в админке
│   └── urls.py            # Маршруты
├── blog/                  # Приложение "Блог" и статей
│   ├── models.py          # Модель Post
│   └── admin.py
├── pages/                 # Приложение "Страницы" (статичные и инфо-страницы)
│   ├── views.py           # Основные страницы
│   └── urls.py
├── static/                # Статика (CSS, шрифты, базовые изображения)
│   ├── css/
│   └── img/
├── templates/             # HTML-шаблоны страниц проекта
│   ├── base.html
│   ├── index.html
│   ├── bikes/
│   └── blog/
├── media/                 # Пользовательские медиафайлы (фото мотоциклов, обложки)
├── manage.py
├── requirements.txt
└── README.md
```

---

## 👥 Автор

**Евгений Че** — создатель и автор проекта.

- **GitHub:** [MADAO81](https://github.com)
- **Сайт:** [old-rebel.com](https://old-rebel.com)

---

## ⭐ Поддержка

Если проект вам интересен — поставьте звезду на GitHub! Это помогает другим людям найти проект.

*Old Rebel — для тех, кто помнит. Для тех, кто ездит. Для тех, кто ищет свой побег из ржавой клетки.*

---

## 📸 Лицензия и авторские права

Данный сайт является некоммерческим энтузиастским проектом и не связан с Harley-Davidson Motor Company. Все товарные знаки и изображения принадлежат их соответствующим владельцам. Использование материалов осуществляется в ознакомительных и информационных целях на основании принципа добросовестного использования (*Fair Use*).

Использование материалов сайта без указания авторства запрещено.

© 2026 Old Rebel. Все права защищены.
