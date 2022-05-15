from flask import Blueprint

example_route = Blueprint('api', __name__)


@example_route.route('/')
def example():
    pass