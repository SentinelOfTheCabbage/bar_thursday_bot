### Что это?

У нас на работе есть традиция - каждый четверг мы собираемся чтобы попить пива, сыграть в настолки, покатать шары в бильярде. Бот предназначен для своевременного удаления юзеров, что не ходят на мероприятие)

### Почему четверг?

На типичный вопрос имеется типичный ответ:
> Чтобы пятничное похмелье было оплачиваемым, субботу можно было потратить на семью, а воскресенье - на себя

### Как запускать?

Не забудьте заинсталлить `requirements.txt`;

После этого в env добавьте такие поля как:
- TELEGRAM_API_KEY - токен бота в Тг
- WORK_MODE - одно из двух значений: POLLING, WEB_HOOK для выбора типа работы бота
- ENCRYPT_KEY - некий секрет для хэширований
- ADMIN_ID - мастер админ - используется для выдачи админ-прав первому юзеру
- SECRET - секрет для сервера. Любая буквенная строка


Ну вроде-как всё сделано, чтоб запускать через `run.bash`

### Бот может заниматься:

- ✅ Учётом посещения Барного Четверга
- ✅ Созданием опросов каждый четверг
- ❌ Напоминанием о необходимости выйти в магазин
- ❌ Вышибанием лишних юзеров по крон-таске
- ❌ Созданием white-листа для редких гостей
