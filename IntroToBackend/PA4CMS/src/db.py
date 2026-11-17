from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

students = db.Table(
    "students",
    db.Column("course_id", db.Integer, db.ForeignKey("course.id"), primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
)

instructors = db.Table(
    "instructors",
    db.Column("course_id", db.Integer, db.ForeignKey("course.id"), primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
)


class Course(db.Model):
    """A course with assignments, students, and instructors."""

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    assignments = db.relationship(
        "Assignment", back_populates="course", cascade="all, delete-orphan",
        order_by="Assignment.id",
    )
    students = db.relationship(
        "User", secondary=students, back_populates="student_courses",
        order_by="User.id",
    )
    instructors = db.relationship(
        "User", secondary=instructors, back_populates="instructor_courses",
        order_by="User.id",
    )

    def simple_serialize(self):
        """Return course details without relationships to prevent recursion."""
        return {"id": self.id, "code": self.code, "name": self.name}

    def serialize(self):
        """Return the course and its immediate relationships."""
        return {
            **self.simple_serialize(),
            "assignments": [item.simple_serialize() for item in self.assignments],
            "students": [user.simple_serialize() for user in self.students],
            "instructors": [user.simple_serialize() for user in self.instructors],
        }


class User(db.Model):
    """A user who can be a student, an instructor, or both."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    netid = db.Column(db.String, nullable=False)
    student_courses = db.relationship(
        "Course", secondary=students, back_populates="students",
    )
    instructor_courses = db.relationship(
        "Course", secondary=instructors, back_populates="instructors",
    )

    def simple_serialize(self):
        """Return user details without course relationships."""
        return {"id": self.id, "name": self.name, "netid": self.netid}

    def serialize(self):
        """Return all courses the user attends or teaches, without duplicates."""
        courses = {
            course.id: course
            for course in self.student_courses + self.instructor_courses
        }
        return {
            **self.simple_serialize(),
            "courses": [courses[key].simple_serialize() for key in sorted(courses)],
        }


class Assignment(db.Model):
    """An assignment belonging to one course."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    due_date = db.Column(db.Integer, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)
    course = db.relationship("Course", back_populates="assignments")

    def simple_serialize(self):
        """Return assignment details without its course."""
        return {"id": self.id, "title": self.title, "due_date": self.due_date}

    def serialize(self):
        """Return assignment details with the course's basic information."""
        return {**self.simple_serialize(), "course": self.course.simple_serialize()}
