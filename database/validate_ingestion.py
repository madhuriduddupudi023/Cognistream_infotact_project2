import psycopg2

from db_config import DB_CONFIG


def validate_ingestion():
    connection = psycopg2.connect(**DB_CONFIG)
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM developer_activity")
    count = cursor.fetchone()[0]

    print(f"Total developer activity events: {count}")

    cursor.close()
    connection.close()


if __name__ == "__main__":
    validate_ingestion()
