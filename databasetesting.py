from google.cloud.sql.connector import Connector
import sqlalchemy
import pymysql


# initialize Connector object
connector = Connector()
# function to return the database connection
def getconn() -> pymysql.connections.Connection:
    conn: pymysql.connections.Connection = connector.connect(
        "winged-metric-403908:europe-central2:shoebook",
        "pymysql",
        user="root",
        password="shoebook",
        db="FEETBOOKER"
    )
    return conn

# create connection pool
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)

sizeD = 43
amount_check = sqlalchemy.text(
    "select count(*) from bookers where feet = :feet"
)
limit_check = sqlalchemy.text(
    "select amount from storeroom where bootsize = :bootsize"
)
with pool.connect() as db_conn:
    limited = db_conn.execute(limit_check, parameters={"bootsize": sizeD}).fetchone()
    amounted = db_conn.execute(amount_check, parameters={"feet": sizeD}).fetchone()

print(amounted)
print(limited)
if amounted >= limited:
    print("cant book")
else:
    print("can book")