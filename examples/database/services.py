from typing import Type, Optional

from sqlalchemy.orm import Session

from .models import UserModel
from .core import session
from .utils import add_specified_fields_to_query


class UserDALService:

    def __init__(self, session: Session):
        self.session = session

    def get_all(self, requested_fields: tuple = None) -> list[Optional[Type[UserModel]]]:
        query = self.session.query(UserModel)
        if requested_fields is not None:
            query = add_specified_fields_to_query(query, requested_fields, model=UserModel)
        return query.all()

    def get_by_id(self, id: int, requested_fields: tuple = None) -> Optional[Type[UserModel]]:
        query = self.session.query(UserModel).filter_by(id=id)
        if requested_fields is not None:
            query = add_specified_fields_to_query(query, requested_fields, model=UserModel)
        return query.first()

    def create(self, user: UserModel) -> UserModel:
        self.session.add(user)
        self.session.commit()
        return user

    def update(self, user: UserModel, **data_to_update) -> UserModel:
        for key, value in data_to_update.items():
            setattr(user, key, value)
        self.session.commit()
        return user

    def delete(self, user: UserModel) -> None:
        self.session.delete(user)
        self.session.commit()


user_dal_service = UserDALService(session=session)
