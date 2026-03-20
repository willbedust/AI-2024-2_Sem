from abc import ABC, abstractmethod


class BaseRecommender(ABC):
    @abstractmethod
    async def predict(self, user_id: int) -> list[int]:
        """
        Возвращает список из 10 идентификаторов фильмов для заданного идентификатора пользователя.

        :param user_id: уникальный идентификатор пользователя
        :return: список идентификаторов фильмов для заданного пользователя
        """
