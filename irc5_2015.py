import math
from common import *


class IRC5_2015(object):

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


    def cl_104_1_3_4_design_life(design_life):
        design_life = 100  # Design life in years as per IRC Clause 104.1.3.4
        return design_life

    '''
    def cl_104_3_1_carriageway_width(carriageway_width, traffic_lanes):
        # Carriageway width requirements (IRC Clause 104.3.1)
        if carriageway_width == 4250: # Single lane
    '''      


    def cl_104_3_6_footpath_width(footpath, footpath_width):
        # Footpath width requirements (IRC Clause 104.3.6)
        if footpath == KEY_FOOTPATH[1]:  # "Single Side"
            if footpath_width < KEY_FOOTPATH_CLEAR_MIN_WIDTH:
                return ValueError("Footpath width is less than the minimum requirement of 1500 mm.")
            if footpath_width >= KEY_FOOTPATH_CLEAR_MIN_WIDTH:
                return footpath_width
        elif footpath == KEY_FOOTPATH[2]:  # "Both Sides"
            if footpath_width < KEY_FOOTPATH_CLEAR_MIN_WIDTH:
                return ValueError("Footpath width is less than the minimum requirement of 1500 mm.")
            if footpath_width >= KEY_FOOTPATH_CLEAR_MIN_WIDTH:
                return footpath_width
        else:
            return False, "No footpath provided; footpath width requirement does not apply."
        

    # def cl_105_2_1_protection_to_user():


    def cl_109_7_2_railing_height(railing_height):
        # Clause 109.7.2.3 Railings or parapets shall have a minimum 1.1 meter height above the adjacent roadway or footway safety kerb surface
        if KEY_CYCLE_TRACK[0]:
            if railing_height < KEY_RAILING_MIN_HEIGHT[0]:
                railing_height = KEY_RAILING_MIN_HEIGHT[0]
                print("railing height is less than minimum railing height, changed to minimum height")
        if KEY_CYCLE_TRACK[1]:
            if railing_height < KEY_RAILING_MIN_HEIGHT[1]:
                railing_height = KEY_RAILING_MIN_HEIGHT[1]
                print("railing height is less than minimum railing height, changed to minimum height")

    

    def cl_105_3_3_skew_angle(skew_angle):
        if skew_angle > KEY_MIN_SKEW_ANGLE:
            print("The skew angle is greater than 30 degrees")
            return True
        if skew_angle <= KEY_MIN_SKEW_ANGLE:
            print("WARNING, the skew angle is less than 30 degrees")
            return False
        
    def cl_105_3_6_logitudinal_gradient(logitudinal_gradient):
        if logitudinal_gradient >= KEY_MIN_LOGITUDINAL_GRADIENT:
            return True
        else:
            raise ValueError("Logitudinal gradient is less than the minimum requirement of 0.3 percent.")
        
    def cl_105_3_10_bridge_length_single_curve(bridge_length):
        if bridge_length <= KEY_MAX_BRIDGE_LENGTH_SINGLE_CURVE:
            return True
        else:
            raise ValueError("Bridge length exceeds the maximum limit of 30 meters for single curve alignment.")

    
    def cl_109_5_wearing_coat(wearing_coat):

        if wearing_coat == KEY_WEARING_COAT[0] or wearing_coat == KEY_WEARING_COAT[1]:
            return True
        
    def cl_109_6_3_shapes(barrier_type, footpath, railing_type, design_dict, crash_barrier_type):
        if barrier_type == KEY_CRASH_BARRIER_TYPE[2]:  # Rigid
            if footpath == KEY_FOOTPATH[1] or footpath == KEY_FOOTPATH[2]:  # Single Side or Both Sides
                if railing_type == KEY_RAILING_TYPE[0]:  # RCC
                    railing_dims = {
                        'railing_height': None,  # Default height in mm, should be validated by cl_109_7_2_railing_height
                        'railing_width': 275,  # in mm
                        'railing_type': 'RCC',
                        'crash_barrier_height': 900,  # in mm
                        'crash_barrier_width': 450,  # in mm
                        'crash_barrier_radius1': 50,  # in mm
                        'crash_barrier_radius2': 250,  # in mm
                        'crash_barrier_top_notch': 175,  # in mm
                        'crash_barrier_base_notch': 100,  # in mm
                        'crash_barrier_middle_length': 550  # in mm
                    }
                    # Validate railing height
                    IRC5_2015.cl_109_7_2_railing_height(railing_dims['railing_height'])
                    design_dict.update(railing_dims)
                    
                elif railing_type == KEY_RAILING_TYPE[1]:  # steel
                    railing_dims = {
                        'railing_height': None,  # Default height in mm, should be validated by cl_109_7_2_railing_height
                        'railing_width': 200,  # in mm        check this
                        'railing_type': 'steel',
                        'crash_barrier_height': 900,  # in mm
                        'crash_barrier_width': 450,  # in mm
                        'crash_barrier_radius1': 50,  # in mm
                        'crash_barrier_radius2': 250,  # in mm
                        'crash_barrier_top_notch': 175,  # in mm
                        'crash_barrier_base_notch': 100,  # in mm
                        'crash_barrier_middle_length': 550  # in mm
                    }
                    # Validate railing height
                    IRC5_2015.cl_109_7_2_railing_height(railing_dims['railing_height'])
                    design_dict.update(railing_dims)
            elif footpath == KEY_FOOTPATH[0] :  # None
                if crash_barrier_type == KEY_RIGID_CRASH_BARRIER_TYPE[0]:  # IRC-5R
                    crash_barrier_dims = {
                        'crash_barrier_height': 1100,  # in mm
                        'crash_barrier_width': 450,  # in mm
                        'crash_barrier_radius1': 50, # in mm
                        'crash_barrier_radius2': 250,  # in mm
                        'crash_barrier_top_notch': 175,  # in mm
                        'crash_barrier_base_notch': 100,  # in mm
                        'crash_barrier_middle_length': 750  # in mm
                    }
                    design_dict.update(crash_barrier_dims)
                elif crash_barrier_type == KEY_RIGID_CRASH_BARRIER_TYPE[1]:  # High Containment
                    crash_barrier_dims = {
                        'crash_barrier_height': 1550,  # in mm
                        'crash_barrier_width': 525,  # in mm
                        'crash_barrier_radius1': 50, # in mm
                        'crash_barrier_radius2': 250,  # in mm
                        'crash_barrier_top_notch': 250,  # in mm
                        'crash_barrier_base_notch': 100,  # in mm
                        'crash_barrier_middle_length': 1200  # in mm
                    }
                    design_dict.update(crash_barrier_dims)











