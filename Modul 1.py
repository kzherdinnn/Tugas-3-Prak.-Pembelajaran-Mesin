import pandas as pd

# Ganti dengan path file CSV yang sudah diunduh
file_path = "DatasetForCoffeeSales2.csv"

# Membaca dataset CSV
df_stunting = pd.read_csv(file_path)

# Menampilkan beberapa baris pertama untuk memastikan data terbaca
print(df_stunting.head())

# Fungsi untuk menentukan jenis data
def detect_data_type(series):
    if series.dtype == 'object':
        return "Nominal"
    elif series.dtype in ['int64', 'float64']:
        unique_values = series.nunique()
        if unique_values < 10:
            return "Ordinal"
        elif series.min() == 0 and series.max() > 0:
            return "Rasio"
        else:
            return "Interval"
    return "Unknown"

# Menampilkan hasil deteksi jenis data
print("\nJenis Data untuk Dataset:")
for col in df_stunting.columns:
    print(f"{col}: {detect_data_type(df_stunting[col])}")
