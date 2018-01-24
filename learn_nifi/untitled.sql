SELECT 
    *
FROM 
    basics AS b
LEFT JOIN 
( 
SELECT 
    p.objective_guid, 
    GROUP_CONCAT(p.product_name separator " && ") AS product_names,
    GROUP_CONCAT(p.policy_code separator " && ") AS policy_codes,
    GROUP_CONCAT(p.pay_mode separator " && ") AS pay_modes,
    GROUP_CONCAT(p.way_name separator " && ") AS way_names,
    GROUP_CONCAT(p.charge_desc separator " && ") AS charge_descs,
    GROUP_CONCAT(p.single_mode separator " && ") AS single_modes,
    GROUP_CONCAT(p.organ_area separator " && ") AS organ_areas
FROM 
    products AS p 
GROUP BY 
    p.objective_guid
) AS gp
ON
    b.market_guid = gp.objective_guid
WHERE 
    b.record_status = "R";