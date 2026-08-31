-- Developer activity analytics

-- Total activity events
SELECT COUNT(*) AS total_events
FROM developer_activity;


-- Activity count by type
SELECT
    activity,
    COUNT(*) AS activity_count
FROM developer_activity
GROUP BY activity
ORDER BY activity_count DESC;


-- Average duration by activity
SELECT
    activity,
    AVG(duration_minutes) AS average_duration
FROM developer_activity
GROUP BY activity
ORDER BY average_duration DESC;


-- Developer activity summary
SELECT
    developer_id,
    COUNT(*) AS total_events,
    SUM(duration_minutes) AS total_duration,
    AVG(duration_minutes) AS average_duration
FROM developer_activity
GROUP BY developer_id
ORDER BY total_duration DESC;
