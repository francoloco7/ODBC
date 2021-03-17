import pyodbc
from config import DSN, UID, PWD
import pandas.io.sql
import pandas as pd

cnxn = pyodbc.connect('DSN=' + DSN + '; UID=' + UID + '; PWD=' + PWD)
#cursor = cnxn.cursor()

query = """
        SELECT fechafac, nrodoc, idcliente 
        FROM mascara 
        WHERE fechafac >= {d '2021-01-01'}
        """

df = pandas.io.sql.read_sql(query, cnxn)
df.head()

#cursor.execute(query)
#rows = cursor.fetchall()

#for row in rows:
#   print("Fecha: ", row.fechafac, " - Nro de comprobante: ", row.nrodoc, " - Código de cliente: ", row.idcliente)

