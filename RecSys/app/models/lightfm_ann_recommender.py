import json
from pathlib import Path

from app.models.interfaces import BaseRecommender


class LightFMANNRecommender(BaseRecommender):
    _DICTIONARY_PATH = Path(__file__).parents[2] / "data/reco_hot_lightfm_ann.json"
    _COLD_RECS = [10440, 15297, 13865, 4151, 2657, 9728, 3734, 4740, 142, 4880]
    # _COLD_RECS = [15297, 13865, 9728, 10440, 4740, 6809, 12192, 8636, 7571, 9583]  # knn

    def __init__(self):
        with open(self._DICTIONARY_PATH, encoding="utf-8") as fin:
            self._cached_recommendations: dict[str, list[int]] = json.load(fin)

    async def predict(self, user_id: int) -> list[int]:
        return self._cached_recommendations.get(str(user_id), self._COLD_RECS)
