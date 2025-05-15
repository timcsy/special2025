import pandas as pd

# 讀取Excel檔案
xlsx = pd.ExcelFile('2025score.xlsx')

# 顯示所有工作表名稱
print("工作表名稱(術科):")
print(xlsx.sheet_names)

# 讀取每個工作表的內容並顯示
for sheet in xlsx.sheet_names:
    print(f"\n{sheet}的資料結構:")
    df = pd.read_excel('2025score.xlsx', sheet_name=sheet)
    print(df.columns.tolist())
    print("資料範例:")
    print(df.head(2))
