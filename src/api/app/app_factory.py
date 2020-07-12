from flask import Flask


class ApplicationFactory:

    @staticmethod
    def __prefix_route(route_function, prefix='', mask='{0}{1}'):
        """
          Defines a new route function with a prefix.
          The mask argument is a `format string` formatted with, in that order:
            prefix, route
        """

        def newroute(route, *args, **kwargs):
            """Ne function to prefix the route"""
            return route_function(mask.format(prefix, route), *args, **kwargs)

        return newroute

    @staticmethod
    def create(base_uri):
        app = Flask(__name__)
        app.route = ApplicationFactory.__prefix_route(app.route, base_uri)
        return app
