import pandas as pd

pd.set_option('display.max_colwidth', None)

данные = pd.read_csv('C:/Users/marki/Desktop/Lab-2/books.csv', delimiter=';', encoding='cp1251', on_bad_lines='skip')

данные['Дата поступления'] = pd.to_datetime(данные['Дата поступления'], errors='coerce', dayfirst=True)


Записи_удовлетворяющие_обоим_условиям = данные[(данные['Название'].str.len() > 30) & (данные['Дата поступления'].dt.year > 2018)]

print(f"Количество записей, удовлетворяющих обоим условиям: {len(Записи_удовлетворяющие_обоим_условиям)}")

print(Записи_удовлетворяющие_обоим_условиям)