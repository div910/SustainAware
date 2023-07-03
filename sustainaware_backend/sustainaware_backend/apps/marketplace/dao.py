from django.conf import settings
from sustainaware_backend.utils.mysql_helpers import *
class Dao:

    def __init__(self):
        self.database_config = settings.DATABASES['default']
        self.market_place_table_name = 'product'

    def get_all_products(self):
        try:
            connection_obj = get_connection(self.database_config)
            query_params = {}
            query = f'select id, product_description_raw, product_description_frontend, image_name from {self.market_place_table_name}'
            result = execute_select(connection_obj, query, query_params)
            return result
        except Exception as ex:
            print(f"Exception found in get_all_products : Dao : marketplace, {ex}")

        return []