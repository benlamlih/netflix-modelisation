from Video import Video


class TVShow:
    def __init__(self, name: str, description: str, episodes: list[list[Video]]):
        self.name = name
        self.description = description
        # The 'episodes' variable is a 2D list where each sub-list represents a season of a TV show.
        self.episodes = episodes
