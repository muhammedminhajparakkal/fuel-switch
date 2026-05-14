WITH source AS (
    --
    SELECT * FROM {{ source('raw', 'raw_car_sales') }}
),

cleaned AS (
    SELECT
       
        CAST(Year AS INTEGER) as registration_year,
        
     
        TRIM(UPPER(State)) AS state,

        
    
        CASE 
            WHEN LOWER("Fuel Type") LIKE '%electric%' THEN 'EV'
            WHEN LOWER("Fuel Type") LIKE '%hybrid%' THEN 'HYBRID'
            WHEN LOWER("Fuel Type") LIKE '%diesel%' THEN 'DIESEL'
            WHEN LOWER("Fuel Type") LIKE '%petrol%' THEN 'PETROL'
            WHEN LOWER("Fuel Type") LIKE '%cng%' THEN 'CNG'
            WHEN LOWER("Fuel Type") LIKE '%lpg%' THEN 'LPG'
            
            ELSE 'OTHER'
        END AS fuel_type,
        
        -- 
        TRIM(UPPER(Brand)) AS brand,
        "Model Name" as model_name,

         CASE 
            WHEN Owner LIKE '1%' THEN 'FIRST'
            WHEN Owner LIKE '2%' THEN 'SECOND'
            WHEN Owner LIKE '3%' THEN 'THIRD'
            WHEN Owner LIKE '4%' THEN 'FOURTH'
            ELSE 'RE-SALE'
        END AS ownership_status,
        
        CAST(Price AS INTEGER) as asking_price,
        
       
        
    FROM source
    WHERE "Fuel Type" IS NOT NULL 
      AND Year IS NOT NULL 
      AND TRY_CAST(Year AS INT) IS NOT NULL
)

SELECT * FROM cleaned