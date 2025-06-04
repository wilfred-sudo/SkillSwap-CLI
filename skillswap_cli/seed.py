from database import Session
from models import User, Skill

db = Session()

jane = User(name="Jane", contact="jane@email.com")
mark = User(name="Mark", contact="mark@email.com")
db.add_all([jane, mark])
db.commit()

guitar = Skill(name="Guitar", teacher_id=jane.id)
db.add(guitar)
db.commit()

print("Seed data added!")