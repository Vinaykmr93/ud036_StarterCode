import fresh_tomatoes
import media
# Creating instances of movies to describe the Movie Class

Kung_fu_panda = media.Movie("Kung fu Panda",
                """When an obese Po the Panda, a kung fu enthusiast,
                 gets selected as the Dragon Warrior, he decides to
                 team up with the Furious Five and destroy the evil
                 forces that threaten the Valley of Peace""",
                "https://resizing.flixster.com/YJNiubmM7nW455AiYCnBlRQgRIM=/206x305/v1.bTsxMTE3Nzg0MztqOzE3NTg5OzEyMDA7ODAwOzEyMDA",  # Noqa
                "https://www.youtube.com/watch?v=PXi3Mv6KMzY")

Titanic = media.Movie("Titanic",
           "Love Story of a Rich girl and a poor artist",
           "http://t0.gstatic.com/images?q=tbn:ANd9GcQhYjUIu2o5v5u3rfJpCq5Cz0Q9WK--XdYxai_N2d0ImohPiIOp",  # Noqa
           "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

Into_the_wild = media.Movie("Into the Wild",
                """ A young graduate, decides to renounce all his
                    possessions and hitchhike across America""",
                "http://www.gstatic.com/tv/thumb/movieposters/168385/p168385_p_v8_aa.jpg",  # Noqa
                "https://www.youtube.com/watch?v=g7ArZ7VD-QQ")

Saving_private_Ryan = media.Movie("Saving Private Ryan",
                      "Saving Ryan who is the last Survivor of the family",
                      "http://t2.gstatic.com/images?q=tbn:ANd9GcR0lDhR_dXAKTm9wysp3nWu6kP0V5skJBVbCNC_Q8urAWcr4iF_",  # Noqa
                      "https://www.youtube.com/watch?v=zwhP5b4tD6g")

The_Shawshank_Redemption = media.Movie("The Shawshank Redemption",
                           """A successful banker, is arrested for the
                              murders of his wife and her lover, and is
                              sentenced to life imprisonment at the Shawshank
                              prison. He becomes the most unconventional
                              prisoner""",
                           "http://t0.gstatic.com/images?q=tbn:ANd9GcSkmMH-bEDUS2TmK8amBqgIMgrfzN1_mImChPuMrunA1XjNTSKm",  # Noqa
                           "https://www.youtube.com/watch?v=K_tLp7T6U1c")

Enemy_at_the_gates = media.Movie("Enemy at the Gates",
                     "A war story of a German and Russians",
                     "http://www.gstatic.com/tv/thumb/movieposters/26100/p26100_p_v8_aa.jpg",  # Noqa
                     "https://www.youtube.com/watch?v=xqwlIaOyBSA")
# list of movies
movies = [Kung_fu_panda,
          Titanic,
          Into_the_wild,
          Saving_private_Ryan,
          The_Shawshank_Redemption,
          Enemy_at_the_gates]
""" open_movies_page(<movie_list>) takes list of movies and outputs the
movie website. This function is declared in fresh_tomatoes"""
fresh_tomatoes.open_movies_page(movies)
