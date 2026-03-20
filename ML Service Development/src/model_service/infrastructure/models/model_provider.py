import re
from typing import Optional

from nltk import WordNetLemmatizer, word_tokenize
from nltk.corpus import stopwords

from src.model_service.core.models import IModelProvider
from src.model_service.infrastructure.models.model import Model


class ModelProvider(IModelProvider):
    AVAILABLE_MODELS = ["lr", "nb", "gb"]

    def __init__(self):
        self._models_registry = {name: Model(name) for name in self.AVAILABLE_MODELS}

        for model in self._models_registry.values():
            model.load()

        self._stop_words = set(stopwords.words("english"))
        self._lemmatizer = WordNetLemmatizer()

    def predict(self, text: str, model_name: str) -> Optional[bool]:
        try:
            clean_text = self._preprocess_text(text)
            return self._models_registry[model_name].predict([clean_text])
        except Exception:
            return None

    def _preprocess_text(self, text: str) -> str:
        text = text.lower()
        text = re.sub(r"[^a-z\s]", "", text)
        tokens = word_tokenize(text)
        tokens = [self._lemmatizer.lemmatize(token) for token in tokens if token not in self._stop_words]
        return " ".join(tokens)
