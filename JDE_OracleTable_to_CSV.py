import os
os.chdir("C:\Oracle\instantclient_19_3")
import cx_Oracle
import os
import csv

cnn = """tptjde/consulta@(DESCRIPTION=(SOURCE_ROUTE=OFF)
                    (ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=127.0.0.1)(PORT=1521)))
                    (CONNECT_DATA=(SID=tupass)(SRVR=DEDICATED)))"""

csv_file = open("IXX_StockInsumos.csv","w") #"K:/Control de Gestion/Compras/IXX_StockInsumos.csv"
writer = csv.writer(csv_file, delimiter=',', lineterminator="\n", quoting=csv.QUOTE_NONNUMERIC)

oracle = cx_Oracle.connect(cnn)

#STOCK INSUMOS IXX a la Fecha
sql = """select LIITM as NRO_CORTO,
trim(IMAITM) as NRO_3RO, 
trim(IMLITM) as DESCRIPCION, 
(LIPQOH/10000) as EXISTENCIA_FISICA, 
(LIPREQ/10000) as EN_ORDEN_COMPRA
from PRODDTA.F41021 INV inner join PRODDTA.F4101 MAE on INV.LIITM=MAE.IMITM
where 
LIITM=13630 or 
LIITM=13607 or 
LIITM=732 or
LIITM=822979 or
LIITM=700554 or
LIITM=16512"""

cursor = oracle.cursor()
cursor.execute(sql)

for row in cursor:
    print(row)
    writer.writerow(row)

cursor.close()
oracle.close()
csv_file.close()