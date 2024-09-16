from openpyxl import load_workbook

wb = load_workbook('Book.xlsx')
for sheet in wb:
    print(sheet.title)
    