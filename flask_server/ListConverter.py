from werkzeug.routing import BaseConverter


class ListConverter(BaseConverter):

    def to_python(self, value):
        return value.split('+')

    def to_url(self, values):
        print(values)
        if len(values) is 1:
            return BaseConverter.to_url(self, values[0])
        return '+'.join(BaseConverter.to_url(self, value)
                        for value in values)
