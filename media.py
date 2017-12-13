# Class object stores the movie related information
class Movie():
    # Constructor for initiating the value of variables
    def __init__(self,
                 movie_name,
                 movie_storyline,
                 movie_poster,
                 movie_trailer):
        """
        :param movie_title: string
        :param movie_storyline: string
        :param poster_image: string
        :param trailer_youtube: string
        """
        self.title = movie_name
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
