WITH brand_share AS (
    SELECT * FROM {{ ref('int_brand_sales_leaderboard') }}
)

SELECT
    brand ,
    registration_year AS year,

    -- 1. ev sale percentage in market compared to all brands
    ev_registrations,
   
    ROUND(
        (ev_registrations * 100.0) / SUM(ev_registrations) OVER (PARTITION BY registration_year), 
        2
    ) AS ev_market_share_pct,

    -- 2. overall business performance
    total_registrations AS total_vehicles_sold,
    brand_market_share_percentage AS overall_market_share_pct,
    brand_ev_focus_percentage AS ev_focus_pct

FROM brand_share
ORDER BY year DESC, ev_registrations DESC