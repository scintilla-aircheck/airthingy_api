from marshmallow import (
    Schema,
    fields
)

from . import models


_TARGETS = [t[0] for t in models.TARGETS]
_UNITS = [u[0] for u in models.UNITS]


class CreateSensorDataPoint(Schema):
    target = fields.String(required=True, validate=lambda t: t in _TARGETS)
    unit = fields.String(required=True, validate=lambda u: u in _UNITS)
    value = fields.Decimal(required=True)


class CreateSensorData(Schema):
    datetime = fields.DateTime(required=True)
    latitude = fields.Decimal(required=True)
    longitude = fields.Decimal(required=True)
    data = fields.Nested(CreateSensorDataPoint, required=True, many=True,
                         validate=lambda d: len(d) > 0)


class GetSensorData(Schema):
    target = fields.String(validate=lambda t: t in _TARGETS)
    offset = fields.Integer(default=0, validate=lambda n: n >= 0)
    limit = fields.Integer(default=100, validate=lambda n: n > 0)
