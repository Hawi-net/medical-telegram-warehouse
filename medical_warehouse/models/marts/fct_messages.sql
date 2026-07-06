SELECT

    m.message_id,
    c.channel_key,
    d.date_key,

    m.message_text,
    m.message_length,
    m.views,
    m.forwards,
    m.has_image

FROM {{ ref('stg_telegram_messages') }} m

JOIN {{ ref('dim_channels') }} c
ON m.channel = c.channel_name

JOIN {{ ref('dim_dates') }} d
ON CAST(m.message_date AS DATE) = d.date_key