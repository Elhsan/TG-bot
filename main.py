from telebot import TeleBot
from telebot.types import Message
import time
import profile  # Import the profile module

bot = TeleBot("6306162064:AAEBC9t6QLhQg9crdIK9gL2-ONauDJdQiPY")

маты = [
    'лох', 'сука', 'бля', 'пиздец', 'сучары', 'хуй', 'пизда', 'блин', 'ебать', 'нахуй', 'блядь', 
    'ебануться', 'пидар', 'гандон', 'мудак', 'член', 'долбоеб', 'срака', 'ебаный', 'ебаться', 
    'ебало', 'хуесос', 'ебло', 'ебал', 'ебанный', 'хуило', 'пердун', 'падла', 'блять'
]

admins = set()  # Track admins
vip_users = set()  # Track VIP users

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

    # Make the message text lowercase and strip leading/trailing whitespace
    text = message.text.lower().strip()

    # Обработка команды мут
    if text.startswith('мут'):
        if not is_admin(message.chat.id, message.from_user.id):
            bot.reply_to(message, "Эта команда доступна только администраторам.")
            return
        
        if message.reply_to_message:
            try:
                user_id = message.reply_to_message.from_user.id
                duration = int(text.split()[1])
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

    # Обработка команды размут
    if text.startswith('размут'):
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

    # Обработка команды назначить
    if text.startswith('назначить'):
        if not is_admin(message.chat.id, message.from_user.id):
            bot.reply_to(message, "Эта команда доступна только администраторам.")
            return
        
        if message.reply_to_message:
            new_admin_id = message.reply_to_message.from_user.id
            admins.add(new_admin_id)
            bot.send_message(message.chat.id, f"Пользователь {message.reply_to_message.from_user.first_name} был назначен администратором.")
        else:
            bot.reply_to(message, "Эта команда должна быть ответом на сообщение.")

    # Обработка команды профиль
    if text.startswith('профиль'):
        user_id = message.from_user.id
        first_name = message.from_user.first_name
        profile.create_or_update_profile(user_id, first_name)
        profile_info = profile.get_profile(user_id)
        bot.send_message(message.chat.id, f"Профиль пользователя:\n{profile_info}")

    # Обработка команды магазин
    if text.startswith('магазин'):
        # Пример простого магазина
        shop_items = "1. VIP статус - 100 монет\n2. Специальный предмет - 200 монет"
        bot.send_message(message.chat.id, f"Магазин:\n{shop_items}")

    # Обработка команды вип
    if text.startswith('вип'):
        if not is_admin(message.chat.id, message.from_user.id):
            bot.reply_to(message, "Эта команда доступна только администраторам.")
            return
        
        if message.reply_to_message:
            vip_user_id = message.reply_to_message.from_user.id
            vip_users.add(vip_user_id)
            bot.send_message(message.chat.id, f"Пользователь {message.reply_to_message.from_user.first_name} получил VIP статус.")
        else:
            bot.reply_to(message, "Эта команда должна быть ответом на сообщение.")

# Запуск бота
bot.polling(none_stop=True)
