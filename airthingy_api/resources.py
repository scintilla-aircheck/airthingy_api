import flask
import flask_restful as frest


class IModelResource(frest.Resource):
    """
    A base resource interface providing standard helper methods for working with
    the Scintilla API.

    By default, :class:`~IModelResource` will reject all methods with `405
    METHOD NOT ALLOWED`.
    """

    # A data model for this resource
    _MODEL = NotImplemented

    # A dict of schemas for table-level methods
    _SCHEMAS = {
        'POST': NotImplemented,
        'GET': NotImplemented,
        'PUT': NotImplemented,
        'DELETE': NotImplemented
    }

    @property
    def model(self):
        """
        Provides a read-only reference to the data model.
        """
        return self._MODEL

    @property
    def schema(self):
        return self._SCHEMAS[flask.request.method]

    def get_cursor(self):
        """
        Instantiates a new table cursor object.
        """
        return self.model.select()

    def get_params(self):
        """
        Returns validated request parameters based on the method type.
        """
        request = flask.request
        raw_data = request.args if request.method == 'GET' \
            else request.get_json()

        if self.schema:
            clean_data = self.schema.load(raw_data)
            return clean_data.data, clean_data.errors
        else:
            return raw_data, {}

    def post(self):
        flask.abort(405)

    def get(self):
        flask.abort(405)

    def put(self):
        flask.abort(405)

    def delete(self):
        flask.abort(405)
