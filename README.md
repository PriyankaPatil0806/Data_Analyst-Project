# Data_Analyst_Project

# Task 1: Data Cleaning and Preprocessing

**Dataset**: Medical Appointment No Shows (Kaggle)

### Cleaning Steps Performed:
- Removed rows with missing values
- Removed duplicate records
- Standardized column names to lowercase with underscores
- Converted `scheduledday` and `appointmentday` to proper datetime format
- Cleaned `no_show` column by standardizing to lowercase
- Ensured `age` column has correct integer type

### Tools Used:
- Python (Pandas)

### Output:
- `Medical_Appointment_No_Shows_Cleaned.csv`: Cleaned dataset ready for analysis.
