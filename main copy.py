from script.custom_layouts_builder import CustomLayoutsBuilder

from script.models import ZoneDirection as D
from script.models import ZoneExtend as Z
from script.models import LayoutExtend

normal = LayoutExtend()
m = 30
w = 1600
h = 900
normal.display_resolution_x = w
normal.display_resolution_y = h

normal.zone_list = [
    Z(0, 0, w/2, h/2, m, D.up_left),
    Z(m, 0, w/2, h/2, m, D.up_left),
    Z(0, m, w/2, h/2, m, D.up_left),
    Z(m, m, w/2, h/2, m, D.up_left),
    Z(0, 0, w/2, h/2, m, D.up_right),
    Z(m, 0, w/2, h/2, m, D.up_right),
    Z(0, m, w/2, h/2, m, D.up_right),
    Z(m, m, w/2, h/2, m, D.up_right),
    Z(0, 0, w/2, h/2, m, D.down_right),
    Z(m, 0, w/2, h/2, m, D.down_right),
    Z(0, m, w/2, h/2, m, D.down_right),
    Z(m, m, w/2, h/2, m, D.down_right),
    Z(0, 0, w/2, h/2, m, D.down_left),
    Z(m, 0, w/2, h/2, m, D.down_left),
    Z(0, m, w/2, h/2, m, D.down_left),
    Z(m, m, w/2, h/2, m, D.down_left),

    Z(0, 0, w/2, h, m, D.up_left),
    Z(0, m, w/2, h, m, D.up_left),
    Z(m, 0, w/2, h, m, D.up_left),
    Z(m, m, w/2, h, m, D.up_left),
    Z(0, 0, w/2, h, m, D.up_right),
    Z(0, m, w/2, h, m, D.up_right),
    Z(m, 0, w/2, h, m, D.up_right),
    Z(m, m, w/2, h, m, D.up_right),

    Z(m, 0, w*0.8, h, 0, D.up_left),
    Z(m, 0, w*0.8, h, 0, D.up_right),

    Z(0, 0, w, h, 0, D.up_left)

]

wide = LayoutExtend()
m = 30
w = 2100
h = 900
wide.display_resolution_x = w
wide.display_resolution_y = h

wide.zone_list = [
    Z(m, 0, w-m*2, h, 0, D.up_left),
    Z(m, 0, w/2-m, h, 0, D.up_left),
    Z(m, 0, w/2-m, h, 0, D.up_right),
    Z(m, 0, w*0.75-m, h, 0, D.up_left),
    Z(m, 0, w*0.75-m, h, 0, D.up_right),

    Z(0, 0, w*0.4, h, m, D.up_right),
    Z(0, m, w*0.4, h, m, D.up_right),
    Z(m, 0, w*0.4, h, m, D.up_right),
    Z(m, m, w*0.4, h, m, D.up_right),

]


layout_list: list[Z] = [
    normal,
    wide,
]


clb = CustomLayoutsBuilder(layout_list)
clb.run()
