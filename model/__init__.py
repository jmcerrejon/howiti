from . import database, models

models.Base.metadata.create_all(bind=database.engine)
