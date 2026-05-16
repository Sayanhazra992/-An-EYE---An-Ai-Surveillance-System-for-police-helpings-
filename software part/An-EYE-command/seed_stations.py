from sqlalchemy.orm import sessionmaker

from backend.database.connection import engine
from backend.models.station_model import PoliceStationModel


Session = sessionmaker(bind=engine)

db = Session()

stations = [
    {
        "name": "Pirbahore Police Station",
        "latitude": 25.6211,
        "longitude": 85.1582,
        "city": "Patna",
    },
    {
        "name": "Kadamkuan Police Station",
        "latitude": 25.6095,
        "longitude": 85.1540,
        "city": "Patna",
    },
    {
        "name": "Alamganj Police Station",
        "latitude": 25.6280,
        "longitude": 85.1705,
        "city": "Patna",
    },
]

for station in stations:
    existing_station = (
        db.query(PoliceStationModel)
        .filter(PoliceStationModel.name == station["name"])
        .first()
    )

    if existing_station:
        for key, value in station.items():
            setattr(existing_station, key, value)
    else:
        db.add(PoliceStationModel(**station))

db.commit()
db.close()

print("Stations seeded successfully")
