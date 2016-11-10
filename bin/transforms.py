import numpy as np
import math


def translate(dx, dy, shape):
    translate_matrix = np.matrix([[1, 0, dx],
                                 [0, 1, dy],
                                 [0, 0, 1]],
                                 dtype=np.float_)
    for point in shape.get_coor():
        point.set_coor(*[z[0] for z in (translate_matrix *
                         np.matrix(point.coor(),
                         dtype=np.float_).reshape(3, 1)).tolist()])
    return shape


def scale(x_factor, y_factor, opoint, shape):
    scale_matrix = np.matrix([[x_factor, 0, 0],
                             [0, y_factor, 0],
                             [0, 0, 1]],
                             dtype=np.float_)
    verts = shape.get_coor()
    dx = verts[0].x-opoint.x
    dy = verts[0].y-opoint.y
#    translate(-dx, -dy, shape)
    for point in verts:
        point.set_coor(*[z[0] for z in (scale_matrix *
                         np.matrix(point.coor(), 
                         dtype=np.float_).reshape(3, 1)).tolist()])
 #   translate(dx, dy, shape)
    return shape


def rotate(angle, opoint, shape):
    rad = math.radians(angle)
    cos = math.cos(rad)
    sin = math.sin(rad)
    rotate_matrix = np.matrix([[cos, -sin, 0],
                              [sin, cos, 0],
                              [0, 0, 1]],
                              dtype=np.float_)
    verts = shape.get_coor()
    dx = verts[0].x-opoint.x
    dy = verts[0].y-opoint.y
    for point in verts:
        point.set_coor(*[z[0] for z in (rotate_matrix *
                         np.matrix(point.coor(),
                         dtype=np.float_).reshape(3, 1)).tolist()])
    return shape




