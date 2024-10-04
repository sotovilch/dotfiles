from libqtile import qtile
from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy

from utils.lazy_functions import go_to_group, move_to_group


def __init_key_bindings_to_monad_tall(mod_key):
    return [
        # Basics
        Key([mod_key], "q", lazy.window.kill(), desc="Kill focused window"),
        Key(
            [mod_key],
            "f",
            lazy.window.toggle_fullscreen(),
            desc="Toggle fullscreen on the focused window",
        ),
        Key(
            [mod_key],
            "t",
            lazy.window.toggle_floating(),
            desc="Toggle floating on the focused window",
        ),
        # Move focus
        Key([mod_key], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([mod_key], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([mod_key], "j", lazy.layout.down(), desc="Move focus down"),
        Key([mod_key], "k", lazy.layout.up(), desc="Move focus up"),
        # Move windows in MonadTall layout.
        Key(
            [mod_key, "shift"],
            "h",
            lazy.layout.swap_left(),
            desc="Move window to the left",
        ),
        Key(
            [mod_key, "shift"],
            "l",
            lazy.layout.swap_right(),
            desc="Move window to the right",
        ),
        Key(
            [mod_key, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"
        ),
        Key([mod_key, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
        Key([mod_key, "shift"], "f", lazy.layout.flip(), desc="Switch main pane"),
        # Resize window
        KeyChord(
            [mod_key],
            "m",
            [
                Key([mod_key], "n", lazy.layout.normalize(), desc="Reset sizes"),
                Key([mod_key], "g", lazy.layout.grow(), desc="Grow window"),
                Key([mod_key], "s", lazy.layout.shrink(), desc="Shrink window"),
                Key([mod_key], "r", lazy.layout.reset(), desc="Reset window size"),
                Key([mod_key], "m", lazy.layout.maximize(), desc="Maximize window"),
                Key([mod_key], "q", lazy.ungrab_chord()),
            ],
            mode=True,
            name="Window resize",
        ),
    ]


def __init_key_bindings_to_switch_vts_in_wayland():
    keys = []

    # Add key bindings to switch VTs in Wayland.
    # We can't check qtile.core.name in default config as it is loaded before qtile is started
    # We therefore defer the check until the key binding is run by using .when(func=...)
    for vt in range(1, 8):
        keys.append(
            Key(
                ["control", "mod1"],
                f"f{vt}",
                lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
                desc=f"Switch to VT{vt}",
            )
        )

    return keys


def __init_key_bindings_to_groups_in_qtile(
    mod_key, connected_monitors: int, groups_per_monitor: list[str]
):
    keys = []

    for index_screen in range(connected_monitors):
        for group_name in groups_per_monitor[index_screen]:
            keys.extend(
                [
                    # mod + group number = switch to group
                    Key(
                        [mod_key],
                        group_name,
                        go_to_group(group_name, index_screen),
                        desc="Switch to group {}".format(group_name),
                    ),
                    # mod + shift + group number = switch to & move focused window to group
                    Key(
                        [mod_key, "shift"],
                        group_name,
                        move_to_group(group_name, index_screen),
                        desc="Switch to & move focused window to group {}".format(
                            group_name
                        ),
                    ),
                ]
            )

    return keys


def __init_key_bindings_to_apps(mod_key):
    return [
        KeyChord(
            [mod_key],
            "a",
            [
                Key([], "t", lazy.spawn("alacritty")),
                Key([], "f", lazy.spawn("firefox")),
                Key([], "v", lazy.spawn("vlc")),
                KeyChord(
                    [],
                    "q",
                    [
                        Key([], "r", lazy.reload_config(), desc="Reload the config"),
                        Key([], "q", lazy.shutdown(), desc="Shutdown Qtile"),
                    ],
                    name="Qtile opt.",
                ),
            ],
            name="Apps",
        )
    ]


def init_key_bindings(mod_key, connected_monitors: int, groups_per_monitor: list[str]):
    return [
        *__init_key_bindings_to_monad_tall(mod_key),
        *__init_key_bindings_to_switch_vts_in_wayland(),
        *__init_key_bindings_to_groups_in_qtile(
            mod_key, connected_monitors, groups_per_monitor
        ),
        *__init_key_bindings_to_apps(mod_key),
    ]
