def init_wayland_input_rules(qtile):
    if qtile.core.name == "wayland":
        from libqtile.backend.wayland.inputs import InputConfig

        return {
            "type:keyboard": InputConfig(kb_layout="es"),
        }

    return None
