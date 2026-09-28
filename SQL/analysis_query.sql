Select count(*) as total_student
from campus_admission;

select * from campus_admission
limit 10;

select gender, count(*) as Applicants
from campus_admission
group by gender
Order by Applicants desc;

select category, count(*) as Applicants
from campus_admission
Group by category
Order by Applicants desc;


select city, count(*) as Applicants 
from campus_admission
group by city 
order by Applicants desc;

select course, count(*) as Applicants 
from campus_admission
group by course 
order by Applicants desc;

SELECT
    ROUND(AVG(percentage_10th), 2) AS avg_10th,
    ROUND(AVG(percentage_12th), 2) AS avg_12th,
    ROUND(AVG(pcm_percentage), 2) AS avg_pcm,
    ROUND(AVG(cet_score), 2) AS avg_cet_score,
    ROUND(AVG(cet_percentile), 2) AS avg_cet_percentile
FROM campus_admission;


SELECT
    eligibility_status,
    COUNT(*) AS students
FROM campus_admission
GROUP BY eligibility_status
ORDER BY students DESC;


SELECT
    application_status,
    COUNT(*) AS students
FROM campus_admission
GROUP BY application_status;



SELECT
    COUNT(*) AS total_applicants,

    COUNT(*) FILTER (
        WHERE application_status = 'Confirmed'
    ) AS confirmed_admissions,

    ROUND(
        100.0 *
        COUNT(*) FILTER (
            WHERE application_status = 'Confirmed'
        )
        / COUNT(*),
        2
    ) AS admission_conversion_rate
FROM campus_admission;

--Data Quality Validation
select application_id, 
count(*) as duplicate_count
from campus_admission
group by application_id
having count(*) > 1;


SELECT *
FROM campus_admission
WHERE pcm_percentage < 0
   OR pcm_percentage > 100;


SELECT *
FROM campus_admission
WHERE cet_score < 0
   OR cet_score > 100;

SELECT *
FROM campus_admission
WHERE processing_days < 0;

SELECT *
FROM campus_admission
WHERE processing_days < 0;



