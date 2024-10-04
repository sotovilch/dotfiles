import subprocess
from glob import glob
from typing import Literal

from libqtile import widget

widget_icon_defaults = {
    "padding": 1,
    "fontsize": 20,
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
        widget.GroupBox(visible_groups=[i for i in groups]),
        widget.Prompt(),
        widget.WindowName(),
        widget.Chord(
            chords_colors={
                "launch": ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
        ),
        widget.TextBox(
            " ", background="#000000", foreground="#5e81ac", **widget_icon_defaults
        ),
        widget.TextBox(
            " 󰃰 ", background="#5e81ac", foreground="#ffffff", **widget_icon_defaults
        ),
        widget.Clock(
            format="%Y-%m-%d %a %H:%M", background="#5e81ac", foreground="#ffffff"
        ),
        CapsNumLockIndicator(**widget_icon_defaults),
        widget.QuickExit(),
    ]


def init_secondary_widgets(groups: str):
    return [
        widget.GroupBox(visible_groups=[i for i in groups]),
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
