from app.models.interfaces import BaseRecommender


class DummyRecommender(BaseRecommender):
    async def predict(self, user_id: int) -> list[int]:
        return list(range(1, 11))
