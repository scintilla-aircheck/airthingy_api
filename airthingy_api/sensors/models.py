import peewee

from airthingy_api import models, validators, exceptions as exc


TARGETS = (
    ('UNK', '(Unknown)'),
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
    ('UNK', '(Unknown)'),
    ('PPM', 'ppm'),
    ('GM3', 'g/m^3'),
    ('F', 'F\N{DEGREE SIGN}'),
    ('C', 'C\N{DEGREE SIGN}'),
    ('PCT', '%')
)


class Sensor(models.BaseModel):
    """
    A single sensor (e.g. `SPEC_SO2_20PPM`)
    """

    slug = peewee.CharField(unique=True, max_length=32)
    name = peewee.CharField(unique=True, max_length=32)
    target = peewee.CharField(
        choices=TARGETS, default=TARGETS[0][0], max_length=5)

    def clean(self):
        # Convert a standard name string into a URI slug
        if not self.slug:
            slug = self.name.replace('-', '_').replace(' ', '_').upper()
            slug = ''.join([x for x in slug if x.isalnum() or x is '_'])
            self.slug = slug

    def validate(self):
        # Validate slug
        if not validators.validate_slug(self.slug):
            msg = '\'{}\' is not a valid slug'
            raise exc.ValidationError(msg.format(self.slug))

        # Validate target
        if self.target not in [t[0] for t in TARGETS]:
            msg = '\'{}\' is not a valid target'
            raise exc.ValidationError(msg.format(self.target))

    def serialize(self):
        return {
            'slug': self.slug,
            'name': self.name,
            'target': self.target
        }


class SensorDataPoint(models.BaseModel):
    """
    A single sensor data point from a specific device.
    """

    sensor = peewee.ForeignKeyField(Sensor, related_name='data_points')
    datetime = peewee.DateTimeField()
    latitude = peewee.DecimalField(decimal_places=6)
    longitude = peewee.DecimalField(decimal_places=6)
    unit = peewee.CharField(
        choices=UNITS, default=UNITS[0][0], max_length=5)
    value = peewee.DecimalField(decimal_places=6)

    def validate(self):
        # Validate unit
        if self.unit not in [u[0] for u in UNITS]:
            msg = '\'{}\' is not a valid unit'
            raise exc.ValidationError(msg.format(self.unit))

    def serialize(self):
        return {
            'sensor': self.sensor.slug,
            'datetime': self.datetime,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'target': self.sensor.target,
            'unit': self.unit,
            'value': self.value
        }
