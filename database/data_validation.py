import psycopg2

from db_config import DB_CONFIG


def validate_activity_data():
    connection = psycopg2.connect(**DB_CONFIG)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            COUNT(*) AS total_events,
            COUNT(developer_id) AS valid_developer_ids,
            COUNT(activity) AS valid_activities,
            COUNT(duration_minutes) AS valid_durations
        FROM developer_activity
    """)

    result = cursor.fetchone()

    print("Total events:", result[0])
    print("Valid developer IDs:", result[1])
    print("Valid activities:", result[2])
    print("Valid durations:", result[3])

    cursor.close()
    connection.close()


if __name__ == "__main__":
    validate_activity_data()
