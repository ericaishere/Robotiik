# [SOAL NOMOR 2]Buat hierarki kelas untuk sistem universitas. 
# Sistem harus memiliki kelas dasar untuk seseorang, dengan kelas turunan untuk siswa dan profesor. 
# Kelas siswa harus memiliki variabel instan untuk nama, nomor ID, dan daftar mata kuliah. 
# Kelas profesor harus memiliki variabel instan untuk nama, nomor ID, dan daftar mata kuliah yang diajarkan. 
# Hierarki kelas harus dibuat sehingga kode berikut dapat berjalan dan menghasilkan output berikut.


class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
        
class Student(Person):
    def __init__(self, name, id_number, courses=None):
        super().__init__(name, id_number)
        self.courses = courses or []
        
    def enroll(self, course):
        self.courses.append(course)
        
class Professor(Person):
    def __init__(self, name, id_number, courses_taught=None):
        super().__init__(name, id_number)
        self.courses_taught = courses_taught or []
        
    def assign_teaching(self, course):
        self.courses_taught.append(course)



s = Student("Alice", 1234, ["Introduction to Computer Science", "Data Structures"])
p = Professor("Bob", 5678, ["Database Systems", "Web Development"])
print(s.name, s.id_number, s.courses)
print(p.name, p.id_number, p.courses_taught)