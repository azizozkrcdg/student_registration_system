import sqlite3

database_connect = sqlite3.connect("studens_registration_system.db")
cursor = database_connect.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS students (ogr_no INT, ogr_adi TEXT, ogr_soyadi TEXT, ogr_bolum TEXT)")

class Student:
    def __init__(self):
       print("""
        1 - Öğrenci Ekle
        2 - Öğrenci Sil
        3 - Öğrenci Güncelle
        4 - Öğrencileri Görüntüle
        0 - Çıkış
       """)
       selected = int(input("Yapmak istediğiniz işlemi seçiniz : "))

       if selected == 1:
           self.add_student()
       elif selected == 2:
           self.delete_student()
       elif selected == 3:
           self.update_student()
       elif selected == 4:
            self.get_student_info()
       elif selected == 0:
           exit()
       else:
           print("Lütfen geçerli bir işlem seçin!")    
           

    # öğrenci ekleme işlemleri
    def add_student(self):
        self.std_no = input("Öğrenci No : ")
        self.std_name = input("Öğrenci Adı : ")
        self.std_surname = input("Öğrenci Soyadı : ")
        self.std_department = input("Öğrenci Bölümü : ")
             
        cursor.execute(f"INSERT INTO students VALUES ({self.std_no}, {self.std_name}, {self.std_surname}, {self.std_department})")
        database_connect.commit()
        print("Öğrenci başarıyla eklendi!")
    
    # öğrenci silme işlemleri
    def delete_student(self):

        del_std_no = input("Silmek istediğiniz öğrencinin numarasını giriniz : ")
        cursor.execute(f"DELETE FROM students WHERE ogr_no = {del_std_no}")
        database_connect.commit()
        print("Öğrenci başarıyla silindi!")
    
    # öğrenci güncelleme işlemleri
    def update_student(self):
        query_number = input("Güncellemek istediğiniz öğrencinin numarasını giriniz : ")
        cursor.execute(f"SELECT ogr_no FROM students WHERE ogr_no = {query_number}")
        number_to_change = cursor.fetchall()
        for i in number_to_change:
            number_to_change = i[0]

        column_to_change = input("Değiştirilecek sütun adını girin : ")
        new_value = input("Hangi değer ile güncellemek istiyorsunuz : ")

        cursor.execute(f"UPDATE students SET {column_to_change} = {new_value} WHERE ogr_no = {number_to_change}")
        database_connect.commit()
        print("Bilgiler başarıyla güncellendi!")
        
    # öğrencileri görüntülem işlemleri
    def get_student_info(self):
        cursor.execute(f"SELECT * FROM students")
        students_list = cursor.fetchall()
        for student in students_list:
            print(student)
    


Student()
database_connect.close()


