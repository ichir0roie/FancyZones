from script.zone_extend import ZoneDirection as Direction
from script.zone_extend import ZoneExtend

margin = 70

zones = [
    ZoneExtend(0, 0, 0.5, 0.5, margin, Direction.up_left),
    ZoneExtend(margin, 0, 0.5, 0.5, margin, Direction.up_left),
    ZoneExtend(0, margin, 0.5, 0.5, margin, Direction.up_left),
    ZoneExtend(margin, margin, 0.5, 0.5, margin, Direction.up_left),
    ZoneExtend(0, 0, 0.5, 0.5, margin, Direction.up_right),
    ZoneExtend(margin, 0, 0.5, 0.5, margin, Direction.up_right),
    ZoneExtend(0, margin, 0.5, 0.5, margin, Direction.up_right),
    ZoneExtend(margin, margin, 0.5, 0.5, margin, Direction.up_right),
    ZoneExtend(0, 0, 0.5, 0.5, margin, Direction.down_right),
    ZoneExtend(margin, 0, 0.5, 0.5, margin, Direction.down_right),
    ZoneExtend(0, margin, 0.5, 0.5, margin, Direction.down_right),
    ZoneExtend(margin, margin, 0.5, 0.5, margin, Direction.down_right),
    ZoneExtend(0, 0, 0.5, 0.5, margin, Direction.down_left),
    ZoneExtend(margin, 0, 0.5, 0.5, margin, Direction.down_left),
    ZoneExtend(0, margin, 0.5, 0.5, margin, Direction.down_left),
    ZoneExtend(margin, margin, 0.5, 0.5, margin, Direction.down_left),

    ZoneExtend(0, 0, 0.5, 1, margin, Direction.up_left),
    ZoneExtend(0, margin, 0.5, 1, margin, Direction.up_left),
    ZoneExtend(margin, 0, 0.5, 1, margin, Direction.up_left),
    ZoneExtend(margin, margin, 0.5, 1, margin, Direction.up_left),
    ZoneExtend(0, 0, 0.5, 1, margin, Direction.up_right),
    ZoneExtend(0, margin, 0.5, 1, margin, Direction.up_right),
    ZoneExtend(margin, 0, 0.5, 1, margin, Direction.up_right),
    ZoneExtend(margin, margin, 0.5, 1, margin, Direction.up_right),

    ZoneExtend(margin, 0, 0.8, 1, 0, Direction.up_left),
    ZoneExtend(margin, 0, 0.8, 1, 0, Direction.up_right),

    ZoneExtend(0, 0, 1, 1, 0, Direction.up_left)

]


# this is adjusted by app , so don't need change.
# if you setup for display not 16:9,need change your resolution
display_resolution_x = 3840
display_resolution_y = 2160
