# %% [markdown]
# # Data Cleaning dan Transformation
# **Memuat dataset dan melakukan analisis awal**

# %% [code]
import pandas as pd

# Membaca dataset
data = pd.read_csv("students.csv")

# Menampilkan 10 baris pertama
print("📌 Data Awal:")
display(data.head(10))

# Menampilkan informasi dataset
print("\n📌 Informasi Dataset Sebelum Cleaning:")
data.info()

# %% [code]
# Mengecek nilai yang hilang (missing values)
print("\n📌 Missing Values Sebelum Handling:")
print(data.isna().sum())

# %% [code]
# Handling missing values untuk fitur 'lunch' dengan modus
if 'lunch' in data.columns:
    data['lunch'].fillna(data['lunch'].mode()[0], inplace=True)

# Handling missing values untuk fitur 'reading score' dengan mean
if 'reading score' in data.columns:
    data['reading score'].fillna(data['reading score'].mean(), inplace=True)

# Handling missing values untuk fitur 'grade' dengan median
if 'grade' in data.columns:
    data['grade'].fillna(data['grade'].median(), inplace=True)

# Menampilkan informasi dataset setelah handling missing values
print("\n📌 Informasi Dataset Setelah Handling Missing Values:")
data.info()

# %% [code]
# Alternatif metode untuk menangani missing values

# Pastikan kolom ada sebelum melakukan transformasi
if 'nama_fitur' in data.columns:
    # Interpolasi linear
    data['nama_fitur'].interpolate(method='linear', inplace=True)

    # Backward fill
    data['nama_fitur'].fillna(method='bfill', inplace=True)

    # Forward fill
    data['nama_fitur'].fillna(method='ffill', inplace=True)

    # Drop baris dengan missing value
    data.dropna(subset=['nama_fitur'], inplace=True)

# Drop kolom jika lebih dari 50% data hilang
threshold = int(len(data) * 0.5)
data.dropna(thresh=threshold, axis=1, inplace=True)

# %% [code]
# Menampilkan kembali informasi dataset setelah semua transformasi
print("\n📌 Informasi Dataset Setelah Transformasi:")
data.info()

# %%
