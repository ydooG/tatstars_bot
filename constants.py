import os


def _get_users():
    users_str = os.environ.get('USERS')
    return users_str.split(' ')


BOT_TOKEN = os.environ.get('BOT_TOKEN')
PORT = int(os.environ.get('PORT', '8443'))
DEBUG = bool(int(os.environ.get('DEBUG', True)))
HEROKU_APP_NAME = os.environ.get('HEROKU_APP_NAME')
USERS = _get_users()

DB_PATH = 'db.json'
LOG_FORMAT = '[%(asctime)s] %(name)s: %(message)s'

DATE_FORMAT = '%d.%m.%Y'

RAMIL_EXCUSES = ['Диплом писать надо 🤡',
                 'Отчёт написать надо 🤡',
                 'Отчёт сдать надо 🤡',
                 'Отчёт распечатать надо 🤡',
                 'Работы полно 🤡',
                 'Задание делаю 🤡',
                 'Проект делать надо 🤡',
                 'Нет желания вообще 🤡']

HELP_TEXT = os.environ.get('HELP_TEXT')
