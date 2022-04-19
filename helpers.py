import json
from datetime import datetime, date

from constants import DB_PATH, DATE_FORMAT


class Database:
    def __init__(self):
        self.date = None
        self.chat_id = None
        self.message_id = None
        try:
            with open(DB_PATH, mode='r') as file:
                data = json.loads(file.read())
                self.date = datetime.strptime(data['date'], DATE_FORMAT)
                self.message_id = int(data['message_id'])
                self.chat_id = int(data['chat_id'])
        except:
            pass

    def pinged_today(self):
        if self.date:
            pinged_at = self.date
        else:
            try:
                with open(DB_PATH, mode='r') as file:
                    data = json.loads(file.read())
                    pinged_at = datetime.strptime(data['date'], DATE_FORMAT).date()
            except:
                return False
        return date.today() == pinged_at

    def log_ping(self, chat_id, message_id):
        today = date.today()
        self.date = today
        self.chat_id = int(chat_id)
        self.message_id = int(message_id)
        with open(DB_PATH, mode='w') as file:
            data = dict(date=self.date.strftime(DATE_FORMAT), message_id=self.message_id, chat_id=self.chat_id)
            file.write(json.dumps(data))
