
CREATE TABLE campus_admission (
    student_id VARCHAR(20),
    application_id VARCHAR(20),
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARCHAR(20),
    age INT,
    city VARCHAR(50),
    category VARCHAR(30),
    percentage_10th NUMERIC(5,2),
    percentage_12th NUMERIC(5,2),
    pcm_percentage NUMERIC(5,2),
    cet_score NUMERIC(6,2),
    cet_percentile NUMERIC(6,2),
    course VARCHAR(100),
    application_date DATE,
    enquiry_source VARCHAR(50),
    application_status VARCHAR(50),
    eligibility_status VARCHAR(50),
    document_status VARCHAR(50),
    verification_date DATE,
    merit_rank INT,
    seat_status VARCHAR(50),
    fee_status VARCHAR(50),
    admission_status VARCHAR(50),
    processing_days INT,
    admission_date DATE
);

select * from campus_admission;


