
class ZoneDirection:
    up_left = 0
    up_right = 1
    down_right = 2
    down_left = 3


class ZoneExtend:

    def __init__(
        self,
        x_percent: float = 0,
        y_percent: float = 0,
        width_percent: float = 1,
        height_percent: float = 1,
        # margin_percent: int = 0,
        dir: ZoneDirection = ZoneDirection.up_left
    ) -> None:
        self.x_percent = x_percent
        self.y_percent = y_percent
        self.width_percent = width_percent
        self.height_percent = height_percent
        # self.margin_parcent = margin_percent
        self.direction = dir
