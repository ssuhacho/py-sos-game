class Player:
    """
    The class of the player.
    """
    def __init__(self, name, first):
        self.name = name
        self.starter = first
        self.now = True if self.starter else False
