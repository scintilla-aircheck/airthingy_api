from airthingy_api import models

from peewee import (
    DateTimeField,
    CharField,
    DecimalField
)


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
    datetime = DateTimeField()
    latitude = DecimalField(decimal_places=6)
    longitude = DecimalField(decimal_places=6)
    target = CharField(choices=TARGETS)
    unit = CharField(choices=UNITS)
    value = DecimalField(decimal_places=6)
