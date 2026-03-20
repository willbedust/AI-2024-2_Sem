from abc import ABC, abstractmethod


class IModel(ABC):
    @abstractmethod
    def load(self) -> None:
        """
        Deserialize model to memory
        """

    @abstractmethod
    def predict(self, text: list[str]) -> bool:
        """
        Predicts if text is spam or not
        :param text: input text
        :return: label
        """
