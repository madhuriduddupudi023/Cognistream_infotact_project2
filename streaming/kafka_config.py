# Kafka configuration for Cognistream

KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"

KAFKA_TOPIC = "developer_activity"

KAFKA_CONSUMER_GROUP = "cognistream-consumer"

PRODUCER_CONFIG = {
    "bootstrap_servers": KAFKA_BOOTSTRAP_SERVERS
}

CONSUMER_CONFIG = {
    "bootstrap_servers": KAFKA_BOOTSTRAP_SERVERS,
    "group_id": KAFKA_CONSUMER_GROUP,
    "auto_offset_reset": "earliest",
    "enable_auto_commit": True
}
