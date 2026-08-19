from kafka.admin import KafkaAdminClient, NewTopic
from kafka_config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC


def create_kafka_topic():
    admin_client = KafkaAdminClient(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        client_id="cognistream-admin"
    )

    topic = NewTopic(
        name=KAFKA_TOPIC,
        num_partitions=1,
        replication_factor=1
    )

    try:
        admin_client.create_topics(new_topics=[topic])
        print(f"Kafka topic '{KAFKA_TOPIC}' created successfully.")
    except Exception as error:
        print(f"Kafka topic may already exist: {error}")
    finally:
        admin_client.close()


if __name__ == "__main__":
    create_kafka_topic()
