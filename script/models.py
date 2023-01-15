

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
        width: float = 0,
        height: float = 0,
        margin: int = 0,
        dir: ZoneDirection = ZoneDirection.up_left
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.margin = margin
        self.direction = dir


class LayoutExtend:
    zone_list: list[ZoneExtend] = []
    display_resolution_x: int = 1600
    display_resolution_y: int = 900
