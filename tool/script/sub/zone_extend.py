
class ZoneDirection:
    up_left = 0
    up_right = 1
    down_right = 2
    down_left = 3


class ZoneExtend:

    def __init__(
        self,
        x: float = 0,
        y: float = 0,
        width_percent: float = 1,
        height_percent: float = 1,
        margin: int = 0,
        dir: ZoneDirection = ZoneDirection.up_left
    ) -> None:
        self.x = x
        self.y = y
        self.width_percent = width_percent
        self.height_percent = height_percent
        self.margin = margin
        self.direction = dir
