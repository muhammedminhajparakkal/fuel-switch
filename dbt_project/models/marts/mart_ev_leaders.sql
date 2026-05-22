WITH state_ev AS(
    SELECT * FROM {{ref('int_state_ev_penetration')}}
)
SELECT
    state,
    registration_year AS year,
    state_ev_penetration_percentage AS ev_share_pct,
    state_ev_leader_rank AS ev_rank
FROM state_ev
ORDER BY year DESC, ev_rank ASC