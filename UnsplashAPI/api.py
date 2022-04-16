from .collection import UnsplashCollections
from .photos import UnsplashPhotos, UnsplashSearch
from .user import UnsplashUsers
from .topics_stats import UnsplashStats, UnsplashTopics


class UnsplashAPI(UnsplashCollections, UnsplashPhotos,
                  UnsplashUsers, UnsplashSearch, UnsplashTopics, UnsplashStats):
    """
    This class combines all subclasses in one interface.
    """

    def __init__(self, access_key):
        """
        Inofficial Wrapper class for the Unsplash API. 

        All functions are named like the official endpoints, which can be found here: https://unsplash.com/documentation

        To get an access key:
            - Create Developer Account on Unsplash.com
            - Add new Application
            - Adjust "permissions" for your application
            - copy the "access key" in "Keys"

        Args:
            access_key (str):   Access key for application from offifical API.

        Usage:
            api = UnsplashAPI(access_key='<your key>')
            api.get_current_rate_limit()
            >>> '49'
        """
        UnsplashCollections.__init__(self, access_key=access_key)
        UnsplashPhotos.__init__(self, access_key=access_key)
        UnsplashUsers.__init__(self, access_key=access_key)
        UnsplashSearch.__init__(self, access_key=access_key)
        UnsplashTopics.__init__(self, access_key=access_key)
        UnsplashStats.__init__(self, access_key=access_key)
        self.access_key = access_key
