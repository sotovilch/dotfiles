from libqtile import widget

widget_icon_defaults = {
    "padding": 1,
    "fontsize": 20,
}


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
