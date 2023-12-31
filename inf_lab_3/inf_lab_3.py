import re
#Зададние 1
print("Задание 1")
def first_exr(inputt):
    res = re.findall(r':-/', inputt)
    if res:
        print(len(res))

#ТЕСТЫ ДЛЯ ЗАДАНИЯ 1
first_exr("[:-/!]:(:-/)")       #Правильный ответ - 2
first_exr("(!*@@:@:)-/:-/")     #Правильный ответ - 1
first_exr("*(!:-/):-/\"")       #Правильный ответ - 2
first_exr("$!:;!(:-/)")         #Правильный ответ - 1
first_exr("#%$^%&^&^&%^")       #Правильный ответ - 2
print()

#Задание 2
print("Задание 2.")
pattern1 = re.compile(r'^([^аеёиоуыэюя]*[аеёиоуыэюя]){5}[^аеёиоуыэюя]*$', re.IGNORECASE)
pattern2 = re.compile(r'^([^аеёиоуыэюя]*[аеёиоуыэюя]){7}[^аеёиоуыэюя]*$', re.IGNORECASE)

def test(tests):
    spisok = re.split(r'/', tests)
    if len(spisok) != 3:
        print("Не хайку. Должно быть 3 строки")
    else:
        if re.search(pattern1, spisok[0]) and re.search(pattern2, spisok[1]) and re.search(pattern1, spisok[2]):
            print("Хайку!")
        else:
            print("Не хайку.")
            
#ТЕСТЫ ДЛЯ ЗАДАНИЯ 2
test("На голой ветке / Сидит синица смело / Метель и буря...")              #Правильный ответ - Хайку!
test("Я еще молод / Люблю гулять и бегать / Хочу сильно спать")             #Правильный ответ - Хайку!
test("Вечереет за окном. / Еще один день прожит. / Жизнь скоротечна...")    #Правильный ответ - Не хайку.
test("Я я я я я / Я я я я я я я / Я я я я я")                               #Правильный ответ - Хайку!
test("Вечер за окном. / Еще один день прожит.")                             #Правильный ответ - Не хайку. Должно быть 3 строчки
print()

#Задание 3
print("Задание 3.")
def mail_server(mail):
    rr = r'[\w.]+@(\w+\.\w+)'
    match = re.match(rr, mail)
    if match:
        return match.group(1)
    else:
        return "Fail!"
    
#ТЕСТЫ ДЛЯ ЗАДАНИЯ 3
mail1 = "students.spam@yandex.ru"   #Правильный ответ - yandex.ru
mail2 = "test"                      #Правильный ответ - Fail! 
mail3 = "@yandex.ru"                #Правильный ответ - Fail!
mail4 = "studs.spam@yandex"         #Правильный ответ - Fail!
mail5 = "test@.ru"                  #Правильный ответ - Fail!
print(mail_server(mail1))
print(mail_server(mail2))
print(mail_server(mail3))
print(mail_server(mail4))
print(mail_server(mail5))