from datetime import datetime
import os
from script.models import *
import shutil
from script.models import ZoneDirection as D

import json


class CustomLayoutsBuilder:
    """
    FancyZonesの画面作成を自動化。
    x,y,width,height
    に加えて、
    margin,calc_dir(計算方向)など追加
    """
    fancy_zones_folder = os.environ["fancy_zones_folder"]
    custom_layouts_path = f"{fancy_zones_folder}/custom-layouts.json"

    def __init__(self, layouts_list: list[LayoutExtend]) -> None:
        self.custom_layouts: dict = {}
        self.layout_list = layouts_list

        pass

    def read_custom_layouts(self):
        with open(f"{self.fancy_zones_folder}/custom-layouts.json", "rb") as f:
            self.custom_layouts = json.load(f)
        print(self.custom_layouts)

    def backup_layouts(self):
        os.makedirs("backup", exist_ok=True)
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        shutil.copyfile(self.custom_layouts_path, f"backup/custom-layouts_{now}.json")

    # need custom layout

    def set_layout_list(self):
        for position, layout in enumerate(self.layout_list):
            self.set_layout(layout, position)
        with open(self.custom_layouts_path, "w") as f:
            json.dump(self.custom_layouts, f, indent=2)
        with open("output.json", "w") as f:
            json.dump(self.custom_layouts, f, indent=2)

    def set_layout(self, layout: LayoutExtend, position: int):
        width = layout.display_resolution_x
        height = layout.display_resolution_y
        # width = 1000
        # height = 1000
        self.custom_layouts["custom-layouts"][position]["info"]["ref-width"] = int(width)
        self.custom_layouts["custom-layouts"][position]["info"]["ref-height"] = int(height)
        self.custom_layouts["custom-layouts"][position]["info"]["zones"] = self.generate_zones(
            layout.zone_list, width, height
        )

    def generate_zones(self, zone_list: list[ZoneExtend], ref_width: int, ref_height: int) -> list[dict]:

        output_zone_json = []
        for zone in zone_list:
            output_zone_json.append(
                self.generate_zone_dict(
                    zone,
                    ref_width,
                    ref_height
                )
            )
        return output_zone_json

    def generate_zone_dict(
        self,
        zone: ZoneExtend,
        display_size_x: int,
        display_size_y: int
    ) -> dict:

        # width = int(display_size_x*zone.width_percent)
        # height = int(display_size_y*zone.height_percent)
        width = zone.width
        height = zone.height
        margin = zone.margin
        width -= margin
        height -= margin

        x = zone.x
        if zone.direction in [D.up_right, D.down_right]:
            x = display_size_x-x-width

        y = zone.y
        if zone.direction in [D.down_left, D.down_right]:
            y = display_size_y-y-height

        return {
            "X": int(x),
            "Y": int(y),
            "width": int(width),
            "height": int(height),
        }

    def run(self):
        self.backup_layouts()
        self.read_custom_layouts()
        self.set_layout_list()
