import json
import uuid
from typing import Any, Dict, Optional

import pika

from src.client_service.core.message_brokers import IMessageBroker
from src.client_service.infrastructure.utils import callback_queue, channel, connection, responses


class RabbitmqBroker(IMessageBroker):
    @staticmethod
    async def predict(text: str, model_name: str) -> Optional[bool]:
        correlation_id = str(uuid.uuid4())
        responses[correlation_id] = None
        channel.basic_publish(
            exchange="",
            routing_key="prediction_queue",
            properties=pika.BasicProperties(reply_to=callback_queue, correlation_id=correlation_id),
            body=json.dumps({"text": text, "model_name": model_name}),
        )
        while responses[correlation_id] is None:
            connection.process_data_events()

        try:
            response: Dict[str, Any] = json.loads(responses[correlation_id])
            label: bool = response["label"]
            return label
        except Exception:
            return None
