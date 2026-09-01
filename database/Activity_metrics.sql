-- Developer activity metrics

-- Total activity duration
SELECT
    SUM(duration_minutes) AS total_activity_minutes
FROM developer_activity;


-- Average activity duration
SELECT
    AVG(duration_minutes) AS average_activity_minutes
FROM developer_activity;


-- Activity distribution
SELECT
    activity,
    COUNT(*) AS event_count,
    SUM(duration_minutes) AS total_minutes
FROM developer_activity
GROUP BY activity
ORDER BY total_minutes DESC;


-- Developer productivity summary
SELECT
    developer_id,
    COUNT(*) AS activity_events,
    SUM(duration_minutes) AS total_minutes,
    AVG(duration_minutes) AS average_session_minutes
FROM developer_activity
GROUP BY developer_id
ORDER BY total_minutes DESC;
