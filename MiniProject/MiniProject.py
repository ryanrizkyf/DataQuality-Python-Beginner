# 1. Case Study: Data Profiling
# Tolong proses dataset terlampir yang  disimpan dalam bentuk csv bernama
# 'https://storage.googleapis.com/dqlab-dataset/uncleaned_raw.csv'.

# Anda bisa memprosesnya dengan cara berikut:
# 1. Import dataset csv ke variable bernama uncleaned_raw.
# 2. Inspeksi dataframe uncleaned_raw.
# 3. Check kolom yang mengandung missing value, jika ada,
# kolom apakah itu dan berapa persen missing value pada kolom tersebut?
# 4. Mengisi missing value tersebut dengan mean dari kolom tersebut!

import matplotlib.pyplot as plt
import pandas as pd

# Baca dataset uncleaned_raw.csv
uncleaned_raw = pd.read_csv(
    'uncleaned_raw.csv')

# inspeksi dataframe uncleaned_raw
print('Lima data teratas:')
print(uncleaned_raw.head())

# Check kolom yang mengandung missing value
print('\nKolom dengan missing value:')
print(uncleaned_raw.isnull().any())

# Persentase missing value
length_qty = len(uncleaned_raw['Quantity'])
count_qty = uncleaned_raw['Quantity'].count()

# mengurangi length dengan count
number_of_missing_values_qty = length_qty - count_qty

# mengubah ke bentuk float
float_of_missing_values_qty = float(number_of_missing_values_qty / length_qty)

# mengubah ke dalam bentuk persen
pct_of_missing_values_qty = '{0:.1f}%'.format(float_of_missing_values_qty*100)

# print hasil percent dari missing value
print('Persentase missing value kolom Quantity:', pct_of_missing_values_qty)

# Mengisi missing value tersebut dengan mean dari kolom tersebut
uncleaned_raw['Quantity'] = uncleaned_raw['Quantity'].fillna(
    uncleaned_raw['Quantity'].mean())

# 2. Case Study: Data Cleansing - Part 1
# Untuk memprosesnya bisa dilakukan dengan cara berikut:
# Mengetahui kolom yang memiliki outliers! Gunakan visualisasi dengan boxplot pada dataframe uncleaned_raw.

# Mengetahui kolom yang memiliki outliers!
uncleaned_raw.boxplot()
plt.show()

# 3. Case Study: Data Cleansing - Part 2
# Langkah selanjutnya bisa dilakukan dengan cara berikut:
# Melakukan proses removing outliers pada kolom UnitPrice.
# Checking duplikasi and melakukan deduplikasi dataset tersebut!

# Check IQR
Q1 = uncleaned_raw['UnitPrice'].quantile(0.25)
Q3 = uncleaned_raw['UnitPrice'].quantile(0.75)
IQR = Q3 - Q1

# removing outliers
uncleaned_raw = uncleaned_raw[~((uncleaned_raw[['UnitPrice']] < (
    Q1 - 1.5 * IQR)) | (uncleaned_raw[['UnitPrice']] > (Q3 + 1.5 * IQR)))]

# check for duplication
print(uncleaned_raw.duplicated(subset=None))

# remove duplication
uncleaned_raw = uncleaned_raw.drop_duplicates()
