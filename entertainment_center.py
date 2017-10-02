import media
import fresh_tomatoes

# Jurassic World movie: movie title, post image and movie trailer
jurassic_world = media.Movie("Jurassic World",
                             "http://cdn3-www.comingsoon.net/assets/uploads/2015/02/Pratt-Velociraptor.jpg",
                             "https://www.youtube.com/watch?v=aJJrkyHas78")

# Fast & Furious 7 movie: movie title, post image and movie trailer
fast_and_furious_7 = media.Movie("Fast & Furious 7",
                                 "https://i.ytimg.com/vi/yISKeT6sDOg/maxresdefault.jpg",
                                 "https://www.youtube.com/watch?v=yISKeT6sDOg")

# X-Men: Days of Future Past movie: movie title, post image and movie trailer
x_men = media.Movie("X-Men: Days of Future Past",
                    "https://upload.wikimedia.org/wikipedia/en/0/0c/X-Men_Days_of_Future_Past_poster.jpg",
                    "https://www.youtube.com/watch?v=pK2zYHWDZKo")

# set the movies that will passed to the media file
movies = [jurassic_world, fast_and_furious_7, x_men]

# Open the HTML file in a webbrowser via the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)