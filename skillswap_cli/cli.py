from database import Session
from models import User, Skill, Session as SkillSession
from tabulate import tabulate

db = Session()

def create_user():
    name = input("Enter your name: ")
    contact = input("Enter your contact info: ")
    user = User(name=name, contact=contact)
    db.add(user)
    db.commit()
    print(f"User '{name}' created!")

def list_users():
    users = db.query(User).all()
    table = [(u.id, u.name, u.contact) for u in users]
    print(tabulate(table, headers=["ID", "Name", "Contact"]))

def add_skill():
    list_users()
    user_id = int(input("Enter your user ID: "))
    skill_name = input("Enter skill to teach: ")
    skill = Skill(name=skill_name, user_id=user_id)  # <-- fixed here
    db.add(skill)
    db.commit()
    print(f"Skill '{skill_name}' added!")

def request_session():
    list_users()
    learner_id = int(input("Enter your user ID (as learner): "))
    teacher_id = int(input("Enter teacher's user ID: "))
    skill_id = int(input("Enter skill ID to learn: "))
    session = SkillSession(learner_id=learner_id, teacher_id=teacher_id, skill_id=skill_id)
    db.add(session)
    db.commit()
    print("Session requested!")

def log_progress():
    session_id = int(input("Enter session ID: "))
    notes = input("What did you learn?: ")
    session = db.query(SkillSession).get(session_id)
    if session:
        session.notes = notes
        db.commit()
        print("Progress logged.")
    else:
        print("Session not found.")

def main_menu():
    while True:
        print("\n--- SkillSwap CLI ---")
        print("1. Create User")
        print("2. Add Skill")
        print("3. Request Session")
        print("4. Log Progress")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            create_user()
        elif choice == "2":
            add_skill()
        elif choice == "3":
            request_session()
        elif choice == "4":
            log_progress()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()