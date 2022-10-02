from openpyxl import Workbook, load_workbook

wb = load_workbook('database.xlsx')
ws = wb.active

ws['A1'].value = "Pi"

wb.save('database.xlsx')
