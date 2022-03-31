#2022.03.03.am.05.51

from urllib.request import urlretrieve

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

urlretrieve("https://movie-phinf.pstatic.net/20220214_120/1644825641315cvVKI_JPEG/movie_image.jpg?type=m99_141_2")
