WITH base AS (
    SELECT * FROM {{ref('int_fuel_mix_yearly')}}
),

yoy AS (
    SELECT 
        registration_year AS year,
        fuel_type,
        registrations,
        fuel_share_percentage,
        LAG(registrations) OVER(PARTITION BY fuel_type
            ORDER BY registration_year 
            ) AS prev_year_registrations
        FROM base
)

SELECT
    year,
    fuel_type,
    registrations,
    fuel_share_percentage,
    prev_year_registrations,
    ROUND(
        (registrations - prev_year_registrations) * 100.0 / 
    NULLIF(prev_year_registrations, 0),2   
    )AS yoy_growth_percentage
FROM yoy
ORDER BY year , fuel_type

