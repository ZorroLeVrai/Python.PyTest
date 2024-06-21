import pytest
from source.school import Classroom, Teacher, Student, TooManyStudents

@pytest.fixture
def initial_setup():
    teacher = Teacher(name="Minerva McGonagall")
    students = [
        Student(name="Harry Potter"),
        Student(name="Hermione Granger"),
        Student(name="Ron Weasley")
    ]
    course_title = "Defense Against the Dark Arts"
    classroom = Classroom(teacher, students, course_title)
    return classroom

def test_add_student(initial_setup):
    classroom = initial_setup
    new_student = Student(name="Draco Malfoy")
    classroom.add_student(new_student)
    assert new_student in classroom.students

def test_add_student_limit(initial_setup):
    classroom = initial_setup
    additional_students = [
        Student(name="Neville Longbottom"),
        Student(name="Luna Lovegood"),
        Student(name="Ginny Weasley"),
        Student(name="Fred Weasley"),
        Student(name="George Weasley"),
        Student(name="Cho Chang"),
        Student(name="Cedric Diggory")
    ]
    
    for student in additional_students:
        classroom.add_student(student)
        
    with pytest.raises(TooManyStudents):
        classroom.add_student(Student(name="Pansy Parkinson"))

def test_remove_student(initial_setup):
    classroom = initial_setup
    classroom.remove_student("Ron Weasley")
    assert not any(student.name == "Ron Weasley" for student in classroom.students)

def test_change_teacher(initial_setup):
    classroom = initial_setup
    new_teacher = Teacher(name="Severus Snape")
    classroom.change_teacher(new_teacher)
    assert classroom.teacher.name == "Severus Snape"

@pytest.mark.parametrize("student_name", [
    ("Sirius Black"),
    ("Remus Lupin"),
    ("Peter Pettigrew")
])
def test_add_various_students(initial_setup, student_name):
    classroom = initial_setup
    new_student = Student(name=student_name)
    classroom.add_student(new_student)
    assert new_student in classroom.students

@pytest.mark.parametrize("teacher_name", [
    ("Albus Dumbledore"),
    ("Rubeus Hagrid"),
    ("Dolores Umbridge")
])
def test_change_various_teachers(initial_setup, teacher_name):
    classroom = initial_setup
    new_teacher = Teacher(name=teacher_name)
    classroom.change_teacher(new_teacher)
    assert classroom.teacher.name == teacher_name
