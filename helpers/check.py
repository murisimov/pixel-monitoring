def is_target(rgb):
    r, g, b = rgb

    if r in range(0, 256):
        if g in range(0, 256):
            if b in range(0, 256):
                return True
