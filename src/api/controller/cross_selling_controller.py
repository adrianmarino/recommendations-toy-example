from flask import jsonify, request

from src.api.context import recommendation_service, app


def query_param(name): return request.args.get(name)


@app.route('/cross-selling/hotels', methods=['GET'])
def get_hotels():
    result = recommendation_service.hotels_by_flight_destination_for_purchaser_user(
        email=query_param('email'),
        time_window=query_param('time-window')
    )
    return jsonify({'hotels': result})


@app.route('/cross-selling/airlines', methods=['GET'])
def get_airlines():
    result = recommendation_service.airlines_by_hotel_city_for_purchaser_user(
        email=query_param('email'),
        time_window=query_param('time-window')
    )
    return jsonify({'airlines': result})
