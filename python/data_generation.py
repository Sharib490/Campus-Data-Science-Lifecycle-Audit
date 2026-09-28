import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# ============================================================
# 1. SETTINGS
# ============================================================

np.random.seed(42)
random.seed(42)

N = 2000

# ============================================================
# 2. BASIC LISTS
# ============================================================

first_names = [
    "Aarav", "Aditya", "Akash", "Aman", "Ananya", "Arjun",
    "Aryan", "Atharva", "Ayush", "Dev", "Dhruv", "Ishaan",
    "Karan", "Krishna", "Manav", "Mohit", "Neha", "Nikhil",
    "Pooja", "Pranav", "Rahul", "Riya", "Rohan", "Sakshi",
    "Shreya", "Sneha", "Tanmay", "Varun", "Vikas", "Yash"
]

last_names = [
    "Sharma", "Patil", "Yadav", "Singh", "Kumar", "Gupta",
    "Jadhav", "Shinde", "Pawar", "More", "Deshmukh", "Joshi",
    "Kulkarni", "Chavan", "Mishra", "Verma", "Mehta", "Naik",
    "Tiwari", "Kadam"
]

cities = [
    "Mumbai", "Thane", "Navi Mumbai", "Kalyan", "Dombivli",
    "Badlapur", "Bhiwandi", "Vasai", "Virar", "Panvel",
    "Mira Road", "Borivali", "Andheri", "Goregaon"
]

genders = ["Male", "Female"]

categories = [
    "Open", "OBC", "SC", "ST", "EWS"
]

courses = [
    "Computer Engineering",
    "Information Technology",
    "Artificial Intelligence & Data Science",
    "Electronics Engineering",
    "Mechanical Engineering"
]

enquiry_sources = [
    "College Website",
    "Google Search",
    "Social Media",
    "Education Portal",
    "College Visit",
    "Friend/Family",
    "Advertisement"
]

# ============================================================
# 3. GENERATE STUDENT DETAILS
# ============================================================

data = []

start_date = datetime(2026, 1, 1)
end_date = datetime(2026, 7, 31)

