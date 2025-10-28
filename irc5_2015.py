import math
from common import *


class IRC5_2015(object):

    def cl_101_41_safety_kerb_width(kerb_width, footpath):
        """Safety kerb width requirements (IRC Clause 101.41)
    
           IRC 5:2015 Standard: Minimum width = 750mm (0.75m)
        """
        # A kerb having width of at least 750 mm for occasional use by pedestrians, where footpath is not provided.

        if footpath == KEY_FOOTPATH[0]:  # "None"
            if kerb_width < KEY_SAFETY_KERB_MIN_WIDTH:            
                check = False
                return check #Kerb width is less than the minimum requirement of 750 mm.
            elif kerb_width >= KEY_SAFETY_KERB_MIN_WIDTH:
                kerb_placement = KEY_SAFETY_KERB_PLACEMENT[1]  # "Both Sides"
                check = True
                return kerb_placement,check  #Kerb width meets the minimum requirement of 750 mm.
        elif footpath == KEY_FOOTPATH[1]:  # "Single Side"
            if kerb_width < KEY_SAFETY_KERB_MIN_WIDTH:
                check = False
                return check  #Kerb width is less than the minimum requirement of 750 mm.
            elif kerb_width >= KEY_SAFETY_KERB_MIN_WIDTH:
                kerb_placement = KEY_SAFETY_KERB_PLACEMENT[0]  # "Single Side"
                check = True
                return kerb_placement,check  #Kerb width meets the minimum requirement of 750 mm.
        
        
    def cl_109_8_1_road_kerb_outline(design_dict):
        """Road kerb dimensions as per IRC 5:2015
        Clause 109.8.1 - Standard dimensions for road kerbs
        """
        road_kerb_dimensions = {
            'road_kerb_width': 225,  # width in mm
            'road_kerb_effective_width': 175,  # effective width in mm, its minimum value
            'road_kerb_height': 225,  # height in mm
            'road_kerb_effective_height': 200,  # effective height in mm
            'road_kerb_edge_radius': 25  # edge radius in mm
        }

        design_dict.update(road_kerb_dimensions)
        return design_dict
    
    
    def cl_109_8_3_safety_kerb_outline(design_dict):
        # Clause 109.8.3 - A safety kerb will have the same outline as that of a road kerb, except that the top width shall not be less than 750 mm.
        
        # Get road kerb dimensions
        kerb_dims = IRC5_2015.cl_109_8_1_road_kerb_outline()

        # Create safety kerb dimensions based on road kerb dimensions

        safety_kerb_dimensions = {
            'safety_kerb_width': kerb_dims['road_kerb_width'],  # width in mm
            'safety_kerb_effective_width': kerb_dims['road_kerb_effective_width'],  # effective width in mm
            'safety_kerb_height': kerb_dims['road_kerb_height'],  # height in mm
            'safety_kerb_effective_height': kerb_dims['road_kerb_effective_height'],  # effective height in mm
            'safety_kerb_edge_radius': kerb_dims['road_kerb_edge_radius']  # edge radius in mm
        }

        if safety_kerb_dimensions['safety_kerb_width'] < KEY_SAFETY_KERB_MIN_WIDTH:
            safety_kerb_dimensions['safety_kerb_width'] = KEY_SAFETY_KERB_MIN_WIDTH  # width in mm
        elif safety_kerb_dimensions['safety_kerb_width'] >= KEY_SAFETY_KERB_MIN_WIDTH:
            safety_kerb_dimensions['safety_kerb_width'] = safety_kerb_dimensions['safety_kerb_width']  # width in mm

        design_dict.update(safety_kerb_dimensions)

        safety_kerb_area = (safety_kerb_dimensions['safety_kerb_effective_width'] * safety_kerb_dimensions['safety_kerb_height'] +
                            (math.pi * safety_kerb_dimensions['safety_kerb_edge_radius'] ** 2)/4   +
                            safety_kerb_dimensions['safety_kerb_effective_width'] * safety_kerb_dimensions['safety_kerb_edge_radius'] +
                            0.5 * safety_kerb_dimensions['safety_kerb_edge_radius'] * safety_kerb_dimensions['safety_kerb_effective_height'])  # in mm^2
        design_dict['safety_kerb_area'] = safety_kerb_area  # in mm^2
        return design_dict


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
                print("Footpath width is less than the minimum requirement of 1500 mm.")
                return None
            if footpath_width >= KEY_FOOTPATH_CLEAR_MIN_WIDTH:
                return footpath_width
        elif footpath == KEY_FOOTPATH[2]:  # "Both Sides"
            if footpath_width < KEY_FOOTPATH_CLEAR_MIN_WIDTH:
                print("Footpath width is less than the minimum requirement of 1500 mm.")
                return None
            if footpath_width >= KEY_FOOTPATH_CLEAR_MIN_WIDTH:
                return footpath_width
        else:
            return None, print("No footpath provided; footpath width requirement does not apply.")
        

    def cl_105_2_1_protection_to_user(footpath, cycle_track, railing_type, design_dict, crash_barrier_type):
        if footpath == KEY_FOOTPATH[0]:  # "None"
            return
    


    def cl_109_7_2_3_railing_height(footpath, railing_height):
        # Clause 109.7.2 Railings or parapets shall have a minimum 1.1 meter height above the adjacent roadway or footway safety kerb surface
        if footpath == KEY_FOOTPATH[0,1,2]:     #None, Single Side, Both Sides
            if railing_height < KEY_RAILING_MIN_HEIGHT[0]:
                railing_height = KEY_RAILING_MIN_HEIGHT[0]
                print("railing height is less than minimum railing height, changed to minimum height")

    
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











