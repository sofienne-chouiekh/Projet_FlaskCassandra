import uuid
from cassandra.cqlengine import columns
from models.base import Base

__author__ = 'hangvirus'


class City(Base):
    IDCity = columns.UUID(primary_key=True, default=uuid.uuid4)
    CityName = columns.Text()
    Longitude = columns.double()
    latitude = columns.double()
    population = columns.integer()

    def get_data(self):
        return {
            'IDCity': str(self.IDCity),
            'CityName': self.CityName,
            'Longitude': self.Longitude
            'latitude': self.latitude
            'population': self.population
            
        }