for i in range(1, N + 1):

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    student_id = f"STU{i:05d}"
    application_id = f"APP{i:05d}"

    gender = random.choice(genders)

    age = int(np.random.choice(
        [17, 18, 19, 20, 21],
        p=[0.05, 0.55, 0.25, 0.10, 0.05]
    ))

    city = random.choice(cities)

    category = np.random.choice(
        categories,
        p=[0.55, 0.20, 0.10, 0.05, 0.10]
    )

    # --------------------------------------------------------
    # Academic performance
    # --------------------------------------------------------

    tenth_percentage = round(
        np.clip(np.random.normal(78, 9), 50, 98), 2
    )

    twelfth_percentage = round(
        np.clip(np.random.normal(76, 10), 45, 97), 2
    )

    # PCM generally close to 12th percentage
    pcm_percentage = round(
        np.clip(
            twelfth_percentage + np.random.normal(0, 4),
            40,
            98
        ),
        2
    )

    # CET percentile related to academic performance
    cet_percentile = round(
        np.clip(
            0.55 * pcm_percentage +
            0.45 * np.random.normal(70, 15),
            25,
            99.99
        ),
        2
    )

    # Convert percentile approximately into CET score
    cet_score = round(
        np.clip(
            cet_percentile * 0.95 +
            np.random.normal(0, 4),
            20,
            100
        ),
        2
    )

    # --------------------------------------------------------
    # Course
    # --------------------------------------------------------

    course = np.random.choice(
        courses,
        p=[0.28, 0.23, 0.22, 0.15, 0.12]
    )

    # --------------------------------------------------------
    # Application date
    # --------------------------------------------------------

    days_difference = (end_date - start_date).days

    application_date = start_date + timedelta(
        days=random.randint(0, days_difference)
    )

    # --------------------------------------------------------
    # Enquiry source
    # --------------------------------------------------------

    enquiry_source = random.choice(enquiry_sources)

    # --------------------------------------------------------
    # Application Status
    # --------------------------------------------------------

    application_status = np.random.choice(
        ["Submitted", "Under Review", "Withdrawn"],
        p=[0.80, 0.15, 0.05]
    )

    # --------------------------------------------------------
    # Eligibility
    #
    # Example project rule:
    # PCM >= 75 AND CET percentile >= 60
    # --------------------------------------------------------

    if pcm_percentage >= 75 and cet_percentile >= 60:
        eligibility_status = "Eligible"
    else:
        eligibility_status = "Not Eligible"

    # --------------------------------------------------------
    # Document verification
    # --------------------------------------------------------

    if application_status == "Withdrawn":
        document_status = "Not Submitted"

    elif eligibility_status == "Not Eligible":
        document_status = np.random.choice(
            ["Verified", "Pending", "Incomplete"],
            p=[0.40, 0.30, 0.30]
        )

    else:
        document_status = np.random.choice(
            ["Verified", "Pending", "Incomplete"],
            p=[0.78, 0.15, 0.07]
        )

    # --------------------------------------------------------
    # Verification date
    # --------------------------------------------------------

    verification_date = None

    if document_status == "Verified":

        verification_date = application_date + timedelta(
            days=random.randint(2, 15)
        )

    # --------------------------------------------------------
    # Merit Rank
    #
    # Better CET percentile = better rank
    # --------------------------------------------------------

    merit_rank = None

    if eligibility_status == "Eligible":

        base_rank = int(
            (100 - cet_percentile) * 70
            + random.randint(1, 500)
        )

        merit_rank = max(1, base_rank)

    # --------------------------------------------------------
    # Seat allocation
    # --------------------------------------------------------

    seat_status = "Not Allocated"

    if (
        eligibility_status == "Eligible"
        and document_status == "Verified"
    ):

        probability = 0.80

        if merit_rank is not None and merit_rank <= 2000:
            probability = 0.90

        if random.random() < probability:
            seat_status = "Allocated"

    # --------------------------------------------------------
    # Fee payment
    # --------------------------------------------------------

    fee_status = "Not Paid"

    if seat_status == "Allocated":

        fee_status = np.random.choice(
            ["Paid", "Pending"],
            p=[0.85, 0.15]
        )

    # --------------------------------------------------------
    # Admission status
    # --------------------------------------------------------

    admission_status = "Not Confirmed"

    if (
        seat_status == "Allocated"
        and fee_status == "Paid"
    ):
        admission_status = "Confirmed"

    # --------------------------------------------------------
    # Admission date
    # --------------------------------------------------------

    admission_date = None

    if admission_status == "Confirmed":

        if verification_date is not None:

            admission_date = verification_date + timedelta(
                days=random.randint(1, 10)
            )

    # --------------------------------------------------------
    # Processing days
    # --------------------------------------------------------

    processing_days = None

    if admission_date is not None:

        processing_days = (
            admission_date - application_date
        ).days

    # --------------------------------------------------------
    # Add record
    # --------------------------------------------------------

    data.append([
        student_id,
        application_id,
        first_name,
        last_name,
        gender,
        age,
        city,
        category,
        tenth_percentage,
        twelfth_percentage,
        pcm_percentage,
        cet_score,
        cet_percentile,
        course,
        application_date,
        enquiry_source,
        application_status,
        eligibility_status,
        document_status,
        verification_date,
        merit_rank,
        seat_status,
        fee_status,
        admission_status,
        admission_date,
        processing_days
    ])


# ============================================================
# 4. CREATE DATAFRAME
# ============================================================

columns = [
    "Student_ID",
    "Application_ID",
    "First_Name",
    "Last_Name",
    "Gender",
    "Age",
    "City",
    "Category",
    "10th_Percentage",
    "12th_Percentage",
    "PCM_Percentage",
    "CET_Score",
    "CET_Percentile",
    "Course",
    "Application_Date",
    "Enquiry_Source",
    "Application_Status",
    "Eligibility_Status",
    "Document_Status",
    "Verification_Date",
    "Merit_Rank",
    "Seat_Status",
    "Fee_Status",
    "Admission_Status",
    "Admission_Date",
    "Processing_Days"
]

df = pd.DataFrame(data, columns=columns)


