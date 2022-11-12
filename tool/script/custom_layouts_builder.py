from script.sub.zone_extend import *
import json
from data.input.custom_zone_extend_layouts import zones
import shutil


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
        width = self.custom_layouts["custom-layouts"][0]["info"]["ref-width"]
        height = self.custom_layouts["custom-layouts"][0]["info"]["ref-height"]
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
        width -= zone.margin
        height -= zone.margin

        x = int(display_size_x*zone.x_percent)
        y = int(display_size_y*zone.y_percent)

        return {
            "X": x,
            "Y": y,
            "width": width,
            "height": height,
        }


if __name__ == "__main__":
    clb = CustomLayoutsBuilder()
    clb.set_zones()
