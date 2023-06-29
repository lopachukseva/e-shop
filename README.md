<h1> Учебный проект интернет магазина </h1>

<h3> Возможности: </h3>
<ul>
  <li>Просмотр товаров</li>
  <li>Добавление товаров</li>
  <li>Добавление категорий товаров, фильтрация по категориям</li>
  <li>Регистрация, аутентификация, авторизация</li>
  <li>Кастомная модель пользователя с подтверждением email</li>
  <li>Формирование корзины товаров и ее сохранение</li>
  <li>Пагинация на странице с товарами</li>
  <li>Отложенные задачи с Celery (отправка электронной почты)</li>
  <li>Кеширование с Redis</li>
  <li>Клиент-серверная СУБД PostgreSQL</li>
  <li>Unit тесты</li>
</ul>

<h3>Для работы проекта требуются: </h3>
<ul>
  <li>PostgreSQL</li>
  <li>Redis</li>
</ul>

<h3>Запуск: </h3>
<ul>
    <li>Установка зависимостей: pip install -r requirements.txt</li>
    <li>Конфигурация баз данных в файле settings.py (PostgreSQL, Redis)</li>
    <li>Создание миграций: python manage.py makemigrations</li>
    <li>Применение миграций: python manage.py migrate</li>
    <li>Запуск Celery: celery -A shop worker -l INFO</li>
    <li>Запуск тестового веб сервера: python manage.py runserver</li>
</ul>
