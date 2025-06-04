# SkillSwap-CLI

SkillSwap-CLI is a simple command-line interface application to manage users, skills, and learning sessions.  
Users can create profiles, add skills they can teach, request sessions to learn skills from others, and log their progress.

---

## Features

- Create and list users  
- Add skills associated with users  
- Request learning sessions between users  
- Log progress notes for sessions  

---

## Requirements

- Python 3  
- [SQLAlchemy](https://www.sqlalchemy.org/)  
- [tabulate](https://pypi.org/project/tabulate/)  

---

## Setup

### 1. Clone the repository

```bash
git clone <>
cd SkillSwap-CLI

2. Create and activate a virtual environment

python3 -m venv venv
source venv/bin/activate       # Linux/macOS
# or
venv\Scripts\activate.bat      # Windows CMD
# or
.\venv\Scripts\Activate.ps1    # Windows PowerShell

3. Install dependencies

You can install dependencies normally:

pip install -r requirements.txt

Or use pipshell for an interactive install experience:

pipshell

Inside the pipshell prompt, run:

pip install -r requirements.txt
exit

Usage

Run the CLI app by executing:

python cli.py

You will see a menu with options to:

    Create User

    Add Skill

    Request Session

    Log Progress

    Exit

Follow the prompts to perform actions.
Project Structure

SkillSwap-CLI/
├── cli.py           
├── models.py         
├── database.py       
├── requirements.txt   
└── README.md         