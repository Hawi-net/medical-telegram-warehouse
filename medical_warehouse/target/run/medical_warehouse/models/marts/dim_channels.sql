
  
    

  create  table "medical_db"."analytics"."dim_channels__dbt_tmp"
  
  
    as
  
  (
    SELECT
    ROW_NUMBER() OVER (ORDER BY channel) AS channel_key,
    channel AS channel_name,

    CASE
        WHEN LOWER(channel) LIKE '%pharma%' THEN 'Pharmaceutical'
        WHEN LOWER(channel) LIKE '%cosmetic%' THEN 'Cosmetics'
        ELSE 'Medical'
    END AS channel_type,

    MIN(message_date) AS first_post_date,
    MAX(message_date) AS last_post_date,
    COUNT(*) AS total_posts,
    AVG(views) AS avg_views

FROM "medical_db"."analytics"."stg_telegram_messages"

GROUP BY channel
  );
  