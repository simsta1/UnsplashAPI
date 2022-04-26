from .base import UnsplashBase
import requests


class UnsplashTopics(UnsplashBase):
    """
    Wrapper for API Methods Topics
    Doc: https://unsplash.com/documentation#topics
    """

    def __init__(self, access_key: str) -> None:
        """
        Args:
            access_key (str):       Access Key for the API
        """
        super().__init__(access_key)

    def get_topics(self, ids: str, number_of_pages: int = 1, items_per_page: int = 10, order_by: str = 'position') -> iter:
        """
        Get a single page from the list of all topics.
        see: https://unsplash.com/documentation#topics


         Args:
             ids (str):                         Limit to only matching topic ids or slugs. (Optional; Comma separated string) 
             number_of_pages (int, optional):   Number of total pages to retrieve. 
                                                Defaults to 1.
             items_per_page (int, optional):    Number of items per page. 
                                                Defaults to 10.
             order_by (str. optional):          How to sort the topics. (Optional; Valid values: featured, latest, oldest, position
                                                Defaults to position
         Raises:
             Exception: Exception

         Yields:
             Iterator[iter]:                    Iterator with list of all topics. 
        """
        
        endpoint = self.base_url + '/topics'
        for i in range(number_of_pages):
            response = self.session.get(endpoint,
                                        params=dict(client_id=self.access_key,
                                                    ids=ids,
                                                    page=i, 
                                                    per_page=items_per_page))
            if not response.status_code == 200:
                raise Exception(f'Not able to extract content. Code - {response.status_code}')

            yield response.json()

    def get_single_topic(self, ids: str) -> dict:
        """
        Get a single topic.
        see: https://unsplash.com/documentation#get-a-topic

         Args:
             ids (str):     Limit to only matching topic ids or slugs. (Optional; Comma separated string) 
         
         Exception: Exception

         Returns:
             Dict:          Dict with topic contents.
        """
        endpoint = self.base_url + '/topics'
        response = self.session.get(endpoint,
                                    params=dict(client_id=self.access_key,
                                                ids=ids))
        if not response.status_code == 200:
            raise Exception(f'Not able to extract content. Code - {response.status_code}')

        return response.json()

    def get_topic_photos(self, ids: str, number_of_pages: int = 1, items_per_page: int = 10, order_by: str = 'latest', **kwargs) -> iter:
        """
        Retrieve a topic’s photos.
        see: https://unsplash.com/documentation#get-a-topics-photos


         Args:
             ids (str):                         Limit to only matching topic ids or slugs. (Optional; Comma separated string) 
             number_of_pages (int, optional):   Number of total pages to retrieve. 
                                                Defaults to 1.
             items_per_page (int, optional):    Number of items per page. 
                                                Defaults to 10.
             order_by (str. optional):          How to sort the topics. (Optional; Valid values: featured, latest, oldest, position
                                                Defaults to latest
             **kwargs:
                        orientation	Filter by photo orientation. (Optional; Valid values: landscape, portrait, squarish)

         Raises:
             Exception: Exception

         Yields:
             Iterator[iter]:                    Iterator with list of all topics. 
        """
        
        endpoint = self.base_url + '/topics'
        for i in range(number_of_pages):
            response = self.session.get(endpoint,
                                        params=dict(client_id=self.access_key,
                                                    ids=ids,
                                                    page=i, 
                                                    per_page=items_per_page, **kwargs))
            if not response.status_code == 200:
                raise Exception(f'Not able to extract content. Code - {response.status_code}')

            yield response.json()
   

class UnsplashStats(UnsplashBase):
    """
    Wrapper for API endpoint stats. Docs: https://unsplash.com/documentation#stats
    """

    def __init__(self, access_key: str) -> None:
        """_summary_

        Args:
            access_key (str): _description_
        """
        super().__init__(access_key)

    def get_stats_total(self) -> dict:
        """
        Get a list of counts for all of Unsplash.
        see here: https://unsplash.com/documentation#totals

        Raises:
            Exception: _description_

        Returns:
            dict:   Dictionary with total stats.
        """
        endpoint = self.base_url + '/stats/total'
        response = self.session.get(endpoint,
                                    params=dict(client_id=self.access_key))
        if not response.status_code == 200:
            raise Exception(f'Not able to extract content. Code - {response.status_code}')

        return response.json()


    def get_stats_month(self) -> dict:
        """
        Get the overall Unsplash stats for the past 30 days.
        see here: https://unsplash.com/documentation#month

        Raises:
            Exception: Exception

        Returns:
            dict:   Dictionary with monthly stats. 
        """
        endpoint = self.base_url + '/stats/month'
        response = self.session.get(endpoint,
                                    params=dict(client_id=self.access_key))
        if not response.status_code == 200:
            raise Exception(f'Not able to extract content. Code - {response.status_code}')

        return response.json()