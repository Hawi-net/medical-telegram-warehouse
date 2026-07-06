SELECT
    message_id,
    channel,
    CAST(date AS TIMESTAMP) AS message_date,
    text AS message_text,
    views,
    forwards,
    has_media,
    LENGTH(COALESCE(text, '')) AS message_length,
    CASE
        WHEN has_media THEN TRUE
        ELSE FALSE
    END AS has_image
FROM raw.telegram_messages
WHERE text IS NOT NULL;