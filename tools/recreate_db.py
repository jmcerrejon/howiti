from model.database import engine
from model.models import Base

Base.metadata.create_all(engine)
