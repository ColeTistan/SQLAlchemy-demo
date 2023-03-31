from sqlalchemy import create_engine
from sqlalchemy import (
    ForeignKey,
    Column,
    String,
    Integer,
    CHAR
)
from config import (
    Base,
    session_config
)
from model import (
    Student,
    Course,
    StudentCourse
)

if __name__ == '__main__':
    engine = create_engine('sqlite:///studentcoursedb.db', echo=True)
    Base.metadata.create_all(bind=engine)
    
    session = session_config(engine)
    students = session.query(Student).all()
    courses = session.query(Course).all()
    student_courses = session.query(StudentCourse).all()

    results = session.query(Student, StudentCourse, Course).select_from(Student).join(StudentCourse).join(Course).all()

    for student, student_course, course in results:
        print(student, course)