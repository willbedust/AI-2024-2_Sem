import json
import os
from typing import Any, Dict

import pika

from src.model_service.infrastructure.models.model_provider import ModelProvider
from src.model_service.infrastructure.utils import download_nltk

download_nltk()
model_provider = ModelProvider()


def on_request(ch, method, properties, body):
    data: Dict[str, Any] = json.loads(body)
    print(data)
    print(data.get("text"))
    print(data.get("model_name"))
    result = model_provider.predict(
        data.get("text", ""),
        data.get("model_name", ""),
    )
    print(result)
    ch.basic_publish(
        exchange="",
        routing_key=properties.reply_to,
        properties=pika.BasicProperties(correlation_id=properties.correlation_id),
        body=json.dumps({"label": result}),
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == "__main__":
    message_broker_host_url = os.environ.get("MESSAGE_BROKER_HOST_URL", "")

    connection = pika.BlockingConnection(pika.ConnectionParameters(host=message_broker_host_url))
    channel = connection.channel()
    channel.queue_declare(queue="prediction_queue")

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue="prediction_queue", on_message_callback=on_request)

    channel.start_consuming()
