from Video import Video


class Movie(Video):
    def __init__(self, name: str, length: int, description: str):
        super().__init__(name, length, description)
