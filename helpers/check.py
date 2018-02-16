def is_target(target_rgb, current_rgb, deviation):
    t_r, t_g, t_b = target_rgb
    r_lower = t_r - deviation if t_r - deviation > 0 else t_r
    r_upper = t_r + deviation + 1 if t_r + deviation < 256 else t_r + 1
    g_lower = t_g - deviation if t_g - deviation > 0 else t_g
    g_upper = t_g + deviation + 1 if t_g + deviation < 256 else t_g + 1
    b_lower = t_b - deviation if t_b - deviation > 0 else t_b
    b_upper = t_b + deviation + 1 if t_b + deviation < 256 else t_b + 1

    r, g, b = current_rgb

    if r in range(r_lower, r_upper):
        if g in range(g_lower, g_upper):
            if b in range(b_lower, b_upper):
                return True
