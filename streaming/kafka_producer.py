import json
from kafka import KafkaProducer

from kafka_config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC


def create_producer():
    return KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda value: json.dumps(value).encode("utf-8")
    )


def publish_event(producer, event):
    producer.send(KAFKA_TOPIC, value=event)
    producer.flush()
    print(f"Published event to {KAFKA_TOPIC}: {event}")


if __name__ == "__main__":
    producer = create_producer()

    sample_event = {
        "developer_id": "DEV001",
        "activity": "coding",
        "duration_minutes": 25
    }

    publish_event(producer, sample_event)
    producer.close()
