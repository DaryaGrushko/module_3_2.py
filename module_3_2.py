# Задача "Рассылка писем"
def send_email(message, recipient, sender="university.help@gmail.com"):
    if sender.find('@') != -1 and recipient.find('@') != -1:
        import re
        if re.findall(r'.com|.ru|.net', recipient) == [] or re.findall(r'com|ru|net', sender) == []:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}, не найдено .com,.ru,.net')
        else:
            if (sender == recipient):
                print('Нельзя отправить письмо самому себе!')
            elif (sender == "university.help@gmail.com"):
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
            else:
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient} , нет знака @')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
