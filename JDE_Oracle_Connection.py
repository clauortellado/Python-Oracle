# Simple Oracle Query
import os
os.chdir("C:\Oracle\instantclient_19_3")

import cx_Oracle
cnn = """tptjde/consulta@(DESCRIPTION=(SOURCE_ROUTE=OFF)
  (ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=127.0.0.1)(PORT=1521)))
  (CONNECT_DATA=(SID=tupass)(SRVR=DEDICATED)))"""

oracle = cx_Oracle.connect(cnn)

sql = """select LIITM as NRO_CORTO, RTRIM(IMAITM) as NRO_3RO, RTRIM(IMLITM) as DESCRIPCION, LIPQOH/10000 as EXISTENCIA 
from PRODDTA.F41021 INV inner join PRODDTA.F4101 MAE on INV.LIITM=MAE.IMITM
where LIITM=13630"""
cur = oracle.cursor()
cur.execute(sql)

printHeader = True

for row in cur:
    print(row)
    
cur.close()
oracle.close()