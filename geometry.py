from irc5_2015 import IRC5_2015

def trapezoidal_area_mm2(top_width_mm, bottom_width_mm, height_mm):
    return ((top_width_mm + bottom_width_mm) / 2) * height_mm


def rectangular_area_mm2(width_mm, height_mm):
    return width_mm * height_mm


def post_and_spacer_area_mm2(
    section_area_mm2,
    post_height_mm,
    spacer_height_mm,
    spacing_mm
):
    """
    Average steel area per meter length
    """
    return section_area_mm2 * (post_height_mm + spacer_height_mm) / spacing_mm


def w_beam_area_mm2(thickness_mm, developed_length_mm, number_of_beams):
    return number_of_beams * thickness_mm * developed_length_mm


def metallic_crash_barrier_edge_area(geom):
    kerb_area = trapezoidal_area_mm2(
        geom['kerb_top_width_mm'],
        geom['kerb_bottom_width_mm'],
        geom['kerb_height_mm']
    )

    post_area = post_and_spacer_area_mm2(
        geom['post_section_area_mm2'],
        geom['post_height_mm'],
        geom['spacer_height_mm'],
        geom['post_spacing_mm']
    )

    beam_area = w_beam_area_mm2(
        geom['w_beam_thickness_mm'],
        geom['w_beam_developed_length_mm'],
        geom['number_of_w_beams']
    )

    return {
        'steel_area_mm2': post_area + beam_area,
        'kerb_area_mm2': kerb_area
    }
