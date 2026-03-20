import json
from pathlib import Path

from app.models.interfaces import BaseRecommender


class KNNOfflineRecommender(BaseRecommender):
    _DICTIONARY_PATH = Path(__file__).parents[2] / "data/reco_hot.json"
    # _COLD_RECS = [10440, 15297, 9728, 13865, 4151, 3734, 2657, 4880, 142, 6809]  # popular
    _COLD_RECS = [15297, 13865, 9728, 10440, 4740, 6809, 12192, 8636, 7571, 9583]  # category

    def __init__(self):
        with open(self._DICTIONARY_PATH, encoding="utf-8") as fin:
            self._cached_recommendations: dict[str, list[int]] = json.load(fin)

    async def predict(self, user_id: int) -> list[int]:
        return self._cached_recommendations.get(str(user_id), self._COLD_RECS)
