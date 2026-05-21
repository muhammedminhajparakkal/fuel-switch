WITH staging AS (
    SELECT * FROM {{ ref('stg_kaggle_car_sales') }}
),

state_yearly_metrics AS (
    SELECT
        registration_year,
        state,
        COUNT(*) AS total_registrations,
        COUNT(CASE WHEN fuel_type = 'EV' THEN 1 END) AS ev_registrations
    FROM staging
    -- Filter out any missing state data if it exists
    WHERE state IS NOT NULL
    GROUP BY 1, 2
)

SELECT
    registration_year,
    state,
    total_registrations,
    ev_registrations,
    -- Calculate what % of this specific state's total sales are EVs
    ROUND(
        (ev_registrations * 100.0) / NULLIF(total_registrations, 0), 
        2
    ) AS state_ev_penetration_percentage,
    -- Rank the states within each year to see who is leading the race
    RANK() OVER (
        PARTITION BY registration_year 
        ORDER BY (ev_registrations * 100.0) / NULLIF(total_registrations, 0) DESC
    ) AS state_ev_leader_rank
FROM state_yearly_metrics    
ORDER BY registration_year DESC, state_ev_penetration_percentage DESC