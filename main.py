import sqlite3

class CreateTables: # Данный класс создает базу дунных и таблицы.
  def __init__(self):

    with sqlite3.connect('student_info.db') as self.__conn:
      self.__cur = self.__conn.cursor()

      self.__cur.execute(''' Create Table IF Not EXISTS Students (StudentID Integer Primary Key Not Null,
      Name Text,
      MajorID integer,
      DeptID integer,
      Foreign Key (MajorID) References Majors (MajorID),
      Foreign Key (DeptID) References Departments (DeptID) ) ''')

      self.__cur.execute(''' Create Table IF Not EXISTS Majors (MajorID Integer Primary Key Not Null,
      Name Text) ''')

      self.__cur.execute(''' Create Table IF Not EXISTS Departments (DeptID Integer Primary Key Not Null,
      Name Text)''')

class Majors (CreateTables): #Данный класс отвечает за работу с базой данных
  # таблицы Majors (Специальности).
  def __init__(self):
    CreateTables.__init__(self)

    with sqlite3.connect('student_info.db') as self.__conn:
      self.__cur = self.__conn.cursor()
      self.__cur.execute('PRAGMA Foreign_Keys=ON')

      self.__user_choice = 0
      UC_MIN = 1
      EXIT = 6

      while self.__user_choice != EXIT: #В данном цикле пользователь
        # взаимодействует с меню и выбирает нужный ему вариант.
        self.__show_menu()
        self.__user_choice = int(input('Введите пункт меню: '))
        print()

        if self.__user_choice == 1:
          major = input('Введите новую специальность: ')

          self.__cur.execute(''' Insert Into Majors (Name)
                Values (?)''',
                             (major,))
          print('Данные успешно добавлены.')
          print()

        if self.__user_choice == 2:
          ID = int (input('Введите ID специальности: '))
          self.__cur.execute('''  Select * From Majors Where MajorID == ? ''',
                             (ID,))

          results = self.__cur.fetchall()
          for row in results:
            print(f'Результаты поиска: {row[0]} {row[1]}')
          print()

        if self.__user_choice == 3:
          ID = int (input ('Введите существующий ID специальности: '))
          new_name = input ('Ведите новую специальность: ')

          self.__cur.execute(''' Update Majors Set Name = ? Where MajorID == ? ''',
                             (new_name,ID))

          results = self.__cur.rowcount
          if results > 0:
            print('Изменения успешно сохранены.')

          else:
            print('Такого ID не существует.')
          print()

        if self.__user_choice == 4:
          ID = input('Введите ID специальности который хотите удалить: ')
          self.__cur.execute(''' Select Name From Majors Where MajorID == ? ''',
                             (ID,))
          results = self.__cur.fetchone()

          if results != None:
            print(f'Проверьте данные: {results[0]}')
            choice = input('Вы действительно хотите удалить эту специальность? (д\н): ')
            if choice.lower() == 'д':
              self.__cur.execute(''' Delete From Majors Where MajorID == ?''',
                                 (ID,))
              print('Данные успешно удалены.')

          else:
            print(f'Такого ID: {ID} не существует.')

        if self.__user_choice == 5:
          self.__cur.execute(''' Select * From Majors ''')
          results = self.__cur.fetchall()

          for row in results:
            print(f'ID: {row[0]} Название: {row[1]}')
            print()

        if self.__user_choice < UC_MIN or self.__user_choice > EXIT:
          print('Введите пункт меню от 1 до 6.')
          print()

  def __show_menu(self):
    print('1. Добавить новую специальность')
    print('2. Найти специальность')
    print('3. Изменить специальность')
    print('4. Удалить специальность')
    print('5. Вывести на экран все специальности')
    print('6. Выйти из раздела специальности')

class Departments (CreateTables): # Данный класс отвечает за работу
  # с базой данных таблицы Departments (Факультеты).
  def __init__(self):
    CreateTables.__init__(self)

    with sqlite3.connect('student_info.db') as self.__conn:
      self.__cur = self.__conn.cursor()
      self.__cur.execute('PRAGMA Foreign_Keys=ON')

      self.__user_choice = 0
      UC_MIN = 1
      EXIT = 6

      while self.__user_choice != EXIT: #В данном цикле пользователь
        # взаимодействует с меню и выбирает нужный ему вариант.
        self.__show_menu()
        self.__user_choice = int(input('Введите пункт меню: '))
        print()

        if self.__user_choice == 1:
          department = input('Введите новый факультет: ')

          self.__cur.execute(''' Insert Into Departments (Name)
                      Values (?)''',
                             (department,))
          print('Данные успешно добавлены.')
          print()

        if self.__user_choice == 2:
          ID = int(input('Введите ID факультета: '))
          self.__cur.execute('''  Select * From Departments Where DeptID == ? ''',
                             (ID,))

          results = self.__cur.fetchall()
          for row in results:
            print(f'Результаты поиска: {row[0]} {row[1]}')
          print()

        if self.__user_choice == 3:
          ID = int(input('Введите существующий ID факультета: '))
          new_name = input('Введите новый факультет: ')

          self.__cur.execute(''' Update Departments Set Name = ? Where DeptID == ? ''',
                             (new_name, ID))

          results = self.__cur.rowcount
          if results > 0:
            print('Изменения успешно сохранены.')

          else:
            print('Такого ID не существует.')
          print()

        if self.__user_choice == 4:
          ID = input('Введите ID факультета который хотите удалить: ')
          self.__cur.execute(''' Select Name From Departments Where DeptID == ? ''',
                             (ID,))
          results = self.__cur.fetchone()

          if results != None:
            print(f'Проверьте данные: {results[0]}')
            choice = input('Вы действительно хотите удалить эту специальность? (д\н): ')
            if choice.lower() == 'д':
              self.__cur.execute(''' Delete From Departments Where DeptID == ?''',
                                 (ID,))
              print('Данные успешно удалены.')

          else:
            print(f'Такого ID: {ID} не существует.')

        if self.__user_choice == 5:
          self.__cur.execute(''' Select * From Departments ''')
          results = self.__cur.fetchall()

          for row in results:
            print(f'ID: {row[0]} Название: {row[1]}')
            print()

        if self.__user_choice < UC_MIN or self.__user_choice > EXIT:
          print('Введите пункт меню от 1 до 6.')
          print()

  def __show_menu(self):
    print('1. Добавить новый факультет')
    print('2. Найти факультет')
    print('3. Изменить факультет')
    print('4. Удалить факультет')
    print('5. Вывести на экран все факультеты')
    print('6. Выйти из раздела факультеты')


