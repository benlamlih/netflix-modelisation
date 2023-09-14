class Video:
    def __init__(self, name: str, length: int, description: str):
        self.name = name
        self.length = length
        self.description = description
        # we can add actors and other relevant info
        self.current = 0

    def play(self, current):
        # play from the current position
        pass

    def pause(self):
        # set current to the current :p
        pass

    def mute(self):
        # mute the video
        pass
