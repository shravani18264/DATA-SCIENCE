import pandas as pd
import matplotlib.pyplot as plt
import os

# FILE PATH (CHANGE IF NEEDED)
file_path = r"C:\Users\Admin\Desktop\INTERNSHIP\shravani\TASK-1\population.csv"

# Check file exists
if not os.path.exists(file_path):
    print("❌ File not found!")
    print("👉 Check file name and location")
    exit()

# Load dataset
df = pd.read_csv(file_path)

# Show columns (IMPORTANT)
print("Columns in dataset:", df.columns)

# ─────────────────────────────
# SAFE COLUMN HANDLING
# ─────────────────────────────
# Change column names if needed
age_col = "Age"
gender_col = "Gender"

if age_col not in df.columns or gender_col not in df.columns:
    print("❌ Column names not found!")
    print("👉 Update column names from above list")
    exit()

# ─────────────────────────────
# PLOT
# ─────────────────────────────
plt.figure(figsize=(10, 4))

# Histogram
plt.subplot(1, 2, 1)
plt.hist(df[age_col], bins=10)
plt.title("Age Distribution")

# Bar Chart
plt.subplot(1, 2, 2)
df[gender_col].value_counts().plot(kind="bar")
plt.title("Gender Distribution")

plt.tight_layout()
plt.show()
