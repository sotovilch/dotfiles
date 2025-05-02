from libqtile import qtile
import subprocess

def _x11_connected_monitors() -> int:
    xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"
    command = subprocess.run(
        xrandr,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    
    return int(command.stdout.decode("UTF-8"))


def _wayland_connected_monitors() -> int:
    return len(qtile.core.get_enabled_outputs())

def _backend_connected_monitors() -> int:
    if qtile.core.name == "wayland":
        return _wayland_connected_monitors()
    else:
        return _x11_connected_monitors()

def get_connected_monitors(max_monitors: int) -> int:
    connected_monitors: int
    qtile_connected_monitors: int = _backend_connected_monitors()

    if qtile_connected_monitors > max_monitors:
        connected_monitors = max_monitors
    else:
        connected_monitors = qtile_connected_monitors

    return connected_monitors
