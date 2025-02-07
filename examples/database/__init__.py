from .core import Base, engine
from .models import UserModel

Base.metadata.create_all(engine)
