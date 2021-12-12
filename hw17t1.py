def list2str(sourcelist):
    if len(sourcelist) == 0:
        return ""
    cur = ''
    for cc in sourcelist:
        cur += cc
        cur += ', '
    cc = list(cur)
    del (cc[len(cur) - 1])
    del (cc[len(cc) - 1])
    return "".join(cc)


def avrg_global(source_list):
    count = 0
    average = 0
    for v in source_list:
        count = count + 1
        average = average + v
    return average / count


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def avrg(self):
        count = 0
        average = 0
        for v in list(self.grades.values())[0]:
            count = count + 1
            average = average + v
        return average / count

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {round(avrg_global(list(self.grades.values())[0]),1)}\n' \
              f'Курсы в процессе изучения: {list2str(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {list2str(self.finished_courses)}'

    def __lt__(self, other):
        if isinstance(other, Student):
            if self.avrg() < other.avrg():
                return True
        return False

    def __gt__(self, other):
        if isinstance(other, Student):
            if self.avrg() > other.avrg():
                return True
        return False

    def __ge__(self, other):
        if isinstance(other, Student):
            if self.avrg() >= other.avrg():
                return True
        return False

    def __le__(self, other):
        if isinstance(other, Student):
            if self.avrg() <= other.avrg():
                return True
        return False

    def __eq__(self, other):
        if isinstance(other, Student):
            if self.avrg() == other.avrg():
                return True
        return False

    def __ne__(self, other):
        if isinstance(other, Student):
            if self.avrg() != other.avrg():
                return True
        return False

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and 0 < grade <= 10:
            if course in lecturer.courses_attached and course in self.courses_in_progress:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {round(avrg_global(list(self.grades.values())[0]),1)}'

    def avrg(self):
        count = 0
        average = 0
        for v in list(self.grades.values())[0]:
            count = count + 1
            average = average + v
        return average / count

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            if self.avrg() < other.avrg():
                return True
        return False

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            if self.avrg() > other.avrg():
                return True
        return False

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            if self.avrg() >= other.avrg():
                return True
        return False

    def __le__(self, other):
        if isinstance(other, Lecturer):
            if self.avrg() <= other.avrg():
                return True
        return False

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            if self.avrg() == other.avrg():
                return True
        return False

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            if self.avrg() != other.avrg():
                return True
        return False


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


student1 = Student('Павел', 'Иванов', 'male')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']

student2 = Student('Ольга', 'Вывертова', 'female')
student2.courses_in_progress += ['Python']
student2.add_courses('English')

l1 = Lecturer('Иван', 'Иванов')
l1.courses_attached += ['Python']
l1.courses_attached += ['Git']

l2 = Lecturer('Светлана','Светова')
l2.courses_attached += ['Python']

student1.rate_lecturer(l1,'Python',10)
student1.rate_lecturer(l1,'Python',7)
student1.rate_lecturer(l1,'Git',5)

student2.rate_lecturer(l2,'Python',8)
student2.rate_lecturer(l2,'Python',9)


r1 = Reviewer('Петр', 'Петров')
r1.courses_attached += ['Python']
r1.rate_hw(student1, 'Python', 10)
r1.rate_hw(student1, 'Python', 8)
r1.rate_hw(student2, 'Python', 10)


print(l1)
print('---------------------')
print(r1)
print('---------------------')
print(student1)
print('')
print(student2)

if l1 == l2:
    print("Преподаватели равнозначны")
elif l1 > l2:
    print(f'{l1.name} {l1.surname} лучше {l2.name} {l2.surname}')
elif l1 < l2:
    print(f'{l1.name} {l1.surname} хуже {l2.name} {l2.surname}')

print('\nСТУДЕНТЫ:')
if student1 == student2:
    print(f'Студенты {student1.name} {student1.surname} и {student2.name} {student2.surname} равнозначны')
elif student1 > student2:
    print(f'{student1.name} {student1.surname} лучше {student2.name} {student2.surname}')
elif student1 < student2:
    print(f'{student2.name} {student2.surname} лучше {student1.name} {student1.surname}')
