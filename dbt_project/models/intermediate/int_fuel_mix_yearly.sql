WITH staging AS (
    SELECT * FROM {{ ref('stg_kaggle_car_sales') }}
),

yearly_fuel_counts AS (
    SELECT
        registration_year,
        fuel_type,
        COUNT(*) AS registrations,
        ROUND(AVG(asking_price), 2) AS avg_asking_price
    FROM staging
    GROUP BY 1, 2
)

SELECT
    registration_year,
    fuel_type,
    registrations,
    ROUND(
        (registrations * 100.0) / SUM(registrations) OVER (PARTITION BY registration_year), 
        2) AS fuel_share_percentage,
    avg_asking_price
FROM yearly_fuel_counts
ORDER BY registration_year DESC, fuel_share_percentage DESC
