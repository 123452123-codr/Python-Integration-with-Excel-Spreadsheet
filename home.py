import imp
from openpyxl.workbook import Workbook
from openpyxl import load_workbook

wb = load_workbook('database.xlsx')
ws = wb.active

ws["A1"].value = 'Hello'

wb.save('database.xlsx')

