import pandas as pd

# 读取Excel文件
df = pd.read_excel(r'F:\firefox\河南.xlsx')

# 筛选包含"许昌市"的行
filtered_df = df[df['工作地点'].str.contains('许昌市')]

# 保存到新的Excel文件
filtered_df.to_excel('xuchang.xlsx', index=False)
