--Course-wise Applicant Analysis
SELECT course, 
COUNT(*) as total_applicants
from campus_admission
group by course 
order by total_applicants desc;



--Eligibility Analysis
SELECT
    CASE
        WHEN pcm_percentage >= 75
             AND cet_percentile >= 60
        THEN 'Eligible'
        ELSE 'Not Eligible'
    END AS calculated_eligibility,
    COUNT(*) AS total_students
FROM campus_admission
GROUP BY
    CASE
        WHEN pcm_percentage >= 75
             AND cet_percentile >= 60
        THEN 'Eligible'
        ELSE 'Not Eligible'
    END
ORDER BY total_students DESC;


--Admission Status Analysis

SELECT
    COUNT(*) AS total_applications,

    COUNT(*) FILTER (
        WHERE eligibility_status = 'Eligible'
    ) AS eligible_students,

    COUNT(*) FILTER (
        WHERE document_status = 'Verified'
    ) AS verified_students,

    COUNT(*) FILTER (
        WHERE seat_status = 'Allocated'
    ) AS allocated_seats,

    COUNT(*) FILTER (
        WHERE fee_status = 'Paid'
    ) AS fees_paid,

    COUNT(*) FILTER (
        WHERE admission_status = 'Confirmed'
    ) AS confirmed_admissions

FROM campus_admission;

--Admission Funnel
WITH funnel AS (

    SELECT
        'Applications' AS stage,
        COUNT(*) AS students
    FROM campus_admission

    UNION ALL

    SELECT
        'Eligible',
        COUNT(*)
    FROM campus_admission
    WHERE eligibility_status = 'Eligible'

    UNION ALL

    SELECT
        'Documents Verified',
        COUNT(*)
    FROM campus_admission
    WHERE document_status = 'Verified'

    UNION ALL

    SELECT
        'Seats Allocated',
        COUNT(*)
    FROM campus_admission
    WHERE seat_status = 'Allocated'

    UNION ALL

    SELECT
        'Fees Paid',
        COUNT(*)
    FROM  campus_admission
    WHERE fee_status = 'Paid'


    UNION ALL

    SELECT
        'Admission Confirmed',
        COUNT(*)
    FROM campus_admission
    WHERE admission_status = 'Confirmed'
)

SELECT *
FROM funnel;



--Course Ranking
WITH course_summary AS (

    SELECT
        course,
        COUNT(*) FILTER (
            WHERE admission_status = 'Confirmed'
        ) AS confirmed_admissions
    FROM campus_admission
    GROUP BY course
)

SELECT
    course,
    confirmed_admissions,

    RANK() OVER (
        ORDER BY confirmed_admissions DESC
    ) AS admission_rank

FROM course_summary

ORDER BY admission_rank;




--Monthly Application Trend
SELECT
    DATE_TRUNC(
        'month',
        application_date
    ) AS application_month,

    COUNT(*) AS applications

FROM campus_admission

GROUP BY
    DATE_TRUNC(
        'month',
        application_date
    )

ORDER BY application_month;




SELECT
    course,

    COUNT(*) AS total_applications,

    COUNT(*) FILTER (
        WHERE admission_status = 'Confirmed'
    ) AS confirmed_admissions,

    ROUND(
        100.0 *
        COUNT(*) FILTER (
            WHERE admission_status = 'Confirmed'
        ) / COUNT(*),
        2
    ) AS admission_conversion_rate

FROM campus_admission

GROUP BY course

ORDER BY admission_conversion_rate DESC;


-- Top student by cet
SELECT
    student_id,
    first_name,
    last_name,
    course,
    pcm_percentage,
    cet_percentile,

    RANK() OVER (
        ORDER BY cet_percentile DESC
    ) AS cet_rank

FROM campus_admission

WHERE eligibility_status = 'Eligible'

ORDER BY cet_rank

LIMIT 20;




-- average processing time
SELECT
    course,

    COUNT(*) AS confirmed_admissions,

    ROUND(
        AVG(
            admission_date - application_date
        ),
        2
    ) AS avg_processing_days

FROM campus_admission

WHERE admission_status = 'Confirmed'
  AND application_date IS NOT NULL
  AND admission_date IS NOT NULL

GROUP BY course

ORDER BY avg_processing_days DESC;





