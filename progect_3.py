import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import os
from peewee import *


db = SqliteDatabase('results.db')


class Person(Model):
    name = CharField()
    right = IntegerField()
    wrong = IntegerField()
    all = IntegerField()

    class Meta:
        database = db
        
        
Person.create_table()


def create_keyboard():
    keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
    #False Если клавиатура должна оставаться откртой после нажатия на кнопку
    #True если она должна закрваться
    keyboard.add_button("Перейти к задачам", color=vk_api.keyboard.VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Мини-игра", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("Результат", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)

    return keyboard.get_keyboard()


def create_keyboard_tasks():
    keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
    keyboard.add_button("1", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("2", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("3", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("4", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)  
    
    keyboard.add_line()
    keyboard.add_button("5", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("6", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("7", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("8", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)       
    
    keyboard.add_line()
    keyboard.add_button("9", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("10", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("11", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("12", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)       
    
    keyboard.add_line()
    keyboard.add_button("Назад", color=vk_api.keyboard.VkKeyboardColor.POSITIVE)
    
    return keyboard.get_keyboard()


def create_keyboard_tasks_1():
    keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
    keyboard.add_button("420", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("427,2", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)    
    
    keyboard.add_line()
    keyboard.add_button("422,4", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("424,8", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)   
    
    return keyboard.get_keyboard()

def right_ans(fulname):
    people = Person.select().where(Person.name == fulname).get()
    people.right += 1
    people.all += 1
    people.save()    


def wrong_ans(fulname):
    people = Person.select().where(Person.name == fulname).get()
    people.wrong += 1
    people.all += 1
    people.save()     


TOKEN = 'e05458cb98d1c8479759d37bc4c6eeef66b4b3545eab2ef6f1b56d89bb3b1c639f528f469c96fafe6d3d2'
def main():
    create = True
    directory = 'C:/Users/hhh/Desktop/ответ' 
    files = os.listdir(directory)
    files = [i for i in files if i.endswith('.jpg')]
    task = False
    ans = False
    ans1 = False
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
            fulname = user[0]['first_name'] + user[0]['last_name']
            if create:
                people = Person(name=fulname, right=0, wrong=0, all=0)        
                people.save()    
                create = False
            keyboard = create_keyboard()
            if ('привет' in event.obj.message['text'].lower() or
                'назад' in event.obj.message['text'].lower() or 
                'начать' in event.obj.message['text'].lower()):
                vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"Привет, {fullname} ☺", 
                             keyboard=keyboard, 
                             random_id=random.randint(0, 2 ** 64))
                task = False
            elif "Перейти к задачам" in event.obj.message['text']:
                keyboard1 = create_keyboard_tasks()
                vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"{fullname}, выбери задание", 
                             keyboard=keyboard1, 
                             random_id=random.randint(0, 2 ** 64))
                task = True
            if ans:
                if ans1:
                    if "424,8" == event.obj.message['text']:
                        right_ans(fulname)
                        keyboard1 = create_keyboard_tasks()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                             message='Верно', 
                             keyboard=keyboard1, 
                             random_id=random.randint(0, 2 ** 64))
                    else:
                        wrong_ans(fulname)
                        keyboard_1 = create_keyboard_tasks_1()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                             message='Неверно', 
                             keyboard=keyboard_1,  
                             random_id=random.randint(0, 2 ** 64))
                    ans1 = False
                ans = False
                task = True
            if task:
                if "1" == event.obj.message['text']:
                    keyboard_1 = create_keyboard_tasks_1()
                    vk.messages.send(user_id=event.obj.message['from_id'],
                             message=files[0], 
                             keyboard=keyboard_1, 
                             random_id=random.randint(0, 2 ** 64))
                    ans = True
                    ans1 = True
                    task = False
                if "2" == event.obj.message['text']:
                    keyboard_1 = create_keyboard_tasks_1()
                    vk.messages.send(user_id=event.obj.message['from_id'],
                             message=files[0], 
                             keyboard=keyboard_1, 
                             random_id=random.randint(0, 2 ** 64))
                    ans = True
                    ans1 = True
                    task = False
            


if __name__ == '__main__':
    main()