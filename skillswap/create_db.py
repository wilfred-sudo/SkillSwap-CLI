from database import engine, Base
from models import user, skill, user_skill

Base.metadata.create_all(engine)
# This script creates the database tables based on the models defined in the skillswap application.