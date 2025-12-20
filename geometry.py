from common import *

# METALLIC CRASH BARRIER – EDGE (FIG. 4)

def metallic_crash_barrier_geometry(crash_barrier_type):
    # Overall geometry
    width_mm = 550
    height_mm = 950 + 100

    # RCC kerb (trapezoid)
    kerb_height = 100
    kerb_top_width = 500
    kerb_bottom_width = 550

    kerb_area_mm2 = (
        (kerb_top_width + kerb_bottom_width) / 2
    ) * kerb_height

    # Steel post + spacer (ISMC 150)
    ISMC_150_AREA_MM2 = 2088
    post_height = 950
    spacer_height = 330
    post_spacing_mm = 1000

    post_area_mm2 = (
        ISMC_150_AREA_MM2 * (post_height + spacer_height)
    ) / post_spacing_mm

    # W-beam
    w_beam_thickness = 3
    w_beam_dev_length = 750

    if crash_barrier_type == KEY_METALLIC_CRASH_BARRIER_TYPE[1]:
        w_beam_area_mm2 = 2 * w_beam_thickness * w_beam_dev_length
        beam_type = "Double W-beam"
    else:
        w_beam_area_mm2 = w_beam_thickness * w_beam_dev_length
        beam_type = "Single W-beam"

    steel_area_mm2 = post_area_mm2 + w_beam_area_mm2

    return {
        'crash_barrier_width': width_mm,
        'crash_barrier_height': height_mm,
        'post_spacing_m': 1.0,
        'steel_area_mm2': steel_area_mm2,
        'kerb_area_mm2': kerb_area_mm2,
        'metallic_barrier_type': beam_type
    }



# MEDIAN WITH METALLIC CRASH BARRIER – FIG. 5(c)

def median_metallic_crash_barrier_geometry():
    median_width_mm = 1200
    median_height_mm = 950 + 100

    # RCC median kerb
    kerb_height = 100
    kerb_top_width = 500
    kerb_bottom_width = 550

    kerb_area_mm2 = (
        (kerb_top_width + kerb_bottom_width) / 2
    ) * kerb_height

    # Steel posts (ISMC 150)
    ISMC_150_AREA_MM2 = 2088
    post_height = 950
    spacer_height = 330
    post_spacing_mm = 1000

    post_area_mm2 = (
        ISMC_150_AREA_MM2 * (post_height + spacer_height)
    ) / post_spacing_mm

    # Single W-beam assumed
    w_beam_area_mm2 = 3 * 750

    steel_area_mm2 = post_area_mm2 + w_beam_area_mm2

    return {
        'median_width': median_width_mm,
        'median_height': median_height_mm,
        'median_steel_area_mm2': steel_area_mm2,
        'median_kerb_area_mm2': kerb_area_mm2
    }

# FIG 5(a): MEDIAN WITH RAISED KERB

def median_raised_kerb_geometry():
    """
    IRC Fig. 5(a) – Median with raised kerb
    """

    median_width_mm = 1200     # minimum as per IRC
    kerb_height_mm = 100
    kerb_top_width_mm = 500
    kerb_bottom_width_mm = 550

    # Trapezoidal kerb area
    kerb_area_mm2 = (
        (kerb_top_width_mm + kerb_bottom_width_mm) / 2
    ) * kerb_height_mm

    return {
        'median_type': 'Raised Kerb',
        'median_width_mm': median_width_mm,
        'median_height_mm': kerb_height_mm,
        'median_kerb_height_mm': kerb_height_mm,
        'median_kerb_top_width_mm': kerb_top_width_mm,
        'median_kerb_bottom_width_mm': kerb_bottom_width_mm,
        'median_kerb_area_mm2': kerb_area_mm2
    }


# FIG 5(b): MEDIAN WITH RCC CRASH BARRIER

def median_rcc_crash_barrier_geometry():
    """
    IRC Fig. 5(b) – Median with RCC crash barrier
    """

    median_width_mm = 1200     # minimum
    barrier_height_mm = 900
    kerb_height_mm = 100

    total_height_mm = barrier_height_mm + kerb_height_mm

    # RCC barrier geometry (same profile as edge RCC barrier)
    barrier_top_width_mm = 175
    barrier_bottom_width_mm = 450

    barrier_area_mm2 = (
        (barrier_top_width_mm + barrier_bottom_width_mm) / 2
    ) * barrier_height_mm

    # RCC kerb (trapezoid)
    kerb_top_width_mm = 500
    kerb_bottom_width_mm = 550

    kerb_area_mm2 = (
        (kerb_top_width_mm + kerb_bottom_width_mm) / 2
    ) * kerb_height_mm

    return {
        'median_type': 'RCC Crash Barrier',
        'median_width_mm': median_width_mm,
        'median_height_mm': total_height_mm,

        'rcc_barrier_height_mm': barrier_height_mm,
        'rcc_barrier_area_mm2': barrier_area_mm2,

        'median_kerb_height_mm': kerb_height_mm,
        'median_kerb_top_width_mm': kerb_top_width_mm,
        'median_kerb_bottom_width_mm': kerb_bottom_width_mm,
        'median_kerb_area_mm2': kerb_area_mm2
    }
