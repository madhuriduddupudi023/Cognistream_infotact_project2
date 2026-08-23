-- Cognistream developer activity table

CREATE TABLE IF NOT EXISTS developer_activity (
    id SERIAL PRIMARY KEY,
    developer_id VARCHAR(50) NOT NULL,
    activity VARCHAR(100) NOT NULL,
    duration_minutes INTEGER,
    event_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
