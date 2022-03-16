import xlrd
import xlsxwriter

wb_pri = xlrd.open_workbook('dlp.xlsx')  # 打开原始文件
wb_tar = xlrd.open_workbook('gs.xlsx')  # 打开目标文件
sheet = wb_pri.sheet_by_name("Sheet1")  # 通过名称获取表格
li = []
row_length = len(sheet.col_values(0)) - 1
col_length = len(sheet.row_values(0)) - 1
row = 1
col = 1
while row <= row_length:
    info_dict = {}
    while col <= col_length:
        info_dict[sheet.cell(0, col).value] = sheet.cell(row, col).value  # 将第一行的内容作为键，分别获取每行对应的值
        col += 1
    col = 1
    row += 1
    li.append(info_dict)
print(li)

sheet = wb_tar.sheet_by_name("字段信息")  # 通过名称获取表格
li = []
row_length = len(sheet.col_values(0)) - 1
col_length = len(sheet.row_values(0)) - 1
row = 1
col = 0
while row <= row_length:
    info_dict = {}
    while col <= col_length:
        info_dict[sheet.cell(0, col).value] = sheet.cell(row, col).value  # 将第一行的内容作为键，分别获取每行对应的值
        col += 1
    col = 1
    row += 1
    li.append(info_dict)
print(li)
