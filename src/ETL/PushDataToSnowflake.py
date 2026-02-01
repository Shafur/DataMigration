import requests
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

######

from models.CommissionPreservationAwards_Historical import HistoricCommissionPreservationAwards
from models.YearbookCollection import YearbookCollection
from models.ServiceRequests2024 import ServiceRequests2024


#########


api_params = {
    "outFields": "*",
    "where": "1=1",
    "f": "geojson",
}



#etl
def api_etl_process(models):
    response = requests.get(models.api_endpoint, params=api_params, timeout=60)
    data = response.json()


    records = [f["properties"] for f in data["features"]]
    df = pd.DataFrame(records)


    with snowflake.connector.connect(connection_name="dev") as conn:
        write_pandas(
            conn,
            df,
            table_name=models.TABLE_NAME,
            auto_create_table=True,
            overwrite=True,
        )


    print(f"Loaded {len(df)} rows into {models.TABLE_NAME}")



api_etl_process(HistoricCommissionPreservationAwards)
api_etl_process(YearbookCollection)
api_etl_process(ServiceRequests2024)


