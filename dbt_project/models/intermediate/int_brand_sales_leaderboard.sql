WITH staging AS (
    SELECT * FROM {{ ref('stg_kaggle_car_sales') }}
),

brand_yearly_metrics AS (
    SELECT
        registration_year,
        brand,
        COUNT(*) AS total_registrations,
        ROUND(AVG(asking_price), 2) AS avg_asking_price,
      
        COUNT(CASE WHEN fuel_type = 'EV' THEN 1 END) AS ev_registrations
    FROM staging
    GROUP BY 1, 2
)

SELECT
    registration_year,
    brand,
    total_registrations,
   -- Window function to find the brand's volume share out of all cars sold that year
    ROUND(
        (total_registrations * 100.0) / SUM(total_registrations) OVER (PARTITION BY registration_year), 
        2
    ) AS brand_market_share_percentage,
    avg_asking_price,
    ev_registrations,
    -- Calculate what % of THIS brand's total sales are actually EVs
    ROUND(
        (ev_registrations * 100.0) / NULLIF(total_registrations, 0), 
        2
    ) AS brand_ev_focus_percentage
FROM brand_yearly_metrics
ORDER BY registration_year DESC, total_registrations DESC