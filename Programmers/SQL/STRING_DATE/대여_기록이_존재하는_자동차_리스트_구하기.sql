SELECT DISTINCT A.CAR_ID
FROM CAR_RENTAL_COMPANY_CAR AS A
    JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS B
    ON A.CAR_ID = B.CAR_ID
WHERE CAR_TYPE = '세단'
    AND START_DATE LIKE '2022-10-%'
ORDER BY A.CAR_ID DESC