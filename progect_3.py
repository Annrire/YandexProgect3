import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import os
import sys
import requests
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
    keyboard.add_button("Результат", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    
    keyboard.add_line()
    keyboard.add_button("Сообщить об ошибке и/или оставить отзыв", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)

    return keyboard.get_keyboard()


def create_keyboard_game():
    keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
    keyboard.add_button("Старт", color=vk_api.keyboard.VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Назад", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    
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


def create_keyboard_tasks_2():
    keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
    keyboard.add_button("4", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("8", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)    
    
    keyboard.add_line()
    keyboard.add_button("9", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("6", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)   
    
    return keyboard.get_keyboard()


def create_keyboard_tasks_3():
    keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
    keyboard.add_button("1", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("1,5", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)    
    
    keyboard.add_line()
    keyboard.add_button("2", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("2,5", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)   
    
    return keyboard.get_keyboard()


def create_keyboard_tasks_4():
    keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
    keyboard.add_button("0,4", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("0,2", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)    
    
    keyboard.add_line()
    keyboard.add_button("0,3", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("0,45", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)   
    
    return keyboard.get_keyboard()


def create_keyboard_tasks_5():
    keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
    keyboard.add_button("-13", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("13", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)    
    
    keyboard.add_line()
    keyboard.add_button("11", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("-12", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)   
    
    return keyboard.get_keyboard()


def create_keyboard_tasks_6():
    keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
    keyboard.add_button("60", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("30", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)    
    
    keyboard.add_line()
    keyboard.add_button("45", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("50", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)   
    
    return keyboard.get_keyboard()


def create_keyboard_tasks_7():
    keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
    keyboard.add_button("0", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("1", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)    
    
    keyboard.add_line()
    keyboard.add_button("2", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("3", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)   
    
    return keyboard.get_keyboard()


def create_keyboard_tasks_8():
    keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
    keyboard.add_button("4", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("8", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)    
    
    keyboard.add_line()
    keyboard.add_button("9", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("6", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)   
    
    return keyboard.get_keyboard()

def create_keyboard_tasks_9():
    keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
    keyboard.add_button("-6", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("-3", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)    
    
    keyboard.add_line()
    keyboard.add_button("3", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("6", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)   
    
    return keyboard.get_keyboard()

def create_keyboard_tasks_10():
    keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
    keyboard.add_button("90", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("120", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)    
    
    keyboard.add_line()
    keyboard.add_button("9", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("12", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)   
    
    return keyboard.get_keyboard()


def create_keyboard_tasks_11():
    keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
    keyboard.add_button("14", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("5", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)    
    
    keyboard.add_line()
    keyboard.add_button("9", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("20", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)   
    
    return keyboard.get_keyboard()


def create_keyboard_tasks_12():
    keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
    keyboard.add_button("-4", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("4", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)    
    
    keyboard.add_line()
    keyboard.add_button("-9", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("9", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)   
    
    return keyboard.get_keyboard()


def create_keyboard_tasks_ans():
    keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
    keyboard.add_button("Далее", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)  
    
    keyboard.add_line()
    keyboard.add_button("Назад", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)    


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
    photoss = []
    create = True
    task = False
    ans = False
    game = False
    ans1 = False
    ans2 = False
    ans3 = False
    ans4 = False
    ans5 = False
    ans6 = False
    ans7 = False
    ans8 = False
    ans9 = False
    ans10 = False
    ans11 = False
    ans12 = False
    otziv = False
    quest = False
    photoo = []
    num = -1
    ans_game = False
    login, password = '89605241010', 'Lihannna8'
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()    
    owner_id = -194171750
    album_id = '271712137'
    directory = 'C:/Users/hhh/Desktop/prog_3/ответ' #путь до папки с задачами
    files = os.listdir(directory)
    files = [i for i in files if i.endswith('.jpg') or i.endswith('.jpeg')]
    upload = vk_api.VkUpload(vk_session)
    for i in files:
        photo = upload.photo(f'{directory}/{i}', album_id=album_id, group_id='194171750')
        photos_count = vk.photos.get(owner_id=owner_id, album_id=album_id)
    for i in photos_count['items']:
        photoss.append(f"photo{owner_id}_{i['id']}")      
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
                quest = False
            elif "Сообщить об ошибке и/или оставить отзыв" == event.obj.message['text']:
                vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"Ждем ваших отзывов или предложений ☺", 
                             random_id=random.randint(0, 2 ** 64))
                otziv = True
            elif "Перейти к задачам" == event.obj.message['text']:
                keyboard1 = create_keyboard_tasks()
                vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"{fullname}, выбери задание", 
                             keyboard=keyboard1, 
                             random_id=random.randint(0, 2 ** 64))
                task = True
                quest = True
            elif "Результат" == event.obj.message['text']:
                people = Person.select().where(Person.name == fulname).get()  
                vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"""Имя - {people.name}
                             Правильных - {people.right}
                             Неверных - {people.wrong} 
                             Всего - {people.all}""", 
                             keyboard=keyboard, 
                             random_id=random.randint(0, 2 ** 64))       
                
            
            
            elif not ans_game and not task and not ans:
                vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"Администратор вскоре рассмотрит ваше сообщение ☺", 
                             keyboard=keyboard, 
                       random_id=random.randint(0, 2 ** 64))
            
                
            if ans:
                if ans1:
                    if "424,8" == event.obj.message['text']:
                        right_ans(fulname)
                        keyboard1 = create_keyboard_tasks()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                             message='Верно', 
                             keyboard=keyboard1, 
                             random_id=random.randint(0, 2 ** 64))
                        ans1 = False
                        ans = False
                        quest = True   
                        task = False
                    else:
                        wrong_ans(fulname)
                        keyboard_1 = create_keyboard_tasks_1()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                             message='Неверно', 
                             keyboard=keyboard_1,  
                             random_id=random.randint(0, 2 ** 64))
                        quest = False
                if ans2:
                    if "8" == event.obj.message['text']:
                        right_ans(fulname)
                        keyboard1 = create_keyboard_tasks()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                             message='Верно', 
                             keyboard=keyboard1, 
                             random_id=random.randint(0, 2 ** 64))
                        ans2 = False
                        ans = False
                        quest = True    
                        task = False
                    else:
                        wrong_ans(fulname)
                        keyboard_2 = create_keyboard_tasks_2()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                             message='Неверно', 
                             keyboard=keyboard_2,  
                             random_id=random.randint(0, 2 ** 64))
                        quest = False
                if ans3:
                    if "2,5" == event.obj.message['text']:
                        right_ans(fulname)
                        keyboard1 = create_keyboard_tasks()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                             message='Верно', 
                             keyboard=keyboard1, 
                             random_id=random.randint(0, 2 ** 64))
                        ans3 = False
                        ans = False
                        quest = True        
                        task = False
                    else:
                        wrong_ans(fulname)
                        keyboard_3 = create_keyboard_tasks_3()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                             message='Неверно', 
                             keyboard=keyboard_3,  
                             random_id=random.randint(0, 2 ** 64))
                        quest = False
                if ans4:
                    if "0,4" == event.obj.message['text']:
                        right_ans(fulname)
                        keyboard1 = create_keyboard_tasks()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                             message='Верно', 
                             keyboard=keyboard1, 
                             random_id=random.randint(0, 2 ** 64))
                        ans4 = False
                        ans = False
                        task = False
                        quest = True                        
                    else:
                        wrong_ans(fulname)
                        keyboard_4 = create_keyboard_tasks_4()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                             message='Неверно', 
                             keyboard=keyboard_4,  
                             random_id=random.randint(0, 2 ** 64))
                        quest = False
                if ans5:
                    if "13" == event.obj.message['text']:
                        right_ans(fulname)
                        keyboard1 = create_keyboard_tasks()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                             message='Верно', 
                             keyboard=keyboard1, 
                             random_id=random.randint(0, 2 ** 64))
                        ans5 = False
                        ans = False
                        task = False
                        quest = True                        
                    else:
                        wrong_ans(fulname)
                        keyboard_5 = create_keyboard_tasks_5()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                             message='Неверно', 
                             keyboard=keyboard_5,  
                             random_id=random.randint(0, 2 ** 64))
                        quest = False
                if ans6:
                    if "60" == event.obj.message['text']:
                        right_ans(fulname)
                        keyboard1 = create_keyboard_tasks()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                             message='Верно', 
                             keyboard=keyboard1, 
                             random_id=random.randint(0, 2 ** 64))
                        ans6 = False
                        ans = False
                        task = False
                        quest = True                        
                    else:
                        wrong_ans(fulname)
                        keyboard_6 = create_keyboard_tasks_6()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                             message='Неверно', 
                             keyboard=keyboard_6,  
                             random_id=random.randint(0, 2 ** 64))
                        quest = False
                if ans7:
                    if "1" == event.obj.message['text']:
                        right_ans(fulname)
                        keyboard1 = create_keyboard_tasks()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                             message='Верно', 
                             keyboard=keyboard1, 
                             random_id=random.randint(0, 2 ** 64))
                        ans7 = False
                        ans = False
                        quest = True               
                        task = False
                    else:
                        wrong_ans(fulname)
                        keyboard_7 = create_keyboard_tasks_7()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                             message='Неверно', 
                             keyboard=keyboard_7,  
                             random_id=random.randint(0, 2 ** 64))
                        quest = False
                if ans8:
                    if "6" == event.obj.message['text']:
                        right_ans(fulname)
                        keyboard1 = create_keyboard_tasks()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                             message='Верно', 
                             keyboard=keyboard1, 
                             random_id=random.randint(0, 2 ** 64))
                        ans8 = False
                        ans = False
                        task = False
                        quest = True                        
                    else:
                        wrong_ans(fulname)
                        keyboard_8 = create_keyboard_tasks_8()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                             message='Неверно', 
                             keyboard=keyboard_8,  
                             random_id=random.randint(0, 2 ** 64))
                        quest = False
                if ans9:
                    if "-6" == event.obj.message['text']:
                        right_ans(fulname)
                        keyboard1 = create_keyboard_tasks()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                             message='Верно', 
                             keyboard=keyboard1, 
                             random_id=random.randint(0, 2 ** 64))
                        ans9 = False
                        ans = False
                        quest = True        
                        task = False
                    else:
                        wrong_ans(fulname)
                        keyboard_9 = create_keyboard_tasks_9()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                             message='Неверно', 
                             keyboard=keyboard_9,  
                             random_id=random.randint(0, 2 ** 64))
                        quest = False
                if ans10:
                    if "12" == event.obj.message['text']:
                        right_ans(fulname)
                        keyboard1 = create_keyboard_tasks()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                             message='Верно', 
                             keyboard=keyboard1, 
                             random_id=random.randint(0, 2 ** 64))
                        ans10 = False
                        task = False
                        ans = False
                        quest = True                        
                    else:
                        wrong_ans(fulname)
                        keyboard_10 = create_keyboard_tasks_10()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                             message='Неверно', 
                             keyboard=keyboard_10,  
                             random_id=random.randint(0, 2 ** 64))
                        quest = False
                if ans11:
                    if "9" == event.obj.message['text']:
                        right_ans(fulname)
                        keyboard1 = create_keyboard_tasks()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                             message='Верно', 
                             keyboard=keyboard1, 
                             random_id=random.randint(0, 2 ** 64))
                        ans11 = False
                        ans = False
                        task = False
                        quest = True                        
                    else:
                        wrong_ans(fulname)
                        keyboard_11 = create_keyboard_tasks_11()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                             message='Неверно', 
                             keyboard=keyboard_11,  
                             random_id=random.randint(0, 2 ** 64))
                        quest = False
                if ans12:
                    if "4" == event.obj.message['text']:
                        right_ans(fulname)
                        keyboard1 = create_keyboard_tasks()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                             message='Верно', 
                             keyboard=keyboard1, 
                             random_id=random.randint(0, 2 ** 64))
                        ans12 = False
                        task = False
                        ans = False
                        quest = True                        
                    else:
                        wrong_ans(fulname)
                        keyboard_12 = create_keyboard_tasks_12()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                             message='Неверно', 
                             keyboard=keyboard_12,  
                             random_id=random.randint(0, 2 ** 64))
                        quest = False
            if quest and not task:
                keyboard1 = create_keyboard_tasks()
                vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"{fullname}, выбери задание", 
                             keyboard=keyboard1, 
                             random_id=random.randint(0, 2 ** 64))
                task = True
            elif task and quest:          
                if "1" == event.obj.message['text']:
                    keyboard_1 = create_keyboard_tasks_1()
                    vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"vk.com/{photoss[0]}", 
                             keyboard=keyboard_1, 
                             random_id=random.randint(0, 2 ** 64))
                    ans = True
                    ans1 = True
                    task = False
                if "2" == event.obj.message['text']:
                    keyboard_2 = create_keyboard_tasks_2()
                    vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"vk.com/{photoss[1]}", 
                             keyboard=keyboard_2, 
                             random_id=random.randint(0, 2 ** 64))
                    ans = True
                    ans2 = True
                    task = False
                if "3" == event.obj.message['text']:
                    keyboard_3 = create_keyboard_tasks_3()
                    vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"vk.com/{photoss[2]}", 
                             keyboard=keyboard_3, 
                             random_id=random.randint(0, 2 ** 64))
                    ans = True
                    ans3 = True
                    task = False
                if "4" == event.obj.message['text']:
                    keyboard_4 = create_keyboard_tasks_4()
                    vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"vk.com/{photoss[3]}", 
                             keyboard=keyboard_4, 
                             random_id=random.randint(0, 2 ** 64))
                    ans = True
                    ans4 = True
                    task = False
                if "5" == event.obj.message['text']:
                    keyboard_5 = create_keyboard_tasks_5()
                    vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"vk.com/{photoss[4]}", 
                             keyboard=keyboard_5, 
                             random_id=random.randint(0, 2 ** 64))
                    ans = True
                    ans5 = True
                    task = False
                if "6" == event.obj.message['text']:
                    keyboard_6 = create_keyboard_tasks_6()
                    vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"vk.com/{photoss[5]}", 
                             keyboard=keyboard_6, 
                             random_id=random.randint(0, 2 ** 64))
                    ans = True
                    ans6 = True
                    task = False
                if "7" == event.obj.message['text']:
                    keyboard_7 = create_keyboard_tasks_7()
                    vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"vk.com/{photoss[6]}", 
                             keyboard=keyboard_7, 
                             random_id=random.randint(0, 2 ** 64))
                    ans = True
                    ans7 = True
                    task = False
                if "8" == event.obj.message['text']:
                    keyboard_8 = create_keyboard_tasks_8()
                    vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"vk.com/{photoss[7]}", 
                             keyboard=keyboard_8, 
                             random_id=random.randint(0, 2 ** 64))
                    ans = True
                    ans8 = True
                    task = False
                if "9" == event.obj.message['text']:
                    keyboard_9 = create_keyboard_tasks_9()
                    vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"vk.com/{photoss[8]}", 
                             keyboard=keyboard_9, 
                             random_id=random.randint(0, 2 ** 64))
                    ans = True
                    ans9 = True
                    task = False
                if "10" == event.obj.message['text']:
                    keyboard_10 = create_keyboard_tasks_10()
                    vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"vk.com/{photoss[9]}", 
                             keyboard=keyboard_10, 
                             random_id=random.randint(0, 2 ** 64))
                    ans = True
                    ans10 = True
                    task = False
                if "11" == event.obj.message['text']:
                    keyboard_11 = create_keyboard_tasks_11()
                    vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"vk.com/{photoss[10]}", 
                             keyboard=keyboard_11, 
                             random_id=random.randint(0, 2 ** 64))
                    ans = True
                    ans11 = True
                    task = False
                if "12" == event.obj.message['text']:
                    keyboard_12 = create_keyboard_tasks_12()
                    vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"vk.com/{photoss[11]}", 
                             keyboard=keyboard_12, 
                             random_id=random.randint(0, 2 ** 64))
                    ans = True
                    ans12 = True
                    task = False
            
    

if __name__ == '__main__':  
    main()
    from waitress import serve
    serve(app, host="127.0.0.1", port=8080)         