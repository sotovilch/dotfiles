from libqtile.lazy import lazy
from libqtile.config import Drag, Click


def init_mouse_shortcuts(mod_key):
    # Drag floating layouts.
    return [
        Drag(
            [mod_key],
            "Button1",
            lazy.window.set_position_floating(),
            start=lazy.window.get_position(),
        ),
        Drag(
            [mod_key],
            "Button3",
            lazy.window.set_size_floating(),
            start=lazy.window.get_size(),
        ),
        Click([mod_key], "Button2", lazy.window.bring_to_front()),
    ]
