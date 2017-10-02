class Movie:
    """ Movie class is used to store movie basic information """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """ Movie constructor has 3 properties: movie title, post image url and trailer youtube url """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

