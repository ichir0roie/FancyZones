from script.sub.zone_extend import ZoneDirection as Direction
from script.sub.zone_extend import ZoneExtend

margin = 0.05

zones = [
    ZoneExtend(0, 0, 0.5-margin, 0.5-margin, Direction.up_left),
    ZoneExtend(0+margin, 0, 0.5-margin, 0.5-margin, Direction.up_left),
    ZoneExtend(0, 0+margin, 0.5-margin, 0.5-margin, Direction.up_left),
    ZoneExtend(0+margin, 0+margin, 0.5-margin, 0.5-margin, Direction.up_left),
]
