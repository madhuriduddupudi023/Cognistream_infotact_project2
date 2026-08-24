import json
import psycopg2
from kafka import KafkaConsumer

from kafka_config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC
from db_config import DB_CONFIG


def create_consumer():
    return KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        group_id="cognistream-db-consumer",
        auto_offset_reset="earliest",
        value_deserializer=lambda value: json.loads(value.decode("utf-8"))
    )


def connect_database():
    return psycopg2.connect(**DB_CONFIG)


def insert_event(cursor, event):
    query = """
        INSERT INTO developer_activity
        (developer_id, activity, duration_minutes)
        VALUES (%s, %s, %s)
    """

    cursor.execute(
        query,
        (
            event.get("developer_id"),
            event.get("activity"),
            event.get("duration_minutes")
        )
    )


if __name__ == "__main__":
    consumer = create_consumer()
    connection = connect_database()
    cursor = connection.cursor()

    try:
        for message in consumer:
            insert_event(cursor, message.value)
            connection.commit()
            print("Event inserted into PostgreSQL:", message.value)

    except KeyboardInterrupt:
        print("Consumer stopped.")

    finally:
        cursor.close()
        connection.close()
        consumer.close()
