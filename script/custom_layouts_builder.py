from datetime import datetime
import os
from script.zone_extend import *
import json
from layouts.sample import *
import shutil
from script.zone_extend import ZoneDirection as Direction


class CustomLayoutsBuilder:
    """
    FancyZonesの画面作成を自動化。
    x,y,width,height
    に加えて、
    margin,calc_dir(計算方向)など追加
    """
    fancy_zones_folder = os.environ["fancy_zones_folder"]
    custom_layouts_path = f"{fancy_zones_folder}/custom-layouts.json"

    def __init__(self) -> None:
        self.custom_layouts: dict = {}
        self.backup_layouts()
        self.read_custom_layouts()

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

    def set_zones(self):
        width = display_resolution_x
        self.custom_layouts["custom-layouts"][0]["info"]["ref-width"] = width
        height = display_resolution_y
        self.custom_layouts["custom-layouts"][0]["info"]["ref-height"] = height
        self.custom_layouts["custom-layouts"][0]["info"]["zones"] = self.generate_zones(width, height)
        with open(self.custom_layouts_path, "w") as f:
            json.dump(self.custom_layouts, f, indent=2)

    def generate_zones(self, ref_width: int, ref_height: int) -> list[dict]:

        zone_list = []
        for zone in zones:
            zone_list.append(
                self.generate_zone_dict(
                    zone,
                    ref_width,
                    ref_height
                )
            )
        return zone_list

    def generate_zone_dict(
        self,
        zone: ZoneExtend,
        display_size_x: int,
        display_size_y: int
    ) -> dict:

        width = int(display_size_x*zone.width_percent)
        height = int(display_size_y*zone.height_percent)
        # margin = int(2000*zone.margin_parcent)
        margin = zone.margin
        width -= margin
        height -= margin

        x = zone.x
        if zone.direction in [Direction.up_right, Direction.down_right]:
            x = display_size_x-x-width

        y = zone.y
        if zone.direction in [Direction.down_left, Direction.down_right]:
            y = display_size_y-y-height

        return {
            "X": x,
            "Y": y,
            "width": width,
            "height": height,
        }


if __name__ == "__main__":
    clb = CustomLayoutsBuilder()
    clb.set_zones()
