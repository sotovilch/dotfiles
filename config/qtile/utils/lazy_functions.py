from libqtile.core.manager import Qtile
from libqtile.lazy import lazy


@lazy.function
def go_to_group(qtile: Qtile, name_group: str, index_screen: int):
    if qtile.current_screen.index != index_screen:
        qtile.focus_screen(index_screen)

    if qtile.current_group.name != name_group:
        qtile.groups_map[name_group].toscreen()


@lazy.function
def move_to_group(qtile: Qtile, name_group: str, index_screen: int):
    if qtile.current_window is not None:
        qtile.current_window.togroup(name_group)

    if qtile.current_screen.index != index_screen:
        qtile.focus_screen(index_screen)
    else:
        qtile.groups_map[name_group].toscreen()
