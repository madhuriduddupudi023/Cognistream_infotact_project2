from kafka_producer import create_producer, publish_event


def test_event_publishing():
    producer = create_producer()

    test_event = {
        "developer_id": "DEV001",
        "activity": "coding",
        "duration_minutes": 30
    }

    publish_event(producer, test_event)
    producer.close()

    print("Kafka event publishing test completed successfully.")


if __name__ == "__main__":
    test_event_publishing()
