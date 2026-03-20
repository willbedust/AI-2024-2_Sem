from app.models.dummy_recommender import DummyRecommender
from app.models.interfaces import BaseRecommender
from app.models.knn_offline_recommender import KNNOfflineRecommender
from app.models.lightfm_ann_recommender import LightFMANNRecommender


class ModelRegistry:
    def __init__(self):
        self._models: dict[str, BaseRecommender] = {}

    def register(self, name: str, model: BaseRecommender):
        self._models[name] = model

    async def get(self, name: str) -> BaseRecommender | None:
        return self._models.get(name)


model_registry = ModelRegistry()
model_registry.register("dummy", DummyRecommender())
model_registry.register("knn_offline", KNNOfflineRecommender())
model_registry.register("lightfm_ann", LightFMANNRecommender())
