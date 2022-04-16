
# Unsplash API

[![.github/workflows/python-package.yml](https://github.com/SimonStaehli/UnsplashAPI/actions/workflows/python-package.yml/badge.svg)](https://github.com/SimonStaehli/UnsplashAPI/actions/workflows/python-package.yml) 
[![PyPI version fury.io](https://badge.fury.io/py/unsplashapi.svg)](https://pypi.python.org/pypi/unsplashapi/)


This is a inofficial Wrapper around the Unsplash API. 

## Installation

Install project via pip

```bash
pip install unsplashapi
```

## Get an Access Key

1. Register for a Developer Account on Unsplash.com
2. Add a new application und `Your Apps`
3. Adapt `Redirect URI & Permissions` according to your preferences
4. Copy `Access Key` from `Keys`

    
## Usage/Examples

```python
# Extracts Rate Limits of your key
from UnsplashAPI import UnsplashAPI

api = UnsplashAPI(access_key='<your key>')
api.get_current_rate_limit()

>>> '49'

```
```python
# Extract contents of an image
from UnsplashAPI import UnsplashAPI

api = UnsplashAPI(access_key='<your key>')
api.get_photo_by_id(photo_id='ieic5Tq8YMk')

>>> {'id': 'ieic5Tq8YMk',
 'created_at': '2018-01-13T16:36:34-05:00',
 'updated_at': '2022-04-15T13:02:41-04:00',
 'promoted_at': '2018-01-14T20:42:18-05:00' ...}

```



## Contributing

Contributions are always welcome!

1. Clone Repository 
2. Make adjustments
3. Add PR



## Appendix

All requests are documented in the official Unsplash-API documentation provided
from the developers: https://unsplash.com/documentation

Package Reference: https://pypi.org/project/unplashapi/0.0.1/

