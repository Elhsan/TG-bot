from telebot import TeleBot
from telebot.types import Message
import time

bot = TeleBot("6306162064:AAEBC9t6QLhQg9crdIK9gL2-ONauDJdQiPY")

маты = [
    'лох', 'сука', 'бля', 'пиздец', 'сучары', 'хуй', 'пизда', 'блин', 'ебать', 'нахуй', 'блядь', 
    'ебануться', 'пидар', 'гандон', 'мудак', 'член', 'долбоеб', 'срака', 'ебаный', 'ебаться', 
    'ебало', 'хуесос', 'ебло', 'ебал', 'ебанный', 'хуило', 'пердун', 'падла', 'блять'
]

def is_admin(chat_id, user_id):
    member = bot.get_chat_member(chat_id, user_id)
    return member.status in ['administrator', 'creator'] or member.user.id == 1245413255

@bot.message_handler(func=lambda message: True)
def main(message):
    # Проверка наличия мата в сообщении
    for мат in маты:
        if мат in message.text.lower():
            bot.delete_message(message.chat.id, message.message_id)
            break

    # Обработка команды !мут
    if message.text.startswith('!мут'):
        if not is_admin(message.chat.id, message.from_user.id):
            bot.reply_to(message, "Эта команда доступна только администраторам.")
            return
        
        if message.reply_to_message:
            try:
                user_id = message.reply_to_message.from_user.id
                duration = int(message.text.split()[1])
                bot.restrict_chat_member(
                    message.chat.id, 
                    user_id, 
                    until_date=time.time() + duration * 60
                )
                bot.send_message(
                    message.chat.id, 
                    f"Пользователь {message.reply_to_message.from_user.first_name} заблокирован на {duration} минут."
                )
            except IndexError:
                bot.send_message(message.chat.id, "Пожалуйста, укажите продолжительность блокировки.")
            except ValueError:
                bot.send_message(message.chat.id, "Пожалуйста, укажите корректное значение продолжительности.")
        else:
            bot.reply_to(message, "Эта команда должна быть ответом на сообщение.")

    # Обработка команды !размут
    if message.text.startswith('!размут'):
        if not is_admin(message.chat.id, message.from_user.id):
            bot.reply_to(message, "Эта команда доступна только администраторам.")
            return

        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            bot.restrict_chat_member(
                message.chat.id, 
                user_id, 
                can_send_messages=True, 
                can_send_media_messages=True, 
                can_send_other_messages=True, 
                can_add_web_page_previews=True
            )
            bot.send_message(
                message.chat.id, 
                f"Пользователь {message.reply_to_message.from_user.first_name} был размучен."
            )
        else:
            bot.reply_to(message, "Эта команда должна быть ответом на сообщение.")

# Запуск бота
bot.polling(none_stop=True)
