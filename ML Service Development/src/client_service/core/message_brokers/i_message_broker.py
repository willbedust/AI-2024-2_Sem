from abc import ABC, abstractmethod
from typing import Optional


class IMessageBroker(ABC):
    @staticmethod
    @abstractmethod
    async def predict(text: str, model_name: str) -> Optional[bool]:
        """Predicts if text is spam or not"""
