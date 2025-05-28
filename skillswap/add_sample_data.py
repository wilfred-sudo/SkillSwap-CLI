from database import Session
from models.user import User
from models.skill import Skill
from models.user_skill import UserSkill

session = Session()

# Create user and skill
user1 = User(name="Alice", email="alice@example.com")
skill1 = Skill(name="Python", category="Programming")

# Link user to skill (offering)
user_skill1 = UserSkill(user=user1, skill=skill1, is_offering=True, is_seeking=False)

session.add_all([user1, skill1, user_skill1])
session.commit()
