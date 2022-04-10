import requests
import time
import os
from tqdm import tqdm


class UnsplashDownload(object):

    def __init__(self, download_folder, n_processes):
        """"""
        self.download_folder = download_folder
        self._init_folder(folder=download_folder)
        self.n_processes = n_processes

    def _init_folder(self, folder):
        """"""
        if not os.path.exists(path=folder):
            os.mkdir(folder)

    def clean_image_folder(self):
        """"""
        for element in os.listdir(self.download_folder):
            if not element.endswith('.jpg'):
                try:
                    rm_path = os.path.join(self.download_folder, element)
                    if os.path.isdir(rm_path):
                        os.rmdir(rm_path)
                    elif os.path.isfile(rm_path):
                        os.remove(rm_path)
                except Exception as e:
                    print(e, f'Could not remove {file}')


class ScrapeUnsplashPhotos(UnsplashDownload):
    _retry_after = 10  # minutes
    base_url = 'https://api.unsplash.com/'
    image_endpoint = 'search/photos'

    def __init__(self, access_key, keywords, download_folder, per_page=30, page_limit=None,
                 extract_image_quality='regular', n_processes=5):
        """"""
        super().__init__(download_folder=download_folder, n_processes=n_processes)
        self.access_key = access_key
        self.keywords = keywords
        self.get_items_per_pages = 30 if per_page > 30 else per_page
        self.page_limit = page_limit
        self.extract_quality = extract_image_quality
        self.images = {}

    def get_photos(self):
        """"""
        for kword in self.keywords:
            # Get first page
            session = requests.Session()
            response = session.get(self.base_url + 'search/photos',
                                   params=dict(query=kword, page=1,
                                               client_id=self.access_key, per_page=30))
            if not self.page_limit:
                pages = self._extract_content(response_json=response.json(), return_pages=True)
            else:
                pages = self.page_limit

            with tqdm(total=pages) as pbar:
                pbar.update(1)
                page = 1
                while page < pages:
                    pbar.set_description(f'Keyword: {kword} / Pagining over page {page}/{pages}')
                    response = session.get(self.base_url + 'search/photos',
                                           params=dict(query=kword, page=page,
                                                       client_id=self.access_key, per_page=30))
                    if response.status_code != 200:
                        self.wait_extract()
                    else:
                        self._extract_content(response_json=response.json(), return_pages=False)
                        pbar.update(1)
                        page += 1
                self.wait_extract()

    def _extract_content(self, response_json, return_pages=True):
        """"""
        for res in response_json['results']:
            self.images[res['id']] = res['urls'][self.extract_quality]

        if return_pages:
            total_pages = response_json['total_pages']

            return total_pages

    def wait_extract(self):
        """"""
        print('--- Downloading Images ---')
        # Download images with multiprocessing
        download_images_MP(images=self.images, n_processes=self.n_processes)

        # Check if images downloaded
        images_in_dir = os.listdir(self.download_folder)
        for name in list(self.images.keys()):
            if name + '.jpg' in images_in_dir:
                del self.images[name]

        # Delete all corrupted files
        self.clean_image_folder()
        print(f'--- Sleeping for {self._retry_after}min ---')
        time.sleep(self._retry_after * 60)

