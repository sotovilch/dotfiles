from libqtile.layout.xmonad import MonadTall
from libqtile.layout.floating import Floating
from libqtile.config import Match


def init_layouts(border_width: int, border_focus: str, border_normal: str):
    """
    Parameters
    ----------
    border_width: int
        Border width for the windows
    border_focus: str
        Border color for the focused window
    border_normal: str
        Border color for the unfocused windows

    Returns
    -------
    list
        A list of layouts
    """
    return [
        MonadTall(
            border_width=border_width,
            border_focus=border_focus,
            border_normal=border_normal,
        )
    ]


def init_floating_layout():
    return Floating(
        float_rules=[
            # Run the utility of `xprop` to see the wm class and name of an X client.
            *Floating.default_float_rules,
            Match(wm_type="notification"),
            Match(wm_class="notification"),
            Match(wm_class="confirmreset"),  # gitk
            Match(wm_class="makebranch"),  # gitk
            Match(wm_class="maketag"),  # gitk
            Match(wm_class="ssh-askpass"),  # ssh-askpass
            Match(title="branchdialog"),  # gitk
            Match(title="pinentry"),  # GPG key password entry
        ]
    )
