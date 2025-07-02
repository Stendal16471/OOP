class Student:
    """A class to represent the student.

    Attributes:
        name (str): student's name
        surname (str): student's surname
        gender (str): student's gender
        finished_courses (List[str]): list of completed courses
        courses_in_progress (List[str]): list of current courses
        grades (Dict[str, List[int]]): dictionary with course grades
    """
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        """Evaluates the teacher's lecture.

        Args:
            lecturer: teacher's object
            course: course name
            grade: rating (from 1 to 10)

        Returns:
            str: an error message or teacher's assessment by a student if successful
        """
        if not (1 <= grade <= 10):
            return "Ошибка: оценка должна быть от 1 до 10"

        if (isinstance(lecturer, Lecturer)
                and course in lecturer.courses_attached
                and course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
            return (f"Студент {self.name} оценил лектора {lecturer.name} "
                    f"по курсу {course} на {grade}")
        else:
            return 'Ошибка'

    def __str__(self):
        avg_grade = self.get_avg_grade()
        in_progress = ', '.join(self.courses_in_progress) if self.courses_in_progress \
            else "курсов нет"
        finished = ', '.join(self.finished_courses) if self.finished_courses \
            else "курсов нет"
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {avg_grade:.1f}\n'
                f'Курсы в процессе изучения: {in_progress}\n'
                f'Завершенные курсы: {finished}')

    def get_avg_grade(self):
        """Calculates the average grade for all courses."""
        if not self.grades:
            return 0
        all_grades = [grade for course_grades in self.grades.values()
                      for grade in course_grades]
        return sum(all_grades) / len(all_grades)

    # Comparison using magical methods

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_avg_grade() < other.get_avg_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_avg_grade() <= other.get_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_avg_grade() == other.get_avg_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_avg_grade() > other.get_avg_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_avg_grade() >= other.get_avg_grade()

    def __ne__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_avg_grade() != other.get_avg_grade()


class Mentor:
    """Basic class for mentors.

    Attributes:
        name (str): mentor's name
        surname (str): mentor's surname
        courses_attached (List[str]): list of attached courses
    """
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """A class to introduce the lecturer.

    Attributes:
        grades (Dict[str, List[int]]): dictionary with course grades
    """
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = self.get_avg_grade()
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {avg_grade:.1f}')

    def get_avg_grade(self):
        """Calculates the average grade for lectures."""
        if not self.grades:
            return 0
        all_grades = [grade for course_grades in self.grades.values()
                      for grade in course_grades]
        return sum(all_grades) / len(all_grades)

    # Comparison using magical methods

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_avg_grade() < other.get_avg_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_avg_grade() <= other.get_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_avg_grade() == other.get_avg_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_avg_grade() > other.get_avg_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_avg_grade() >= other.get_avg_grade()

    def __ne__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_avg_grade() != other.get_avg_grade()


