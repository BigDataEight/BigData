import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('bigData\\imu.csv', encoding='CP949')
plt.rcParams['font.family'] = 'Malgun Gothic'

# Feature Selection - 상관관계 이용
sns.heatmap(df.corr(), annot=True)
plt.show()
print(df.corr(method='pearson'))