# ============================================================
# 5. INTRODUCE DATA QUALITY ISSUES
# ============================================================

print("Introducing realistic data-quality issues...")


# ------------------------------------------------------------
# Issue 1: Missing values
# ------------------------------------------------------------

missing_pcm = np.random.choice(
    df.index,
    size=50,
    replace=False
)

df.loc[missing_pcm, "PCM_Percentage"] = np.nan


missing_cet = np.random.choice(
    df.index,
    size=40,
    replace=False
)

df.loc[missing_cet, "CET_Percentile"] = np.nan


missing_city = np.random.choice(
    df.index,
    size=25,
    replace=False
)

df.loc[missing_city, "City"] = np.nan


# ------------------------------------------------------------
# Issue 2: Inconsistent gender values
# ------------------------------------------------------------

gender_problem_rows = np.random.choice(
    df.index,
    size=40,
    replace=False
)

gender_variations = [
    "male",
    "MALE",
    "M",
    "female",
    "FEMALE",
    "F"
]

for idx in gender_problem_rows:
    df.loc[idx, "Gender"] = random.choice(gender_variations)


# ------------------------------------------------------------
# Issue 3: Inconsistent category values
# ------------------------------------------------------------

category_problem_rows = np.random.choice(
    df.index,
    size=35,
    replace=False
)

category_variations = [
    "open",
    "OPEN",
    "OBC ",
    "obc",
    "Sc",
    "sc",
    "St",
    "ews"
]

for idx in category_problem_rows:
    df.loc[idx, "Category"] = random.choice(category_variations)


# ------------------------------------------------------------
# Issue 4: Invalid PCM percentages
# ------------------------------------------------------------

invalid_pcm_rows = np.random.choice(
    df.index,
    size=15,
    replace=False
)

for idx in invalid_pcm_rows:
    df.loc[idx, "PCM_Percentage"] = random.choice(
        [-5, 105, 110, 125]
    )


# ------------------------------------------------------------
# Issue 5: Invalid CET scores
# ------------------------------------------------------------

invalid_cet_rows = np.random.choice(
    df.index,
    size=10,
    replace=False
)

for idx in invalid_cet_rows:
    df.loc[idx, "CET_Score"] = random.choice(
        [-10, -5, 105, 120]
    )


# ------------------------------------------------------------
# Issue 6: Duplicate applications
# ------------------------------------------------------------

duplicate_source_rows = np.random.choice(
    df.index,
    size=20,
    replace=False
)

duplicate_rows = []

for idx in duplicate_source_rows:

    duplicated_record = df.loc[idx].copy()

    # Give duplicate record a different Student ID
    duplicated_record["Student_ID"] = (
        "DUP" + str(random.randint(10000, 99999))
    )

    duplicate_rows.append(duplicated_record)

duplicate_df = pd.DataFrame(duplicate_rows)

df = pd.concat(
    [df, duplicate_df],
    ignore_index=True
)


# ------------------------------------------------------------
# Issue 7: Date-format inconsistencies
# ------------------------------------------------------------

date_problem_rows = np.random.choice(
    df.index,
    size=30,
    replace=False
)

for idx in date_problem_rows:

    if pd.notna(df.loc[idx, "Application_Date"]):

        date_value = pd.to_datetime(
            df.loc[idx, "Application_Date"]
        )

        df.loc[idx, "Application_Date"] = (
            date_value.strftime("%d/%m/%Y")
        )


# ============================================================
# 6. SHUFFLE DATA
# ============================================================

df = df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)


# ============================================================
# 7. SAVE RAW DATASET
# ============================================================

output_file = "campus_admission_raw_2000.csv"

df.to_csv(
    output_file,
    index=False
)


# ============================================================
# 8. DISPLAY INFORMATION
# ============================================================

print("\n==========================================")
print("DATASET CREATED SUCCESSFULLY")
print("==========================================")

print(f"Total records: {len(df)}")
print(f"Total columns: {len(df.columns)}")

print("\nColumns:")
for column in df.columns:
    print("-", column)

print("\nFirst 5 records:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate Application IDs:")
print(
    df["Application_ID"].duplicated().sum()
)

print("\nDataset saved as:")
print(output_file)