import sqlite3


# создание класса БД
class Sport:
    # конструктор класса
    def __init__(self):

                # Подключение к БД
                self.con = sqlite3.connect("Sport.db")
                # Создание курсора
                self.cur = self.con.cursor()
                # Создание таблицы БД
                self.cur.execute(
                "CREATE TABLE IF NOT EXISTS Sportman "
                "(ID INTEGER PRIMARY KEY,"
                "name_sport TEXT,"
                "unit_of_measurement INTEGER,"
                "world_record TEXT,"
                "record_date INTEGER,"
                "The_athlete's_full_name TEXT)"

                )
               self.con.commit()

def __del__(self):
  # отключение от БД
  self.con.close()

def view(self):
  # просмотр всех записей в таблице БД
  self.cur.execute("SELECT * FROM Sportman")
  # список всех записей из таблицы
  rows = self.cur.fetchall()
  return rows

def insert(self, name_sport, unit_of_measurement,world_record,record_date,The_athlete's_full_name):
  # добавить запись
  self.cur.execute("INSERT INTO Sportman "
                  "VALUES (NULL, ?, ?, ?,?,?)",
                  (name_sport, unit_of_measurement,world_record,record_date,The_athlete's_full_name,))
  self.con.commit()

def update(self, id, name_sport, unit_of_measurement,world_record,record_date,The_athlete's_full_name):
    # редактирование записи
    self.cur.execute("UPDATE Sportman SET "
                    "name_sport=?, unit_of_measurement=?,world_record=?,record_date=?,The_athlete's_full_name=? "
                    "WHERE ID = ?",
                    (name_sport, unit_of_measurement,
                   world_record,record_date,The_athlete's_full_name, id,))
    self.con.commit()

def delete(self, id):
    # удаление записи
    self.cur.execute("DELETE FROM Sportman "
                    "WHERE ID=?", (id,))
    self.con.commit()

def search(self, name_sport):
    self.cur.execute("SELECT unit_of_measurement,world_record,record_date,The_athlete's_full_nameFROM Sportman "
                    "WHERE name_sport=?", (name_sport,))
    rows = self.cur.fetchall()
    return rows
