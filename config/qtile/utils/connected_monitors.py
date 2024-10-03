from libqtile import qtile


def get_connected_monitors(max_monitors: int) -> int:
    connected_monitors: int
    qtile_connected_monitors = len(qtile.core.get_enabled_outputs())

    if qtile_connected_monitors > max_monitors:
        connected_monitors = max_monitors
    else:
        connected_monitors = qtile_connected_monitors

    return connected_monitors
