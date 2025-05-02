# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess

from libqtile import qtile, hook
from libqtile.utils import guess_terminal

from settings.layout import init_layouts, init_floating_layout
from settings.wayland import init_wayland_input_rules
from settings.groups import init_groups
from settings.screens import init_screens
from settings.keys import init_key_bindings
from settings.mouse import init_mouse_shortcuts
from utils.connected_monitors import get_connected_monitors

GROUPS_PER_MONITOR = ["uiop", "7890", "1234"]

# Modifier key: more info https://docs.qtile.org/en/latest/manual/config/keys.html#modifiers
# To see a list of modifier names and their matching keys, use the xmodmap command in your terminal.
mod = "lock"
terminal = guess_terminal()

connected_monitors = get_connected_monitors(max_monitors=len(GROUPS_PER_MONITOR))

groups = init_groups(connected_monitors, GROUPS_PER_MONITOR)

keys = init_key_bindings(mod, connected_monitors, GROUPS_PER_MONITOR)

layouts = init_layouts(4, "#5e81ac", "#4c566a")

widget_defaults = dict(
    font="FiraCode Nerd Font",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = init_screens(connected_monitors, GROUPS_PER_MONITOR)

mouse = init_mouse_shortcuts(mod)

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = init_floating_layout()
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = init_wayland_input_rules(qtile)

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


@hook.subscribe.startup_once
def autostart():
    if qtile.core.name == "wayland":
        script = os.path.expanduser("~/.config/qtile/autostart-wayland.sh")
    else:
        script = os.path.expanduser("~/.config/qtile/autostart-x11.sh")
    subprocess.run([script])
