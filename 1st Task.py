import pandas as pd

df = pd.read_csv("Medical Appointment No Shows.csv")

print("Initial shape:", df.shape)
print(df.info())

print("\nMissing values:\n", df.isnull().sum())

df.dropna(inplace=True)

df.drop_duplicates(inplace=True)

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-', '_')

df['no_show'] = df['no_show'].str.strip().str.lower()

df['scheduledday'] = pd.to_datetime(df['scheduledday'], errors='coerce')
df['appointmentday'] = pd.to_datetime(df['appointmentday'], errors='coerce')

df['age'] = df['age'].astype(int)

print("\nCleaned shape:", df.shape)
print(df.dtypes)

df.to_csv("Medical_Appointment_No_Shows_Cleaned.csv", index=False)
print("\n✅ Cleaned dataset saved as 'Medical_Appointment_No_Shows_Cleaned.csv'")