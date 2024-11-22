from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Student, Course, Score
from .models import User, db
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from .models import User, db
from . import login_manager


bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/students', methods=['GET', 'POST'])
def students():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        new_student = Student(name=name, email=email)
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('main.students'))
    students = Student.query.all()
    return render_template('students.html', students=students)

@bp.route('/courses', methods=['GET', 'POST'])
def courses():
    if request.method == 'POST':
        name = request.form['name']
        code = request.form['code']
        new_course = Course(name=name, code=code)
        db.session.add(new_course)
        db.session.commit()
        return redirect(url_for('main.courses'))
    courses = Course.query.all()
    return render_template('courses.html', courses=courses)

@bp.route('/scores', methods=['GET', 'POST'])
def scores():
    if request.method == 'POST':
        student_id = request.form['student_id']
        course_id = request.form['course_id']
        score = request.form['score']
        new_score = Score(student_id=student_id, course_id=course_id, score=score)
        db.session.add(new_score)
        db.session.commit()
        return redirect(url_for('main.scores'))
    scores = Score.query.all()
    return render_template('scores.html', scores=scores)
main = Blueprint('main', __name__)
# Route ví dụ
@main.route('/')
def index():
    return "Trang chủ. Vui lòng <a href='/login'>đăng nhập</a>."

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:  # Nên sử dụng hashed password
            login_user(user)
            return redirect(url_for('main.index'))
        flash('Tên đăng nhập hoặc mật khẩu không đúng.')
    return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))