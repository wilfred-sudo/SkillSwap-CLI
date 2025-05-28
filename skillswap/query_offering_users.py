from database import Session
from models.user import User
from models.skill import Skill
from models.user_skill import UserSkill

session = Session()

# All users offering Python
results = session.query(User).join(UserSkill).join(Skill).filter(
    Skill.name == "Python",
    UserSkill.is_offering == True
).all()

for user in results:
    print(f"{user.name} offers Python")
