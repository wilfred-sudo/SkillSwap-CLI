from database import Base, engine
import models

Base.metadata.create_all(engine)
print("Database created!")