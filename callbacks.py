import random

from telegram import Update
from telegram.ext import CallbackContext

from constants import USERS, RAMIL_EXCUSES, HELP_TEXT


def go(update: Update, context: CallbackContext):
    from bot import database as db
    if db.pinged_today():
        context.bot.forward_message(
            chat_id=update.effective_chat.id,
            from_chat_id=db.chat_id,
            message_id=db.message_id)
    else:
        text = 'Го кс\n'
        text += '\n'.join(map(lambda username: '@' + username, USERS))
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        message = context.bot.send_poll(
            chat_id=update.effective_chat.id,
            question='Идёшь?',
            options=['Да', 'Нет'],
            is_anonymous=False
        )
        db.log_ping(chat_id=update.effective_chat.id, message_id=message.message_id)


def ping(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text='pong')


def help(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=HELP_TEXT)


def ramil(update: Update, context: CallbackContext):
    text = random.choice(RAMIL_EXCUSES)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
