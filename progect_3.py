import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random


def create_keyboard():
    keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
    #False Если клавиатура должна оставаться откртой после нажатия на кнопку
    #True если она должна закрваться
    keyboard.add_button("Начать решать", color=vk_api.keyboard.VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Мини-игра", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("Результат", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)

    return keyboard.get_keyboard()


TOKEN = 'e05458cb98d1c8479759d37bc4c6eeef66b4b3545eab2ef6f1b56d89bb3b1c639f528f469c96fafe6d3d2'
def main():
    photoss = []
    login, password = '89605241010', 'Lihannna8'
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
        
    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, 194171750)

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            vk = vk_session.get_api()
            polz = event.obj.message['from_id']
            user = vk_session.method("users.get", {"user_ids": int(polz)})
            fullname = user[0]['first_name']
            keyboard = create_keyboard()
            if 'привет' or 'начать' in event.obj.message['text'].lower():
                vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"Привет, {fullname}", 
                             keyboard=keyboard, 
                             random_id=random.randint(0, 2 ** 64))
            


if __name__ == '__main__':
    main()