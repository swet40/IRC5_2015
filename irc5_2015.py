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
                check = 'Fail'
                return check #Kerb width is less than the minimum requirement of 750 mm.
            elif kerb_width >= KEY_SAFETY_KERB_MIN_WIDTH:
                kerb_placement = KEY_SAFETY_KERB_PLACEMENT[1]  # "Both Sides"
                check = 'Pass'
                return kerb_placement,check  #Kerb width meets the minimum requirement of 750 mm.
        elif footpath == KEY_FOOTPATH[1]:  # "Single Side"
            if kerb_width < KEY_SAFETY_KERB_MIN_WIDTH:
                check = 'Fail'
                return check  #Kerb width is less than the minimum requirement of 750 mm.
            elif kerb_width >= KEY_SAFETY_KERB_MIN_WIDTH:
                kerb_placement = KEY_SAFETY_KERB_PLACEMENT[0]  # "Single Side"
                check = 'Pass'
                return kerb_placement,check  #Kerb width meets the minimum requirement of 750 mm.
        
        
    def cl_109_8_1_road_kerb_outline():
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
        return road_kerb_dimensions
    
    
    def cl_109_8_3_safety_kerb_outline():
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


    def cl_104_1_3_4_design_life(design_life):
        design_life = 100  # Design life in years as per IRC Clause 104.1.3.4

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
            return "No footpath provided; footpath width requirement does not apply."
        

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
        
    def cl_105_3_6_logitudinal_gradient():
        return
    

    



        
    

            
        