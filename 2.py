import pandas as pd

путь_к_файлу = r'C:\Users\marki\Desktop\Lab-2\books-en.csv'

данные_books_en = pd.read_csv(путь_к_файлу, delimiter=';', encoding='ISO-8859-1', on_bad_lines='skip')


данные_books_en['Year-Of-Publication'] = pd.to_numeric(данные_books_en['Year-Of-Publication'], errors='coerce')


autor = input("Ingrese el nombre del autor para buscar libros: ")


отфильтрованные_результаты = данные_books_en[
    (данные_books_en['Book-Author'].str.contains(autor, case=False, na=False)) &
    (данные_books_en['Year-Of-Publication'] >= 2000)
]

print(f"Número de libros de '{autor}' publicados después del año 2000: {len(отфильтрованные_результаты)}")

print(отфильтрованные_результаты)

