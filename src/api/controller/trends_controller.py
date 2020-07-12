from flask import jsonify

from src.api.context import app, recommendation_service
from src.api.controller.cross_selling_controller import query_param


@app.route('/flights/more-purchased', methods=['GET'])
def more_purchased_flights():
    result = recommendation_service.more_purchased_flights(query_param('time-window'))
    return jsonify({'flights': result})


@app.route('/flights/more-searched', methods=['GET'])
def more_searched_flights():
    result = recommendation_service.more_searched_flights(query_param('time-window'))
    return jsonify({'flights': result})


@app.route('/hotels/more-purchased', methods=['GET'])
def more_purchased_hotels():
    result = recommendation_service.more_purchased_hotels(query_param('time-window'))
    return jsonify({'hotels': result})


@app.route('/hotels/more-searched', methods=['GET'])
def more_searched_hotels():
    result = recommendation_service.more_searched_hotels(query_param('time-window'))
    return jsonify({'hotels': result})
