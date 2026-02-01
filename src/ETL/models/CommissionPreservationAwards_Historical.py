from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base


# Base = declarative_base()

class HistoricCommissionPreservationAwards:

    api_endpoint = ("https://services2.arcgis.com/HdTo6HJqh92wn4D8/arcgis/rest/services/Historical_Commission_Preservation_Awards_Table_view/FeatureServer/0/query")

    TABLE_NAME = "COMMISSION_PRESERVATION_AWARDS_HISTORIC"

    # __ai_params__ = {
    #     "outFields": "*",
    #     "where": "1=1",
    #     "f": "geojson",
    # }

#     OBJECTID = Column(Integer, primary_key=True)
#     Year = Column(Integer)
#     Category = Column(String)
#     Building_Name = Column(String)
#     Street_Address = Column(String)
#     City = Column(String)
#     State = Column(String)
#     Additional_Informtaion = Column(String)
#     ZipCode = Column(String)
#     Created_Date = Column(TIMESTAMP)

# print(HistoricCommissionPreservationAwards)