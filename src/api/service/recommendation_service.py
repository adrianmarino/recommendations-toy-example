from src.repository.database_client import to_object_list


class RecommendationService:

    def __init__(self, client, cfg):
        self.__client = client
        self._cfg = cfg

    def hotels_by_flight_destination_for_purchaser_user(self, email, time_window):
        query = self._cfg['queries.hotels_by_flight_destination_for_purchaser_user'] % (
            email, time_window, time_window)
        return self.__client.query(
            lambda tx: to_object_list(tx.run(query), columns=['id', 'name', 'score', 'city']))

    def airlines_by_hotel_city_for_purchaser_user(self, email, time_window):
        query = self._cfg['queries.airlines_by_hotel_city_for_purchaser_user'] % (
            email, time_window, time_window)
        return self.__client.query(
            lambda tx: to_object_list(tx.run(query), columns=['name', 'score', 'destination']))

    def more_purchased_flights(self, time_window):
        query = self._cfg['queries.more_purchased_flights'] % (time_window)
        return self.__client.query(
            lambda tx: to_object_list(tx.run(query), columns=['airline', 'score', 'destination']))

    def more_purchased_hotels(self, time_window):
        query = self._cfg['queries.more_purchased_hotels'] % (time_window)
        return self.__client.query(
            lambda tx: to_object_list(tx.run(query), columns=['name', 'score', 'destination']))

    def more_searched_flights(self, time_window):
        query = self._cfg['queries.more_searched_flights'] % (time_window)
        return self.__client.query(
            lambda tx: to_object_list(tx.run(query), columns=['score', 'destination']))

    def more_searched_hotels(self, time_window):
        query = self._cfg['queries.more_searched_hotels'] % (time_window)
        return self.__client.query(
            lambda tx: to_object_list(tx.run(query), columns=['score', 'destination']))