class Students (CreateTables): #Данный класс отвечает за работу с базой данных
  # таблицы Students (Студенты) Также данный класс имеет внешнии ключи для получения
  # данных из таблицы Majors и Departments.
  def __init__(self):
    CreateTables.__init__(self)

    with sqlite3.connect('student_info.db') as self.__conn:
      self.__cur = self.__conn.cursor()
      self.__cur.execute('PRAGMA Foreign_Keys=ON')

      try:
        self.__user_choice = 0
        UC_MIN = 1
        EXIT = 6

        while self.__user_choice != EXIT:
          self.__show_menu()
          self.__user_choice = int(input('Введите пункт меню: '))
          print()

          if self.__user_choice == 1:
            student_name = input('Введите имя\фамилию нового студента: ')
            major_id = int (input('Введите ID специальности студента: '))
            dept_id = int (input('Введите ID факультета студента: '))

            self.__cur.execute(''' Insert Into Students (Name,MajorID,DeptID)
                      Values (?,?,?)''',
                             (student_name,major_id,dept_id))
            print('Данные успешно добавлены.')
            print()

          if self.__user_choice == 2:
            ID = int (input('Введите ID студента: '))
            self.__cur.execute('''  Select * From Students Where StudentID == ? ''',
                             (ID,))

            results = self.__cur.fetchall()
            for row in results:
              print(f'Результаты поиска: {row[0]} {row[1]} {row[2]} {row[3]}')
            print()

          if self.__user_choice == 3:
            ID = int (input('Введите существующий ID студента: '))
            new_name = input('Введите новые имя\фамилию студента: ')
            new_major = int (input('Введите новый ID специальности студента: '))
            new_dept = int (input('Введите новый ID факультета студента: '))

            self.__cur.execute(''' Update Students Set Name = ?,MajorID = ?,DeptID = ?
            Where StudentID == ? ''',
                             (new_name,new_major,new_dept, ID))

            results = self.__cur.rowcount
            if results > 0:
              print('Изменения успешно сохранены.')

            else:
              print(f'Такого ID: {ID} не существует.')
            print()

          if self.__user_choice == 4:
            ID = input('Введите ID студента данные о ком хотите удалить: ')
            self.__cur.execute(''' Select Name From Students Where StudentID == ? ''',
                             (ID,))
            results = self.__cur.fetchone()

            if results != None:
              print(f'Проверьте данные: {results[0]}')
              choice = input('Вы действительно хотите удалить этого студента? (д\н): ')

              if choice.lower() == 'д':
                self.__cur.execute(''' Delete From Students Where StudentID == ?''',
                                 (ID,))
                print('Данные успешно удалены.')
                print()

            else:
              print(f'Такого ID: {ID} не существует.')

          if self.__user_choice == 5:
            self.__cur.execute(''' Select Students.StudentID,Students.Name,Majors.Name,Departments.Name
            From Students,Majors,Departments 
            Where Students.MajorID == Majors.MajorID AND Students.DeptID == Departments.DeptID''')
            results = self.__cur.fetchall()

            for row in results:
              print(f'ID: {row[0]} || ФИО студента: {row[1]} || Специальность: {row[2]} || Факультет: {row[3]}')
              print()

          if self.__user_choice < UC_MIN or self.__user_choice > EXIT:
            print('Введите пункт меню от 1 до 6.')
            print()

      except sqlite3.Error as err:
        print(f'Произошла ошибка {err} проверьте введенные данные и попробуйте снова.')
        print()

  def __show_menu(self):
    print('1. Добавить данные о новом студенте')
    print('2. Найти студента')
    print('3. Изменить данные о студенте')
    print('4. Удалить все данные о студенте')
    print('5. Вывести на экран информацию о всех студентах')
    print('6. Выйти из раздела студенты')

# В нашей точке входа выбираем создаем нашу базу данных с таблицами
# и выбираем нужный нам вариант меню для работы с нашими таблицами.
if __name__ == '__main__':
    create = CreateTables()
    min_choice = 1
    choice = 0
    EXIT = 4
    while choice != EXIT:
      print('Добро пожаловать в программу по работе с базой данных о студентах.')
      print('1. Специальности')
      print('2. Факультеты')
      print('3. Студенты')
      print('4. Выйти из программы')
      print()
      choice = int (input('Введите необходимый вариант: '))

      if choice == 1:
        majors = Majors()

      if choice == 2:
        departments = Departments()

      if choice == 3:
        students = Students()

      if choice < min_choice or choice > EXIT:
        print('Введите допустимые варианты 1-4.')
        print()