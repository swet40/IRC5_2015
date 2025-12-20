"""
Module for IRC 5:2015 bridge design clauses.
@author: Aditya Donde

"""

import math
from common import *
from geometry import (
    metallic_crash_barrier_geometry,
    median_metallic_crash_barrier_geometry
)

from properties import (
    steel_load_from_area,
    rcc_load_from_area
)

from geometry import (
    median_raised_kerb_geometry,
    median_rcc_crash_barrier_geometry
)
from properties import rcc_load_from_area


class IRC5_2015(object):

    @staticmethod
    def cl_101_41_safety_kerb_width(kerb_width, footpath):
        """
        IRC 5:2015 – Clause 101.41
        Safety kerb requirement when footpath is not provided.
        """

        result = {
            "applicable": False,
            "is_compliant": True,
            "required_min_width": KEY_SAFETY_KERB_MIN_WIDTH,
            "provided_width": kerb_width,
            "remarks": ""
        }

        # Clause applies only if footpath is NOT provided
        if footpath != KEY_FOOTPATH[0]:  # "None"
            result["remarks"] = "Clause 101.41 not applicable as footpath is provided."
            return result

        result["applicable"] = True

        if kerb_width < KEY_SAFETY_KERB_MIN_WIDTH:
            result["is_compliant"] = False
            result["remarks"] = (
                "Kerb width is less than minimum 750 mm required "
                "when footpath is not provided."
            )
        else:
            result["remarks"] = (
                "Kerb width satisfies minimum 750 mm requirement "
                "for occasional pedestrian use."
            )

        return result

        
        
    def cl_109_8_1_road_kerb_outline(design_dict):
        """Road kerb dimensions as per IRC 5:2015
        Clause 109.8.1 - Standard dimensions for road kerbs
        """
        road_kerb_dimensions = {
            'clause': "IRC 5:2015 109.8.1",
            'road_kerb_width': 225 * mm,  # width in mm
            'road_kerb_effective_width': 175 * mm,  # effective width in mm, its minimum value
            'road_kerb_height': 225 * mm,  # height in mm
            'road_kerb_effective_height': 200 * mm,  # effective height in mm
            'road_kerb_edge_radius': 25 * mm # edge radius in mm
        }

        updated_design = design_dict.copy()
        updated_design.update(road_kerb_dimensions)
        return updated_design
    
    @staticmethod
    def cl_109_8_3_safety_kerb_outline(design_dict):
        # Clause 109.8.3 - A safety kerb will have the same outline as that of a road kerb, except that the top width shall not be less than 750 mm.
        
        # Get road kerb dimensions
        road_kerb = IRC5_2015.cl_109_8_1_road_kerb_outline({})

        # Create safety kerb dimensions based on road kerb dimensions

        safety_kerb_dimensions = {
            'safety_kerb_width': road_kerb['road_kerb_width'],  # width in mm
            'safety_kerb_effective_width': road_kerb['road_kerb_effective_width'],  # effective width in mm
            'safety_kerb_height': road_kerb['road_kerb_height'],  # height in mm
            'safety_kerb_effective_height': road_kerb['road_kerb_effective_height'],  # effective height in mm
            'safety_kerb_edge_radius': road_kerb['road_kerb_edge_radius'],  # edge radius in mm
            'min_required_top_width': KEY_SAFETY_KERB_MIN_WIDTH,
            "is_width_compliant": road_kerb["road_kerb_width"] >= KEY_SAFETY_KERB_MIN_WIDTH,
        }

        updated_design = design_dict.copy()
        updated_design.update(safety_kerb_dimensions)

        return updated_design

    # Utility function to compute safety kerb area
    def compute_safety_kerb_area(kerb):
        r = kerb["safety_kerb_edge_radius"]
        b = kerb["safety_kerb_effective_width"]
        h = kerb["safety_kerb_height"]
        he = kerb["safety_kerb_effective_height"]

        area = (
            b * h +
            (math.pi * r ** 2) / 4 +
            b * r +
            0.5 * r * he
        )

        return area


    def cl_104_1_3_4_design_life(design_dict):
        """
        IRC 5:2015
        Table 104.1.3.4 – Assumed design life
        """

        updated_design = design_dict.copy()
        updated_design.update({
            "clause_104_1_3_4": "IRC 5:2015 Table 104.1.3.4",
            "design_life_years": 100
        })

        return updated_design


    @staticmethod  
    def cl_104_3_1_carriageway_width(carriageway_width, num_lanes):
        # Clause 104.3.1 - Minimum carriageway width: 4250 mm (1-lane), 7500 mm (2-lane), +3500 mm per extra lane.
        """
        IRC 5:2015
        Clause 104.3.1 – Width of carriageway
        """

        result = {
            "clause": "IRC 5:2015 104.3.1",
            "num_lanes": num_lanes,
            "provided_width": carriageway_width,
            "applicable": True,
            "is_compliant": True,
            "remarks": []
        }

        if num_lanes == 1:
            required_width = 4.25
            return required_width # in meters
        if num_lanes == 2:
            required_width = 7.5
            return required_width # in meters
        if num_lanes > 2:
            required_width = 7.5 + 3.5 * (num_lanes - 2)
            return required_width # in meters
    
        # Base requirement
        result["required_min_width"] = required_width

        if carriageway_width < required_width:
            result["is_compliant"] = False
            result["remarks"].append(
                f"Provided width {carriageway_width:.2f} m is less than "
                f"minimum {required_width:.2f} m required for {num_lanes} lane(s)."
            )

        if not result["remarks"]:
            result["remarks"].append("Carriageway width satisfies Clause 104.3.1.")

        return result
    

    @staticmethod
    def cl_104_3_6_footpath_width(footpath, footpath_width):
        """
        IRC 5:2015
        Clause 104.3.6 – Minimum clear width of footpath
        """

        result = {
            "clause": "IRC 5:2015 104.3.6",
            "applicable": False,
            "required_min_clear_width": 1.5,  # meters
            "provided_clear_width": footpath_width,
            "is_compliant": True,
            "remarks": ""
        }

        if footpath == KEY_FOOTPATH[0]:  # "None"
            result["remarks"] = "Footpath not provided; clause not applicable."
            return result

        result["applicable"] = True

        if footpath_width is None:
            result["is_compliant"] = False
            result["remarks"] = "Footpath provided but clear width not specified."
            return result

        if footpath_width < result["required_min_clear_width"]:
            result["is_compliant"] = False
            result["remarks"] = (
                "Footpath clear width is less than minimum 1.5 m required "
                "by IRC 5:2015 Clause 104.3.6."
            )
        else:
            result["remarks"] = "Footpath clear width satisfies Clause 104.3.6."

        return result

        
    @staticmethod
    def cl_105_2_1_protection_to_user(component_placement):
        """
    Applies Clause 105.2.1 protection requirements for edges of structures.

    As per Clause 105.2.1, railings or crash barriers are required along the edges of
    structures. Additionally, where a footpath or cycle track is directly adjacent to the
    carriageway, a crash barrier must be provided between them to safely redirect any
    errant vehicular traffic.

    Parameters
    ----------
    component_placement : list of str
        A list defining the cross-sectional arrangement of components in order
        (e.g., ['Railing', 'Footpath', 'Carriageway', 'Footpath', 'Railing']).
        The presence of 'Footpath' is optional and may not always occur.
        The function modifies this list directly.

    Returns
    -------
    list of str
        The same list passed to the function, updated to include 'Crash Barrier'
        between 'Carriageway' and 'Footpath' wherever they are adjacent.
    """
        i = 0
        while i < len(component_placement) - 1:
            pair = (component_placement[i], component_placement[i+1])

            # Check adjacency
            if pair == ('Carriageway', 'Footpath') or pair == ('Footpath', 'Carriageway'):
                component_placement.insert(i+1, 'Crash Barrier')
                i += 2  # Skip the newly inserted element to avoid infinite loop
            if pair == ('Carriageway', 'Cycle Track') or pair == ('Cycle Track', 'Carriageway'):
                component_placement.insert(i+1, 'Crash Barrier')
                i += 2  # Skip the newly inserted element to avoid infinite loop
            else:
                i += 1

        return component_placement

    

    @staticmethod
    def cl_109_7_2_3_railing_height(footpath, railing_height):
        """Validates and adjusts railing height according to IRC Clause 109.7.2
        
        Railings or parapets shall have a minimum 1.1 meter height above the adjacent 
        roadway or footway safety kerb surface.
        
        Args:
            footpath: String indicating footpath type ("None", "Single Side", or "Both Sides")
            railing_height: Current railing height in mm
            
        Returns:
            float: The validated railing height in mm, adjusted to minimum if necessary
        """
        if footpath in KEY_FOOTPATH:     # None, Single Side, Both Sides
            if railing_height < KEY_RAILING_MIN_HEIGHT[0]:
                railing_height = KEY_RAILING_MIN_HEIGHT[0]
                print("Railing height is less than minimum railing height, adjusted to minimum height of 1100 mm")
        
        return railing_height

    
    '''
    def cl_109_7_2_4_railing_height(railing_height):
        # for this the placemnent of cycle track is needed
        # Clause 109.7.2.3 Railings or parapets shall have a minimum 1.1 meter height above the adjacent roadway or footway safety kerb surface
        if KEY_CYCLE_TRACK[0]:     #None
            if railing_height < KEY_RAILING_MIN_HEIGHT[0]:
                railing_height = KEY_RAILING_MIN_HEIGHT[0]
                print("railing height is less than minimum railing height, changed to minimum height")
        if KEY_CYCLE_TRACK[1]:
            if railing_height < KEY_RAILING_MIN_HEIGHT[1]:
                railing_height = KEY_RAILING_MIN_HEIGHT[1]
                print("railing height is less than minimum railing height, changed to minimum height")
    '''
    
    @staticmethod
    def cl_105_3_3_skew_angle(skew_angle):
        if skew_angle > KEY_MIN_SKEW_ANGLE:
            print("The skew angle is greater than 30 degrees")
            return True
        if skew_angle <= KEY_MIN_SKEW_ANGLE:
            print("WARNING, the skew angle is less than 30 degrees")
            return False


    @staticmethod     
    def cl_105_3_6_logitudinal_gradient(logitudinal_gradient):
        if logitudinal_gradient >= KEY_MIN_LOGITUDINAL_GRADIENT:
            return True
        else:
            return print("Logitudinal gradient is less than the minimum requirement of 0.3 percent.")

    @staticmethod
    def cl_105_3_10_bridge_length_single_curve(bridge_length):
        if bridge_length <= KEY_MAX_BRIDGE_LENGTH_SINGLE_CURVE:
            return True
        else:
            return print("Bridge length exceeds the maximum limit of 30 meters for single curve alignment.")

    
    @staticmethod
    def cl_109_5_wearing_coat(wearing_coat):

        if wearing_coat == KEY_WEARING_COAT[0] or wearing_coat == KEY_WEARING_COAT[1]:
            return True


    @staticmethod
    def cl_109_6_3_shapes(
        barrier_type,
        footpath,
        railing_type,
        design_dict,
        crash_barrier_type,
        median_type=None
    ):

        # EDGE – METALLIC CRASH BARRIER (FIG. 4)
        if barrier_type == KEY_CRASH_BARRIER_TYPE[1]:  # Semi-rigid (metallic)

            geom = metallic_crash_barrier_geometry(crash_barrier_type)

            steel_load = steel_load_from_area(geom['steel_area_mm2'])
            kerb_load = rcc_load_from_area(geom['kerb_area_mm2'])

            total_load = steel_load + kerb_load

            design_dict.update(geom)
            design_dict.update({
                'crash_barrier_load_kNm': round(total_load, 3)
            })

            return design_dict


        # MEDIANS – IRC FIG. 5
        if median_type == KEY_MEDIAN_TYPE[0]:  # Fig. 5(a) Raised kerb

            geom = median_raised_kerb_geometry()
            kerb_load = rcc_load_from_area(geom['median_kerb_area_mm2'])

            design_dict.update(geom)
            design_dict.update({
                'median_load_kNm': round(kerb_load, 3)
            })

            return design_dict


        elif median_type == KEY_MEDIAN_TYPE[1]:  # Fig. 5(b) RCC crash barrier

            geom = median_rcc_crash_barrier_geometry()

            kerb_load = rcc_load_from_area(geom['median_kerb_area_mm2'])
            barrier_load = rcc_load_from_area(geom['rcc_barrier_area_mm2'])

            total_load = kerb_load + barrier_load

            design_dict.update(geom)
            design_dict.update({
                'median_load_kNm': round(total_load, 3)
            })

            return design_dict


        elif median_type == KEY_MEDIAN_TYPE[2]:  # Fig. 5(c) Metallic crash barrier

            geom = median_metallic_crash_barrier_geometry()

            steel_load = steel_load_from_area(geom['median_steel_area_mm2'])
            kerb_load = rcc_load_from_area(geom['median_kerb_area_mm2'])

            total_load = steel_load + kerb_load

            design_dict.update(geom)
            design_dict.update({
                'median_load_kNm': round(total_load, 3)
            })

            return design_dict


        return design_dict
