import os

from db import Assignment, Course, User, db
from flask import Flask, jsonify, request

app = Flask(__name__)
db_filename = "cms.db"

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "sqlite:///%s" % db_filename
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = False

db.init_app(app)
with app.app_context():
    db.create_all()


def error_response(message, status=400):
    """Return a consistent JSON error and HTTP status."""
    return jsonify({"error": message}), status


def request_body():
    """Read JSON, including requests sent without a JSON content type."""
    body = request.get_json(force=True, silent=True)
    return body if isinstance(body, dict) else {}


def has_text(body, *fields):
    """Check that all required text fields contain nonblank strings."""
    return all(
        isinstance(body.get(field), str) and body[field].strip()
        for field in fields
    )


@app.route("/api/courses/", methods=["GET"])
def get_courses():
    """Return all courses and their immediate relationships."""
    courses = Course.query.order_by(Course.id).all()
    return jsonify({"courses": [course.serialize() for course in courses]})


@app.route("/api/courses/", methods=["POST"])
def create_course():
    """Create a course from its required code and name."""
    body = request_body()
    if not has_text(body, "code", "name"):
        return error_response("Code and name are required")
    course = Course(code=body["code"], name=body["name"])
    db.session.add(course)
    db.session.commit()
    return jsonify(course.serialize()), 201


@app.route("/api/courses/<int:course_id>/", methods=["GET"])
def get_course(course_id):
    """Return a course, or report that it does not exist."""
    course = db.session.get(Course, course_id)
    if course is None:
        return error_response("Course not found", 404)
    return jsonify(course.serialize())


@app.route("/api/courses/<int:course_id>/", methods=["DELETE"])
def delete_course(course_id):
    """Delete a course and its assignments, returning its former contents."""
    course = db.session.get(Course, course_id)
    if course is None:
        return error_response("Course not found", 404)
    result = course.serialize()
    db.session.delete(course)
    db.session.commit()
    return jsonify(result)


@app.route("/api/users/", methods=["POST"])
def create_user():
    """Create a user with a name and NetID."""
    body = request_body()
    if not has_text(body, "name", "netid"):
        return error_response("Name and netid are required")
    user = User(name=body["name"], netid=body["netid"])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize()), 201


@app.route("/api/users/<int:user_id>/", methods=["GET"])
def get_user(user_id):
    """Return a user with all courses they attend or teach."""
    user = db.session.get(User, user_id)
    if user is None:
        return error_response("User not found", 404)
    return jsonify(user.serialize())


@app.route("/api/courses/<int:course_id>/add/", methods=["POST"])
def add_user(course_id):
    """Add a user to a course as a student or instructor."""
    course = db.session.get(Course, course_id)
    if course is None:
        return error_response("Course not found", 404)
    body = request_body()
    user_id = body.get("user_id")
    if type(user_id) is not int:
        return error_response("An integer user_id is required")
    role = body.get("type")
    if role not in ("student", "instructor"):
        return error_response("Type must be student or instructor")
    user = db.session.get(User, user_id)
    if user is None:
        return error_response("User not found", 404)
    members = course.students if role == "student" else course.instructors
    if user not in members:
        members.append(user)
    db.session.commit()
    return jsonify(course.serialize())


@app.route("/api/courses/<int:course_id>/assignment/", methods=["POST"])
def create_assignment(course_id):
    """Create an assignment with a title and Unix timestamp due date."""
    course = db.session.get(Course, course_id)
    if course is None:
        return error_response("Course not found", 404)
    body = request_body()
    if not has_text(body, "title") or type(body.get("due_date")) is not int:
        return error_response("Title and an integer due_date are required")
    assignment = Assignment(
        title=body["title"], due_date=body["due_date"], course=course
    )
    db.session.add(assignment)
    db.session.commit()
    return jsonify(assignment.serialize()), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
