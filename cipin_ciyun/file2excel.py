# https://www.cnblogs.com/hedeyong/p/7646125.html

import xlwt

myWorkbook = xlwt.Workbook()
mySheet = myWorkbook.add_sheet('A Test Sheet')
mySheet.write(2, 0, 1)  #行，列，值

myWorkbook.save('excelFile.xls')
