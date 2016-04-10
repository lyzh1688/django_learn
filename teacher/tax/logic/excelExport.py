#coding=utf-8
import xlwt
from django.db import connection,transaction
from django.db.models import Q, Model
from tax.logic.taxCalc import TaxCalc

class TaxExcel():
    def __init__(self,date):
        self.date = date

    def genExcel(self):
        try:
            wb =xlwt.Workbook()
            ws = wb.add_sheet(self.date)
            sql = '''
                      select
                      t.id,
                      max(t.name) as name ,
                      max(t.isFullTime) as isFullTime ,
                      sum(c.fee * r.times) as cost
                      from tax_teacher t,tax_class c,tax_record r
                      where t.id = c.teacher_id
                      and c.id = r.clazz_id
                      and r.date = %s
                      group by t.id
                    '''%self.date
            cursor = connection.cursor()
            cursor.execute(sql)

            fetchall = cursor.fetchall()
            teachertaxlist = []
            i = 0
            ws.write(i, 0, u'教师姓名')
            ws.write(i, 1, u'是否全职')
            ws.write(i, 2, u'金额')
            ws.write(i, 3, u'扣税')
            ws.write(i, 4, u'实发金额')
            for obj in fetchall :
                i += 1
                dic = {}
                dic['id'] = obj[0]
                dic['name'] = obj[1]
                dic['isFullTime'] = obj[2]
                dic['cost'] = obj[3]
                dic['tax'] = TaxCalc.taxCalc(dic['isFullTime'],dic['cost'])
                dic['realCost'] = dic['tax'] + dic['cost']
                ws.write(i, 0, dic['name'])
                ws.write(i, 1, dic['isFullTime'])
                ws.write(i, 2, dic['realCost'])
                ws.write(i, 3, dic['tax'])
                ws.write(i, 4, dic['cost'])
            print ws
        except Exception as e:
            print e
        return wb