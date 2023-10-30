
from datetime import datetime
from src.config import logger, stat_prmtrs
from src.storage import DataFromDB

sys_id = 1
today = datetime.today().strftime('%Y-%m-%d')
db_credentials = stat_prmtrs["db_credentials"]
db_con = DataFromDB(**db_credentials)

db_con = DataFromDB(**db_credentials)
today_str = datetime.today().strftime('%Y-%m-%d')
sql_query_1 = "SELECT * FROM StatisticsRAW.[search].FastAnswer_RBD WHERE SysID = {} AND (ParentBegDate <= {} AND ParentEndDate IS NULL OR ParentBegDate <= {} AND  ParentEndDate >= {})".format(sys_id, today_str, today_str, today_str)
sql_query_2 = "SELECT * FROM StatisticsRAW.[search].FastAnswer_RBD where SysID = 15 and Topic LIKE 'косгу робот'"
rows = db_con.get_rows(sql_query_2)
data_dicts = [nt._asdict() for nt in rows]

print(data_dicts[:5])
print(len(data_dicts))