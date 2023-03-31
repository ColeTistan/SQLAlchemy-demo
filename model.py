from sqlalchemy import (
    ForeignKey,
    Column,
    String,
    Integer,
    CHAR
)
from config import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column('id', Integer, primary_key=True, unique=True, nullable=False)
    first_name = Column('first_name', String, nullable=False)
    last_name = Column('last_name', String, nullable=False)
    major = Column('major', String, nullable=False)
    year = Column('year', CHAR, nullable=False)
    gender = Column('gender', CHAR, nullable=False)
    age = Column('age', Integer, nullable=False)

    def __init__(self, id, first_name, last_name, major, year, gender, age):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.year = year
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f'{self.id}: {self.first_name} {self.last_name} ({self.gender}, {self.age}, {self.major}, {self.year})'
    
class StudentCourse(Base):
    __tablename__ = 'student_courses'

    id = Column('id', Integer, primary_key=True, unique=True, nullable=False)
    student_id = Column('student_id', Integer, ForeignKey('students.id'), nullable=False)
    course_id = Column('course_id', Integer, ForeignKey('courses.id'), nullable=False)

    def __init__(self, id, student_id, course_id):
        self.id = id
        self.student_id = student_id
        self.course_id = course_id

    def __repr__(self):
        return f'{self.id}: Student ID {self.student_id} - Course ID {self.course_id}'

class Course(Base):
    __tablename__ = 'courses'

    id = Column('id', Integer, primary_key=True, unique=True, nullable=False)
    course_title = Column('course_title', String, nullable=False)
    course_subject = Column('course_subject', String, nullable=False)
    num_of_credits = Column('num_of_credits', Integer, nullable=False)
    crn_number = Column('crn_number', Integer, nullable=False)

    def __init__(self, id, course_title, course_subject, num_of_credits, crn_number):
        self.id = id
        self.course_title = course_title
        self.course_subject = course_subject
        self.num_of_credits = num_of_credits
        self.crn_number = crn_number

    def __repr__(self):
        return f'{self.id}: ({self.course_title}, {self.course_subject}, {self.num_of_credits}, {self.crn_number})'
    
