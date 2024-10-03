from libqtile.config import Group


def init_groups(connected_monitors: int, groups_per_monitor: list[str]):
    groups = []
    for index_screen in range(connected_monitors):
        for group_name in groups_per_monitor[index_screen]:
            groups.append(Group(group_name, screen_affinity=index_screen))

    return groups
