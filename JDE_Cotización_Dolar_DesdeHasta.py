#Cotizacion Dolar JDE segun Fecha Desde Hasta

import datetime as dt

'''
today = dt.date.today()
first = today.replace(day=1)
lastMonth = first - dt.timedelta(days=1)
print lastMonth.strftime("%Y%m")
'''

fecha1 = dt.datetime(2020, 1, 1, 0, 0).strftime("%Y-%m-%d")
fecha2 = dt.datetime(2020, 1, 31, 0, 0).strftime("%Y-%m-%d")
print(fecha1)
print(fecha2)

import os
os.chdir("C:\Oracle\instantclient_19_3")
import cx_Oracle
cnn = """tptjde/consulta@(DESCRIPTION=(SOURCE_ROUTE=OFF)
                    (ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=127.0.0.1)(PORT=1521)))
                    (CONNECT_DATA=(SID=tupass)(SRVR=DEDICATED)))"""

oracle = cx_Oracle.connect(cnn)
sql = """
(SELECT CXCRCD, CXCRDC, ROUND(AVG(CXCRRD),3) AS DOLAR
         FROM PRODDTA.F0015
         WHERE CXCRDC='USV'and CXAN8=0 and
             (TP_JTD(CXEFT) BETWEEN TO_DATE( '""" + fecha1 + """','YYYY-MM-DD') AND TO_DATE( '""" + fecha2 + """','YYYY-MM-DD'))
         GROUP BY CXCRCD, CXCRDC) """

cur = oracle.cursor()
cur.execute(sql)

printHeader = True

for row in cur:
    print(row)
    
cur.close()
oracle.close()