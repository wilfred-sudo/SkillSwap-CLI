# app.py

from flask import Flask, render_template
from database import Session
from models.user import User
from models.skill import Skill
from models.user_skill import UserSkill

app = Flask(__name__)

@app.route('/')
def home():
    session = Session()
    skills = session.query(Skill).all()
    return render_template('home.html', skills=skills)

@app.route('/skill/<skill_name>')
def show_users_by_skill(skill_name):
    session = Session()
    users = session.query(User).join(UserSkill).join(Skill).filter(
        Skill.name == skill_name,
        UserSkill.is_offering == True
    ).all()
    return render_template('users.html', users=users, skill=skill_name)

if __name__ == '__main__':
    app.run(debug=True)
