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


display_definition_x = 3840
display_difinition_y = 2160
