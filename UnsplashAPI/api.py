from collection import UnsplashCollections
from photos import UnsplashPhotos, UnsplashSearch
from user import UnsplashUsers
from topics_stats import UnsplashStats, UnsplashTopics


class UnsplashAPI(UnsplashCollections, UnsplashPhotos,
                  UnsplashUsers, UnsplashSearch, UnsplashTopics, UnsplashStats):
    """
    This class combines all subclasses in one interface.
    """

    def __init__(self, access_key):
        """
        Args:
            access_key (_type_): _description_
        """
        UnsplashCollections.__init__(self, access_key=access_key)
        UnsplashPhotos.__init__(self, access_key=access_key)
        UnsplashUsers.__init__(self, access_key=access_key)
        UnsplashSearch.__init__(self, access_key=access_key)
        UnsplashTopics.__init__(self, access_key=access_key)
        UnsplashStats.__init__(self, access_key=access_key)
        self.access_key = access_key
