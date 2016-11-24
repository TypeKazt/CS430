import numpy as np
import math


def translate(dx, dy, dz, shape):
    translate_matrix = np.matrix([[1, 0, 0, 0],
                                 [0, 1, 0, 0],
                                 [0, 0, 1, 0]
                                 [dx, dy, dz, 1]],
                                 dtype=np.float_)
    for point in shape.get_coor():
        point.set_coor(*[z[0] for z in (translate_matrix *
                         np.matrix(point.coor(),
                         dtype=np.float_).reshape(4, 1)).tolist()])
    return shape


def scale(x_factor, y_factor, z_factor, opoint, shape):
    scale_matrix = np.matrix([[x_factor, 0, 0, 0],
                             [0, y_factor, 0, 0],
                             [0, 0, z_factor, 0]
                             [0, 0, 0, 1]],
                             dtype=np.float_)
    verts = shape.get_coor()
    for point in verts:
        point.set_coor(*[z[0] for z in (scale_matrix *
                         np.matrix(point.coor(), 
                         dtype=np.float_).reshape(4, 1)).tolist()])
    return shape


def rotate_x(angle, opoint, shape):
    rad = math.radians(angle)
    cos = math.cos(rad)
    sin = math.sin(rad)
    rotate_matrix = np.matrix([[1, 0, 0, 0],
                               [0, cos, -sin, 0],
                               [0, sin, cos, 0],
                               [0, 0, 0, 1]],
                              dtype=np.float_)
    verts = shape.get_coor()
    for point in verts:
        point.set_coor(*[z[0] for z in (rotate_matrix *
                         np.matrix(point.coor(),
                         dtype=np.float_).reshape(4, 1)).tolist()])
    return shape


def rotate_y(angle, opoint, shape):
    rad = math.radians(angle)
    cos = math.cos(rad)
    sin = math.sin(rad)
    rotate_matrix = np.matrix([[cos, 0, sin, 0],
                               [0, 1, 0, 0],
                               [-sin, 0, cos, 0],
                               [0, 0, 0, 1]],
                              dtype=np.float_)
    verts = shape.get_coor()
    for point in verts:
        point.set_coor(*[z[0] for z in (rotate_matrix *
                         np.matrix(point.coor(),
                         dtype=np.float_).reshape(4, 1)).tolist()])
    return shape


def rotate_z(angle, opoint, shape):
    rad = math.radians(angle)
    cos = math.cos(rad)
    sin = math.sin(rad)
    rotate_matrix = np.matrix([[cos, -sin, 0, 0],
                               [sin, cos, 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]],
                              dtype=np.float_)
    verts = shape.get_coor()
    for point in verts:
        point.set_coor(*[z[0] for z in (rotate_matrix *
                         np.matrix(point.coor(),
                         dtype=np.float_).reshape(4, 1)).tolist()])
    return shape


def camera_rotate_mat(u, v, n):
    rmat = np.matrix([[u[0], u[1], u[2], 0],
                      [v[0], v[1], v[2], 0],
                      [n[0], n[1], n[2], 0],
                      [0, 0, 0, 1]],
                     dtype=np.float_)
    return rmat


def translation_matrix(dx, dy, dz):
    translate_matrix = np.matrix([[1, 0, 0, dx],
                                 [0, 1, 0, dy],
                                 [0, 0, 1, dz],
                                 [0, 0, 0, 1]],
                                 dtype=np.float_)
    return translate_matrix


    
    
