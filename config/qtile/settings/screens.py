from libqtile import bar
from libqtile.config import Screen

from settings.widgets import init_primary_widgets, init_secondary_widgets


def init_screens(connected_monitors: int, groups_per_monitor: list[str]):
    screens = [
        Screen(
            top=bar.Bar(
                init_primary_widgets(groups=groups_per_monitor[0]),
                24,
                # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
                # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            ),
            # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
            # By default we handle these events delayed to already improve performance, however your system might still be struggling
            # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
            # x11_drag_polling_rate = 60,
        ),
    ]

    if connected_monitors > 1:
        for index_screen in range(1, connected_monitors):
            screens.append(
                Screen(
                    top=bar.Bar(
                        init_secondary_widgets(groups=groups_per_monitor[index_screen]),
                        24,
                    )
                )
            )

    return screens
