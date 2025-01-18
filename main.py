from peewee import *
from database.students.names import Student
from dateutil import parser
from datetime import datetime
from random import randint

Student.create_table()

class Database:
    def __init__(self, students):
        # экземпляры модели затабазы
        self.students = students

    def create_new_student(self,full_name:str, birthday:'str'):
        # дата рождения соответствует нужному формату
        try:
            bday = parser.parse(birthday).date()
        except Exception as ex:
            print('Приведите формат даты в надлежащий вид : день.месяц.год. (дд.мм.ГГГГ)')
            return ex

        # проверяем есть ли такой студент в базе
        st = self.students
        try:
            check = st.select().where(
                (st.full_name == full_name) & (st.birthday == bday)
            ).get()
            if check:
                match = f'Проверка: Такой ученику уже есть в базе. ({full_name}, {bday})'
                print(match)
                return match
        except Exception as ex:
            print(f'Проверка: Такого ученика в базе еще нет, продолжаю создание записи... ({full_name}, {bday})')

        # подготовка данных для загрузки в базу данных
        family_name, name, surname = full_name.split(' ')
        id = randint(1000000,9999999)

        # создание записи
        st.create(
                id=id,
                full_name=full_name,
                birthday=bday,
                name=name,
                family_name=family_name,
                surname=surname
        )
        print(f'Создана новая запись в базе данных:\n'
              f'Идентификатор: {id}\n'
              f'Полное имя: {full_name}\n'
              f'Дата рождения: {bday}\n'
              f'Имя: {name}\n'
              f'Фамилия: {family_name}\n'
              f'Отчество: {surname}\n')
        return


db = Database(Student)

db.create_new_student('Малахов Илья Витальевич', '8.09.2006')

