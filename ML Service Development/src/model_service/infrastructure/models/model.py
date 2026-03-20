import pickle
from pathlib import Path
from typing import Optional

from sklearn.pipeline import Pipeline

from src.model_service.core.models.i_model import IModel


class Model(IModel):
    MODEL_BASE_PATH = Path(__file__).parents[4] / "models"
    EXTENSION = "pkl"

    def __init__(self, name: str):
        self._model_path = self.MODEL_BASE_PATH / f"{name}.{self.EXTENSION}"
        if not self._model_path.is_file():
            raise FileNotFoundError(f"There is no file for model {name} in {self._model_path}")

        self._model: Optional[Pipeline] = None

    def load(self) -> None:
        with open(self._model_path, "rb") as fin:
            self._model = pickle.load(fin)

    def predict(self, text: list[str]) -> bool:
        if self._model is None:
            raise ValueError("Model not loaded before predict.")

        return bool(self._model.predict(text))
