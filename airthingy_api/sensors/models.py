import peewee

from airthingy_api import models


TARGETS = (
    ('CO', 'Carbon Monoxide'),
    ('SO2', 'Sulfur Dioxide'),
    ('NO2', 'Nitrogen Sulfide'),
    ('H2S', 'Hydrogen Sulfide'),
    ('O3', 'Ozone'),
    ('DUST', 'Dust/Aerosol'),
    ('TEMP', 'Temperature'),
    ('HUMID', 'Humidity')
)

UNITS = (
    ('PPM', 'ppm'),
    ('GM3', 'g/m^3'),
    ('F', 'F\N{DEGREE SIGN}'),
    ('C', 'C\N{DEGREE SIGN}'),
    ('PCT', '%')
)


class SensorDataPoint(models.BaseModel):
    datetime = peewee.DateTimeField()
    latitude = peewee.DecimalField(decimal_places=6)
    longitude = peewee.DecimalField(decimal_places=6)
    target = peewee.CharField(choices=TARGETS)
    unit = peewee.CharField(choices=UNITS)
    value = peewee.DecimalField(decimal_places=6)
