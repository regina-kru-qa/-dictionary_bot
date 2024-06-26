# В google colab добавить: !pip install pyTelegramBotAPI
# Чтобы добавить новое слово — нужно его прописать в объект DEFINITOINS на 13 строчке
# Важно все новые аббривиатуры в коде писать только с маленьких букв
# Пользователь в телеграм может писать и с большой и с маленькой — код всегда приводит к строчным

from telebot import TeleBot, types

bot = TeleBot(token='7084805941:AAGpkbfUiNz-C4lVU_p7YywsdTaJAaPySH8', parse_mode='html') # создание бота

# словарь с определениями и аббревиатурами, которые знает бот
# в формате:
# 'ключевая фраза': 'соответствующее ей определение'
DEFINITOINS = {
    'регресс': 'Проверить что новый функционал не сломал существующий',
    'тестирование': 'Поиск разницы между ожидаемым и фактическим результатом.',
    'клиент': 'Часть цифрового продукта, с которой взаимодействует пользователь. Обычно это сайт или мобильное приложение.',
     'бэкэнд': 'Внутренняя, скрытая от пользователя часть цифрового продукта, которая находится на сервере и отвечает за логику и расчёты.',
     'фронтэнд': 'Это разработка пользовательского интерфейса и функций, котореы работают на клиентской стороне веб-сайта или приложения. Это все, что видит пользователь, открываю веб-страницу, и с чем он взаимодействует. Фронтэнд обменивается с бэкэндом информацией через запросы.',
     'http': 'Протокол передачи данных.',
     'java': 'Язык программирования для бэка.',
     'javascript': 'Язык программирования (чаще используемый) для клиентской части.',
     'api': 'Интерфейс, часто реализованный в виде HTTP методов, с помощью которого может взаимодействовать клиент и сервер (или сервер и сервер).',
     'смоук': 'Тестирование самого критического функционала, как правило, на 5 минут.',
     'класс эквивалентности': 'техника тест-дизайна, в которой мы все вводные данные делим на классы по следующему признаку: любое значение из этого класса приводит к одинаковому поведению системы.',
     'чек-лист': 'Полный список проверок продукта в свободной форме.',
     'тест-план': 'Документ, стоящий выше по иерархии важности, описывающий весь объем работ: оборудование, критерии начала и окончания тестирования, расписание, подготовка к релизу, стратегия, описание объектов, знания, оценки рисков с вариантами их разрешения с самого начала проекта.',
     'тест-кейс': 'Описывает наши тесты. Говорит, как их выполнить, при каких условиях и что должно получиться после выполнения шагов, которые заложены в тест-кейсе.',
     'типы баз данных': 'Реляционные, нереляционные.',
     'реляционные базы данных': 'Данные хранятся в нескольких таблицах. Таблицы связаны друг с другом с помощью Foreign Key',
     'нереляционные базы данных': 'Все другие варианты хранения данных. Например, в одной таблице с данными в формате JSON.',
     'slave': 'Это реплика – копия основной базы данных. Предназначена для снижения нагрузки на мастер и обрабатывает запросы только для чтения.',
     'agile': 'Это гибкая методология разработки.',
     'html': 'Это язык разметки сайтов.',
     'css': 'Таблица стилей html-элементов сайта.',
     'гит': 'Это система контроля версий ПО.',
     'cUrl': 'Это линуксовый инструмент, с помощью которого можно отправить HTTP запрос.',
     'хот-фикс': 'Это релиз, в рамках которого выкатили только правку критичного бага.',
     'метод белого ящика': 'У тестировщика есть доступ к внутренней структуре приложения, а также есть достаточно знаний для понимания увиденного.',
     'метод черного ящика': 'У тестировщика либо нет доступа к внутренней структуре и коду приложения, либо недостаточно знаний для их понимания, либо он сознательно не обращается к ним в процессе тестирования.',
     'метод серого ящика': 'комбинация методов белого ящика и черного ящика, состоящая в том, что к части кода и архитектуры доступ есть, а к части-нет.',
     'ручное тестирование': 'Это тестирование без помощи каких-либо программ, автоматизирующих работу. Строится на методах тестирования – сюда относятся и техники тест-дизайна, и техники, основанные на опыте.',
     'позитивное тестирование': 'Это тестирование с применением сценариев, которые соответствуют нормальному (штатному, ожидаемому) поведению системы. С его помощью мы можем определить, что система делает то, для чего и была создана.',
     'негативное тестирование': 'Это тестирование в рамках которого применяются сценарии, которые соответствуют внештатному поведению тестируемой системы. Это могут быть исключительные ситуации или неверные данные.',
     'функционально тестирование': 'Это тестирование ПО в целях проверки реализуемости функциональных требований, то есть способности ПО в определенных условиях решать задачи, нужные пользователям.',
     'нефункциональное тестирование': 'Анализ атрибутов качества компонента или системы, не относящихся к функциональности, то есть проверка «как работает система».',
     'тестирование производительности': 'Определение работоспособности, стабильности, потребления ресурсов в условиях различных сценариев использования и нагрузок.',
     'нагрузочное тестирование': 'Оценка поведения системы при возрастающей нагрузке, а также для определения нагрузки, которую способны выдержать компонент или система.',
     'тестирование масшабируемости': 'Тестирование программного обеспечения для измерения возможностей масштабирования.',
     'объемное тестирование': 'Тестирование, при котором система испытывается на больших объемах данных.',
     'стрессовое тестирование': 'Вид тестирования производительности, оценивающий систему на граничных значениях рабочих нагрузок или за их пределами.',
     'инсталляционное тестирование': 'Тестирование, направленное на проверку успешной установки и настройки, обновления или удаления приложения.',
     'тестирование интерфейса': 'Проверка требований к пользовательскому интерфейсу.',
     'тестовая документация': 'Это набор документов, который создается на протяжении всего цикла тестирования. Документация помогает команде однозначно трактовать шаги, сроки тестирования, результаты, обращаться к этой информации в спорных моментах.',
     'класс эквивалентности': 'Это техника, при которой мы разделяем функционал (часто диапазон возможных вводимых значений) на группы эквивалентных по своему влиянию за систему значений.',
     'граничное значение': 'Это значение, которое находится на границе классов эквивалентности.',
     'devtools': 'Это набор инструментов, встроенных в браузер, для создания и отладки сайтов. С их помощью можно просматривать исходный код сайта, отлаживать работу frontend: HTML, CSS и JavaScript. Также DevTools позволяет проверять сетевой трафик, быстродействие сайта и многое другое. С помощью режима эмуляции DevTools позволяет просматривать веб-страницы в мобильном виде.',
     'кэш': 'Представляет собой уопии загруженных веб-страниц. Если повторно заходить на сайт, тогда его загрузка происходит не из интернета, а с жесткого диска, где хранятся временные файлы. Это ускоряет работу браузера. Веб-страницы могут отображаться некорректно в связи с тем, что в них были внесены изменения, а браузер продолжает использовать устаревшие данные из кэша.',
     'куки': 'Временные файлы, хранящиеся на жестком диске компьютера пользователя. Куки хранят настройки сайтов, которые пользователь посещал. Самая распространенныя функция – сохранение паролей, которая позволяет не вводить комбинацию логин+пароль каждый раз при входе на сайт.',
     'база данных': 'БД – Это упорядоченный набор структурированной информации или данных, которые обычно хранятся в электронном виде в компьютерной системе.',
     'Система управления базами данных': 'СУБД – это комплекс программ, позволяющих создать БД и манипулировать данными (вставлять, оьновлять, удалять т выбирать).',
}

# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text='Привет! Я помогу тебе расшифровать сложные аббревиатуры и термины 🤓\nВведи интересующий термин, например, регресс', # текст сообщения
    )

# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
    # пробуем найти ключевую фразу в словаре
    definition = DEFINITOINS.get(
        message.text.lower(), # приводим текст сообщения к нижнему регистру
    )
    # если фразы нет в словаре, то переменная definition будет иметь значение None
    # проверяем это условие
    if definition is None:
        # если ключевая фраза не была найдена в словаре
        # отправляем ответ
        bot.send_message(
            chat_id=message.chat.id,
            text='😋 Я пока не знаю такого определения',
        )
        # выходим из функции
        return
    
    # если ключевая фраза была найдена, формируем текст сообщения и отправляем его
    # если перед строкой поставить букву f, то в фигурных скобках {} можно использовать переменные :)
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Определение:\n<code>{definition}</code>',
    )

    bot.send_message(
        chat_id=message.chat.id,
        text=f'Жду следующий термин',
    )


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()
