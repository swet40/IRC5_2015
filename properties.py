"""
Material properties and load calculations
"""

# IRC standard densities
STEEL_DENSITY = 78   # kN/m3
RCC_DENSITY = 25     # kN/m3


def rcc_load_from_area(area_mm2):
    """
    Converts RCC area (mm²) to load (kN/m)
    """
    return (area_mm2 / 1e6) * RCC_DENSITY


def steel_load_from_area(area_mm2):
    """
    Converts steel area (mm²) to load (kN/m)
    """
    return (area_mm2 / 1e6) * STEEL_DENSITY
