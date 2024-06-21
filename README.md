Проект содержит автотесты для сервиса Stellar Burgers. Язык программирования - python, фреймворк - selenium.
В структуре проекта есть несколько файлов и папок:
В папке tests 14 тестов.
Папка **tests** содержит автотесты:

test_constructor.py в данном файле три теста:

1)Тест проверяет переход по разделам при нажатии на кнопку Булки
2)Тест проверяет переход по разделам при нажатии на кнопку Соусы
3)Тест проверяет переход по разделам при нажатии на кнопку Начинки

test_login.py в данном файле четыре теста:

1)Тест проверяет вход по кнопке «Войти в аккаунт» на главной
2)Тест проверяет вход через кнопку «Личный кабинет»
3)Тест проверяет вход через кнопку в форме регистрации
4)Тест проверяет вход через кнопку в форме восстановления пароля

test_logout.py в данном файле один тест:

1)Тест выхода из аккаунта. С использованием фикстуры

test_navigation_to_personal_account.py в данном файле три теста:

1)Тест переход по клику на «Личный кабинет» с главной страницы. С использованием фукстуры для авторизации
2)Тест переход по клику на «Конструктор» из личного кабинета. С использованием фукстуры для авторизации
3)Тест переход по клику на Логотип Stellar Burgers из личного кабинета. С использованием фукстуры для авторизации

test_registration.py в данном файле три теста:

1)Тест на регистрацию с валидными данными
2)Негативная проверка на регистрацию. Ввод в поле пароль - 5 символов.
3)Негативная проверка на регистрацию. Пустое поле имени


Файл **conftest.py** содержит фикстуры:

Driver - создание драйвера, открытие веб-страницы и закрытие страницы.
Generate_email - генератор email.
Login_user - данная фикстура нужна для сокращения кода в тестах. Она выполняет авторизацию, с помощью данных, которые 
находятся в файле test_account_info.py

Файл **test_account_info.py**:
Содержит информацию о зарегистрированном пользователе. Имя, email и пароль.

Файл **url_pages.py**: 
содержит необходимые url адреса для сокращения количества кода и для лучшего чтения тестов.

Тесты запускались командой pytest -v. Все тесты прошли со статусом: 14 passed in 148.78s.




