import pandas as pd

df = pd.read_csv('python_bigdata\\BigData\\imu.csv', encoding='CP949')

# 결측치 개수 확인
print(df.isnull().sum())