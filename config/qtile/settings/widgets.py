import subprocess
from glob import glob
from typing import Literal

from libqtile import widget

widget_icon_defaults = {
    "padding": 0,
    "fontsize": 20,
}

widget_volume_defaults = {
    "mute_command": "pactl set-sink-mute @DEFAULT_SINK@ toggle",
    "volume_down_command": "pactl set-sink-volume @DEFAULT_SINK@ -5%",
    "volume_up_command": "pactl set-sink-volume @DEFAULT_SINK@ +5%",
    "get_volume_command": "pactl get-sink-volume @DEFAULT_SINK@ | grep 'Volume' | awk -F '/' '{print $2}'",
    "check_mute_command": "pactl list sinks | grep 'Mute' | awk '{print $2}'",
    "check_mute_string": "yes",
    "background": "#000000",
    "foreground": "#ffffff",
}

widget_group_box_defaults = {
    "fmt": "<b>{}</b>",
    "markup": True,
    "foreground": "#ffffff",
    "inactive": "#4c566a",
    "highlight_method": "line",
    "active": "#ffffff",
    "this_current_screen_border": "#ffffff",
    "this_screen_border": "#ffffff",
    "padding": 6,
}


class CapsNumLockIndicator(widget.CapsNumLockIndicator):
    def __init__(self, **config):
        super().__init__(**config)

    def get_indicator(self, lock: Literal["capslock", "numlock"], on: str, off: str):
        """Return on/off indicators for CapsLock or NumLock."""
        try:
            output = self.call_process(
                ["cat"] + glob(f"/sys/class/leds/*{lock}/brightness")
            )
        except subprocess.CalledProcessError as err:
            output = err.output
            return off

        if "1" in output:
            return on
        else:
            return off

    def poll(self):
        """Poll content for the text box."""
        capslockIndicator = self.get_indicator("capslock", " 󰬈 ", "")
        numlockIndicator = self.get_indicator("numlock", " 󰎤 ", "")

        return f"{capslockIndicator}{numlockIndicator}"


def init_primary_widgets(groups: str):
    return [
        widget.TextBox("  ", foreground="#ffffff", **widget_icon_defaults),
        widget.Sep(linewidth=1, padding=10, foreground="#ffffff"),
        widget.GroupBox(
            visible_groups=[i for i in groups], **widget_group_box_defaults
        ),
        widget.Sep(linewidth=1, padding=10, foreground="#ffffff"),
        CapsNumLockIndicator(**widget_icon_defaults),
        widget.Chord(
            name_transform=lambda name: name.upper(),
        ),
        widget.Spacer(),
        widget.TextBox(
            " ", background="#000000", foreground="#4c566a", **widget_icon_defaults
        ),
        widget.TextBox(
            "  ", background="#4c566a", foreground="#ffffff", **widget_icon_defaults
        ),
        widget.Memory(
            format="{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}",
            measure_mem="M",
            background="#4c566a",
            foreground="#ffffff",
        ),
        widget.TextBox(
            " ", background="#4c566a", foreground="#5e81ac", **widget_icon_defaults
        ),
        widget.TextBox(
            " 󰃰 ", background="#5e81ac", foreground="#ffffff", **widget_icon_defaults
        ),
        widget.Clock(
            format="%Y-%m-%d %a %H:%M", background="#5e81ac", foreground="#ffffff"
        ),
        widget.TextBox(
            " ", background="#5e81ac", foreground="#000000", **widget_icon_defaults
        ),
        widget.Volume(
            emoji="True",
            emoji_list=["  ", "  ", "  ", "  "],
            fontsize=14,
            **widget_volume_defaults,
        ),
        widget.Volume(**widget_volume_defaults),
        widget.QuickExit(),
    ]


def init_secondary_widgets(groups: str):
    return [
        widget.TextBox("  ", foreground="#ffffff", **widget_icon_defaults),
        widget.Sep(linewidth=1, padding=10, foreground="#ffffff"),
        widget.GroupBox(
            visible_groups=[i for i in groups],
            **widget_group_box_defaults,
        ),
        widget.Spacer(),
        widget.TextBox(
            " ", background="#000000", foreground="#5e81ac", **widget_icon_defaults
        ),
        widget.TextBox(
            " 󰃰 ", background="#5e81ac", foreground="#ffffff", **widget_icon_defaults
        ),
        widget.Clock(
            format="%Y-%m-%d %a %H:%M", background="#5e81ac", foreground="#ffffff"
        ),
    ]
