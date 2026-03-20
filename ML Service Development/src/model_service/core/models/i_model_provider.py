from abc import ABC, abstractmethod
from typing import Optional


class IModelProvider(ABC):
    @abstractmethod
    def predict(self, text: str, model_name: str) -> Optional[bool]:
        """
        Predicts if text is spam or not
        :param text: input text
        :param model_name: name of the model we want to use
        :return: label
        """
