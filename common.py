# Unit definitions
kilo = 1e3
milli = 1e-3
N = 1
m = 1
mm = milli * m
m2 = m ** 2
m3 = m ** 3
m4 = m ** 4
kN = kilo * N
Pa = 1
MPa = N / ((mm) ** 2)
GPa = kilo * MPa
kPa = kilo * Pa


KEY_FOOTPATH = ["None", "Single Side", "Both Sides"]
KEY_SAFETY_KERB_MIN_WIDTH = 750  # in mm
KEY_SAFETY_KERB_PLACEMENT = ['Single Side', 'Both Sides', ]
KEY_FOOTPATH_CLEAR_MIN_WIDTH = 1500  # in mm
KEY_RAILING_MIN_HEIGHT = [1100, 1250] # in mm
KEY_CYCLE_TRACK = ['None', 'Single', 'Both Sides'] 
KEY_MIN_SKEW_ANGLE = 30  # in degrees
KEY_WEARING_COAT = ['bituminous', 'concrete']
KEY_CRASH_BARRIER_TYPE = ['Flexible', 'Semi-Rigid', 'Rigid']
KEY_RAILING_TYPE = ['RCC', 'steel']
KEY_MIN_LOGITUDINAL_GRADIENT = 0.3  # in percent
KEY_MAX_BRIDGE_LENGTH_SINGLE_CURVE = 30  # in meters
KEY_RIGID_CRASH_BARRIER_TYPE = ['IRC-5R', 'High Containment']
# Metallic crash barrier sub-types
KEY_METALLIC_CRASH_BARRIER_TYPE = ['Single W-beam', 'Double W-beam']

KEY_MIN_SINGLE_LANE = 4.25  # in meters
KEY_MIN_DOUBLE_LANE = 7.5  # in meters  
KEY_ADDITIONAL_LANE = 3.5  # in meters
KEY_MEDIAN_TYPE = [
    'Raised Kerb',
    'RCC Crash Barrier',
    'Metallic Crash Barrier'
]
