import numpy as np

##################
# Utils
################

# angle_1 - angle_2
# contains direction in range [-3.14, 3.14]
def find_angle_diff(angle_1, angle_2):
    angle_diff_raw = angle_1 - angle_2
    angle_diff = (angle_diff_raw + np.pi) % (2 * np.pi) - np.pi
    return angle_diff

# keep angle between [-pi, pi]
def wrap(angle):
    while angle >= np.pi:
        angle -= 2*np.pi
    while angle < -np.pi:
        angle += 2*np.pi
    return angle

def find_nearest(array,value):
    # array is a 1D np array
    # value is an scalar or 1D np array
    tiled_value = np.tile(np.expand_dims(value,axis=0).transpose(), (1,np.shape(array)[0]))
    idx = (np.abs(array-tiled_value)).argmin(axis=1)
    return array[idx], idx

def rad2deg(rad):
    return rad*180/np.pi

def rgba2rgb(rgba):
    # rgba is a list of 4 color elements btwn [0.0, 1.0]
    # returns a list of rgb values between [0.0, 1.0] accounting for alpha and background color [1, 1, 1] == WHITE
    alpha = rgba[3]
    r = max(min((1 - alpha) * 1.0 + alpha * rgba[0],1.0),0.0)
    g = max(min((1 - alpha) * 1.0 + alpha * rgba[1],1.0),0.0)
    b = max(min((1 - alpha) * 1.0 + alpha * rgba[2],1.0),0.0)
    return [r,g,b]