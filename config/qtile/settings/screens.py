from libqtile import bar
from libqtile.config import Screen

from settings.widgets import init_primary_widgets, init_secondary_widgets

default_screen_options = {
    "wallpaper": "wallpaper/nissan-skyline.jpg",
    "wallpaper_mode": "fill",
    "x11_drag_polling_rate": None,
}


def init_screens(connected_monitors: int, groups_per_monitor: list[str]):
    screens = [
        Screen(
            top=bar.Bar(
                init_primary_widgets(groups=groups_per_monitor[0]),
                24,
            ),
            **default_screen_options,
        ),
    ]

    if connected_monitors > 1:
        for index_screen in range(1, connected_monitors):
            screens.append(
                Screen(
                    top=bar.Bar(
                        init_secondary_widgets(groups=groups_per_monitor[index_screen]),
                        24,
                    ),
                    **default_screen_options,
                )
            )

    return screens
