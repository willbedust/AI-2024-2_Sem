from abc import ABC, abstractmethod


class IModelService(ABC):
    @abstractmethod
    async def predict(self, text: str, model_name: str, current_user_id: int) -> bool:
        """
        Predicts if the message is spam or not judging by it's text
        :param text: text of the message
        :param model_name: name of the model
        :param current_user_id: user identifier in db who called the method
        :return: boolean if the text is spam or not
        """