class Reviewer(Mentor):
    """A class for homework examiners."""
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        """Gives a student a grade for their homework.

        Args:
            student: student's Object
            course: course name
            grade: rating (from 1 to 10)

        Returns:
            str: an error message or the student's evaluation by the checker upon success
        """
        if not (1 <= grade <= 10):
            return "Ошибка: оценка должна быть от 1 до 10"
        if (isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            return (f"Проверяющий {self.name} оценил студента {student.name} "
                    f"по курсу {course} на {grade}")
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def calculate_avg_hw_grade(students, course_name):
    """Calculates the average grade for homework assignments for all students in a particular course.

    Args:
        students: list of objects Student
        course_name: course name

    Returns:
        Average grade for the course or 0 if there are no grades
    """
    total_grades = []

    for student in students:
        if course_name in student.grades:
            total_grades.extend(student.grades[course_name])

    if not total_grades:
            return 0.0

    return round(sum(total_grades) / len(total_grades), 1)

def calculate_avg_lecture_grade(lecturers, course_name):
    """Calculates the average rating of lecturers for a specific course.

    Args:
        lecturers: list of objects Lecturers
        course_name: course name

    Returns:
        Average grade for the course or 0 if there are no grades
    """
    total_grades = []

    for lecturer in lecturers:
        if course_name in lecturer.grades:
            total_grades.extend(lecturer.grades[course_name])

    if not total_grades:
            return 0.0

    return round(sum(total_grades) / len(total_grades), 1)


# 4 задание
some_student_1 = Student('Марина', 'Иванова', 'Ж')
some_student_1.finished_courses = ['Git']
some_student_1.courses_in_progress = ['Python']
some_student_1.grades = {
    'Git': [6, 5, 8],
    'Python': [7, 9, 7]
}
some_student_2 = Student('Иван', 'Кириченко', 'М')
some_student_2.finished_courses = ['Python']
some_student_2.courses_in_progress = ['C++']
some_student_2.grades = {
    'Python': [4, 6, 9],
    'C++': [7, 6, 4]
}
print(some_student_1)
print()
print(some_student_2)
print()
some_lecturer_1 = Lecturer('Артем', 'Коновалов')
some_lecturer_1.courses_attached = ['Python']
some_lecturer_2 = Lecturer('Екатерина', 'Молчанова')
some_lecturer_2.courses_attached = ['C++']

result_1 = some_student_1.rate_lecture(some_lecturer_1, 'Python', 7)
result_2 = some_student_2.rate_lecture(some_lecturer_2, 'C++', 8)

print(result_1)
print(result_2)
print()
print(some_student_1.get_avg_grade())
print(some_student_2.get_avg_grade())
print()
print(some_student_1.get_avg_grade() < some_student_2.get_avg_grade())
print(some_student_1.get_avg_grade() > some_student_2.get_avg_grade())
print(some_student_1.get_avg_grade() <= some_student_2.get_avg_grade())
print(some_student_1.get_avg_grade() >= some_student_2.get_avg_grade())
print(some_student_1.get_avg_grade() == some_student_2.get_avg_grade())
print(some_student_1.get_avg_grade() != some_student_2.get_avg_grade())
print()

print(some_lecturer_1)
print()
print(some_lecturer_2)
print()

print(some_lecturer_1.get_avg_grade())
print(some_lecturer_2.get_avg_grade())
print()
print(some_lecturer_1.get_avg_grade() < some_lecturer_2.get_avg_grade())
print(some_lecturer_1.get_avg_grade() > some_lecturer_2.get_avg_grade())
print(some_lecturer_1.get_avg_grade() <= some_lecturer_2.get_avg_grade())
print(some_lecturer_1.get_avg_grade() >= some_lecturer_2.get_avg_grade())
print(some_lecturer_1.get_avg_grade() == some_lecturer_2.get_avg_grade())
print(some_lecturer_1.get_avg_grade() != some_lecturer_2.get_avg_grade())
print()

some_reviewer_1 = Reviewer('Ирина', 'Дмитриева')
some_reviewer_1.courses_attached = ['Python']
print()
some_reviewer_2 = Reviewer('Дмитрий', 'Мельников')
some_reviewer_2.courses_attached = ['C++']
print(some_reviewer_1)
print()
print(some_reviewer_2)
print()

result_1 = some_reviewer_1.rate_hw(some_student_1, 'Python', 7)
result_2 = some_reviewer_2.rate_hw(some_student_2, 'C++', 6)

print(result_1)
print(result_2)
print()

avg_grade_1 = calculate_avg_hw_grade([some_student_1, some_student_2], 'Python')
print(f"Средняя оценка студентов по курсу Python: {avg_grade_1:.1f}")
print()

some_lecturer_3 = Lecturer('Даниил', 'Мещанин')
some_lecturer_3.courses_attached = ['Python']
result_3 = some_student_1.rate_lecture(some_lecturer_3, 'Python', 3)

avg_grade_2 = calculate_avg_lecture_grade([some_lecturer_1, some_lecturer_3], 'Python')
print(f"Средняя оценка лекторов по курсу Python: {avg_grade_2:.1f}")

