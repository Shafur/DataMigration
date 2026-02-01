import requests 
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas



URL = "https://services2.arcgis.com/HdTo6HJqh92wn4D8/arcgis/rest/services/Police_Chief_Search_Survey_Results_view/FeatureServer/0/query"
params = {
    "where": "1=1",
    "outFields": "*",
    "f": "json"
}

response = requests.get(URL, params=params)
data =response.json()

rows = [f["attributes"] for f in data["features"]]

df = pd.DataFrame(rows)

TABLE_NAME = "POLICE_CHIEF_SEARCH_SURVEY_RESULTS"

with snowflake.connector.connect(connection_name="dev") as conn:

 # with conn.cursor() as cur:print(cur.execute("SELECT 1 FROM TEST_TABLE;").fetchall())

 success, nchunks, nrows, _ = write_pandas(
  conn,
  df,
  table_name=TABLE_NAME,
  auto_create_table=True,
  overwrite=True
 )

 print({"success": success, "rows_loaded": nrows})






print(df)