from script.sub.zone_extend import *
import json
from data.input.custom_zone_extend_layouts import zones
import shutil
from script.sub.zone_extend import ZoneDirection as Direction


class CustomLayoutsBuilder:
    """
    FancyZonesの画面作成を自動化。
    x,y,width,height
    に加えて、
    margin,calc_dir(計算方向)など追加
    """

    custom_layouts_path = "custom-layouts.json"

    def __init__(self) -> None:
        self.custom_layouts: dict = {}
        self.backup_layouts()
        self.read_custom_layouts()

        pass

    def read_custom_layouts(self):
        with open(self.custom_layouts_path, "rb") as f:
            self.custom_layouts = json.load(f)
        print(self.custom_layouts)

    def backup_layouts(self):
        shutil.copy(self.custom_layouts_path, f"{self.custom_layouts_path}_backup.json")

    # need custom layout

    def set_zones(self):
        width = 2000
        self.custom_layouts["custom-layouts"][0]["info"]["ref-width"] = 2000
        height = 2000
        self.custom_layouts["custom-layouts"][0]["info"]["ref-height"] = 2000
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
        # width -= margin
        # height -= margin

        x = int(display_size_x*zone.x_percent)
        # x += margin
        if zone.direction in [Direction.up_right, Direction.down_right]:
            x = display_size_x-x-width

        y = int(display_size_y*zone.y_percent)
        # y += margin
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
