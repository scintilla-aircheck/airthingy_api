from marshmallow import (
    Schema,
    fields,
    validates,
    ValidationError
)

from airthingy_api import validators

from . import models


_TARGETS = [t[0] for t in models.TARGETS]
_UNITS = [u[0] for u in models.UNITS]


class UpdateSensor(Schema):
    slug = fields.String()
    name = fields.String()
    target = fields.String(validate=lambda t: t in _TARGETS)

    @validates('slug')
    def validate_slug(self, data):
        if not validators.validate_slug(data):
            msg = '\'{}\' is an invalid URI slug'
            raise ValidationError(msg.format(data))


class CreateSensor(UpdateSensor):
    name = fields.String(required=True)


class RetrieveSensors(Schema):
    target = fields.String(validate=lambda t: t in _TARGETS)
    offset = fields.Integer(default=0, validate=lambda n: n >= 0)
    limit = fields.Integer(default=100, validate=lambda n: n > 0)


class CreateSensorDataPoint(Schema):
    sensor = fields.String(required=True)
    unit = fields.String(required=True, validate=lambda u: u in _UNITS)
    value = fields.Decimal(required=True)


class CreateSensorData(Schema):
    datetime = fields.DateTime(required=True)
    latitude = fields.Decimal(required=True)
    longitude = fields.Decimal(required=True)
    data = fields.Nested(CreateSensorDataPoint, required=True, many=True,
                         validate=lambda d: len(d) > 0)


class RetrieveSensorData(Schema):
    target = fields.String(validate=lambda t: t in _TARGETS)
    offset = fields.Integer(default=0, validate=lambda n: n >= 0)
    limit = fields.Integer(default=100, validate=lambda n: n > 0)
