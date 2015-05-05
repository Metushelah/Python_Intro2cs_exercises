#############################################################################
# FILE: ex7.py
# WRITER : konstantin, guybrush, 30888377
# EXERCISE : intro2cs ex7a 2014-2015
# DESCRIPTION:
# This file holds helper functions for the gui.py file which processes
# images and creates a morphing sequence between them.
# This file manages creation of triangles from lists of points, comparing them
# and creation of intermediate triangles. From there it creates helper lists
# of points through which our images will pass to each other. It then creates
# a number of intermediate images that will show the transformation
#############################################################################

from SolveLinear3 import solve_linear_3


def is_point_inside_triangle(point, v1, v2, v3):
    """
    this function recieves 4 points, and checks if the first is inside the
    triangle created by the other 3, it returns True of False accordingly
    and the result of the linear equation used to check if so.
    input: a tuple representing a point, and 3 more tuples representing the
    edges of the triangle to check
    output: a list holding an answer True/ False if point is inside the
    triangle, and the result of solve_linear_3 (the a,b,c we recieved)
    """
    EQU_COEFFICENT = 1          # the linear equation coefficents 1 according
                                # to Crammer method
    
    result_val = True           # will hold our binary answer True/False
    
    coeff_lst = [[v1[0], v2[0], v3[0]], [v1[1],v2[1],v3[1]],
                             [EQU_COEFFICENT, EQU_COEFFICENT, EQU_COEFFICENT]]
    right_lst = [point[0], point[1], EQU_COEFFICENT]
    
    result = solve_linear_3(coeff_lst, right_lst)
    
    if min(result) < 0:         # according to the guidelines and Crammers
        result_val =  False     # method
    return (result_val, result)  


def create_triangles(list_of_points):
    """
    this function creates tringles from the points given to it in the input.
    input: a list of tuples representing the points on the images
    output: a list holding tuples which represent triangles by holding tuples
    of 2 representing it's edges using (x,y) coordinates.
        e.g: [((x1,y1),(x2,y2),(x3,y3)),...]
    """
    INDEX_START = 4
    
    triangle_lst = [(list_of_points[0], list_of_points[1], list_of_points[2]),
                    (list_of_points[0], list_of_points[2], list_of_points[3])]
    
    for i in range(INDEX_START, len(list_of_points)):
        for j, triangle in enumerate(triangle_lst):
            check = is_point_inside_triangle(list_of_points[i],
                                         triangle[0], triangle[1], triangle[2])
            if check[0] == True:
                triangle_lst.insert(j, (triangle[0], triangle[1],
                                                 list_of_points[i]))
                triangle_lst.insert(j, (triangle[0], triangle[2],
                                                 list_of_points[i]))
                triangle_lst.insert(j, (triangle[1], triangle[2],
                                                 list_of_points[i]))
                triangle_lst.pop(j+3)
                break
        
    return triangle_lst


def _points_match(pt, triangle):
    """
    this is a shortcut function, so i won't need to write this long line
    again each time :P
    input: a tuple for point, and a tuple holding 3 points for a triangle
    output: the result of the function is_point_inside_triangle
    """
    return is_point_inside_triangle(pt, triangle[0], triangle[1], triangle[2])


def do_triangle_lists_match(list_of_points1, list_of_points2):
    """
    this function recieves two lists of points and checks if the triangles
    created for each list are equal on every points index
    input: two list objects holding a list of tuples representing points
    output: True of False if the triangles created match
    """
    triangles_list1 = create_triangles(list_of_points1)
    triangles_list2 = create_triangles(list_of_points2)
    
    for i in range(len(list_of_points1)):
        point_i_1 = list_of_points1[i]
        point_i_2 = list_of_points2[i]
        for j in range(len(triangles_list1)):
            if (_points_match(point_i_1, triangles_list1[j])[0] !=
                         _points_match(point_i_2, triangles_list2[j])[0]):            
                return False
    return True

def get_point_in_segment(p1, p2, alpha):
    """
    This function recieves 2 points (tuples of 2) and a scalar between 0 - 1
    and returns a new point in between them in the ratio of Alpha from pt 1
    input: 2 tuples of 2 representing points and a ratio Alpha
    output: a tuple with the new point
    """
    new_ptx = (1-alpha)*p1[0] + alpha*p2[0]
    new_pty = (1-alpha)*p1[1] + alpha*p2[1]
    return tuple([new_ptx, new_pty])


def get_intermediate_triangles(source_triangles_list, target_triangles_list,
                                                                  alpha):
    """
    This function recieves two lists and an alpha ratio and creates a new list
    of tuples holding the intermediate triangles between them.
    input: a list holding the triangles (tuples of tuples), a list holding the
    triangles list of the target to compare to (tuples of tuples) and a ratio
    alpha between 0-1
    output: a list of tuples representing intermidiate triangles
    """
    inter_triangle_list = []      # this list will hold our ending intermediate
                                  # triangles
    for i in range(len(source_triangles_list)):
        inter_triangle = []
        for j in range(3):
            pt = get_point_in_segment(source_triangles_list[i][j],
                                target_triangles_list[i][j], alpha)
            inter_triangle.append(pt)
        inter_triangle_list.append(tuple(inter_triangle))
    return inter_triangle_list



# until here should be submitted by next week - 18.12.2014


def _get_triangle_index(pt, triangle_list):
    """
    This function helps find a triangle within which the point exists and 
    returns it's index number in the list and it's a,b,c variables
    input: a tuple representing point to check and a list of tuples for
    triangles
    output: a tuple holding an index in the first place and a tuple for the
    3 variables (a,b,c) to return
    """
    for i, triangle in enumerate(triangle_list):
        check = _points_match(pt, triangle)
        if check[0]:
            return (i, check[1])


def create_new_pt(coefficents_abc, triangle_edges):
    """
    This function creates a new point by multiplying the coefficents with the
    appropriate v1, v2, v3 coordinate to create a new (x',y') coordinate
    input: a tuple holding the coefficents, and a triangle holding the points
    output: a new tuple point
    """
    new_pt_x = (coefficents_abc[0] * triangle_edges[0][0] +
                coefficents_abc[1] * triangle_edges[1][0] +
                coefficents_abc[2] * triangle_edges[2][0])
    new_pt_y = (coefficents_abc[0] * triangle_edges[0][1] +
                coefficents_abc[1] * triangle_edges[1][1] +
                coefficents_abc[2] * triangle_edges[2][1])
    return ((new_pt_x, new_pt_y))


def get_array_of_matching_points(size,triangles_list ,
                                 intermediate_triangles_list):
    """
    This function recieves a matrix of points on an image and it calculates
    new points on the triangle list via the intermediate triagle list given
    input: a size tuple holding the max pixels in the image on the X and Y axis
    It also recieves a list of tuples representing the triangles and a list of
    tuples representing the intermediate triangles
    output: a list of list the size of "size" 
    """
    new_points_list = []
    previous_index = 0          #initialization, will hold our previous index

    for y in range(size[1]):
        new_points_list.append([])
        for x in range(size[0]):
            pt = (x,y)
            # result tuple will hold my index and the abc recieved (i, (a,b,c))
            check = _points_match(pt, 
                            intermediate_triangles_list[previous_index])
            if check[0]:    
                result = (previous_index, check[1])
            else:
                result = _get_triangle_index(pt, intermediate_triangles_list)
                previous_index = result[0]
            
            
            triangle = triangles_list[result[0]] # the triangle at that index
            coefficents = result [1]    # my coefficents gained in the triangle
            
            new_point = create_new_pt(coefficents, triangle)
            new_points_list[y].append(new_point)
       
    return new_points_list


def _new_rgb_value(alpha, source_rgb, target_rgb):
    """
    This function recieves an alpha and two tuples representing rgb values of
    a specific point in an image and returns their intermediate according to
    alpha
    input: alpha: the ratio to which they should be
           source_rgb: tuple holding the rgb values in the pixel
           target_rgb: tuple holding the rgb values in the pixel
    output: returns a new tuples holding the intermediate rgb value
    """
    red_value = int((1-alpha) * source_rgb[0] + alpha * target_rgb[0])
    green_value = int((1-alpha) * source_rgb[1] + alpha * target_rgb[1])
    blue_value = int((1-alpha) * source_rgb[2] + alpha * target_rgb[2])
    return (red_value, green_value, blue_value)


def create_intermediate_image(alpha, size, source_image, target_image,
                              source_triangles_list, target_triangles_list):
    """
    This function recieves two images represented in a matrix and their 
    representing triangles and creates an image inbetween according to the
    alpha given.
    input: alpha: a scalar from 0 (source image) to 1 (target image) 
    representing how close should the new image be to each of those.
            size: a matrix holding the size of the image
            source_image: a matrix holding the image values 
            target_image: a matrix holding the image values 
            source_triangles_list: a list holding tuples representing the 
                                    triangles on the image
            target_triangles_list: a list holding tuples representing the 
                                    triangles on the image
    output: an image in between the source and the target according to alpha
    """
    new_image = []    #init image with matrix size
    for i in range (size[1]):
        new_image.append([])
        for j in range (size[0]):
            new_image[i].append(0)
       
    inter_triangles = get_intermediate_triangles(source_triangles_list,
                                                 target_triangles_list, alpha)
    source_matching_pts = get_array_of_matching_points(size,
                                     source_triangles_list , inter_triangles)
    target_matching_pts = get_array_of_matching_points(size,
                                     target_triangles_list , inter_triangles)
    
    for y in range(len(new_image)):
        for x in range(len(new_image[0])):
            src_pt = source_matching_pts[y][x]
            trg_pt = target_matching_pts[y][x]

            source_rgb = source_image[src_pt[0], src_pt[1]]
            target_rgb = target_image[trg_pt[0], trg_pt[1]]

            new_image[y][x] = _new_rgb_value(alpha, source_rgb, target_rgb)

    return new_image
    


def create_sequence_of_images(size, source_image, target_image, 
                source_triangles_list, target_triangles_list, num_frames):
    """
    This function calls for the create_intermediate_image function and creates
    a number of frames of such images between the souce and the target images
    input: size: the matrix size of the image
           source_image: a matrix holding the image pixels
           target_image: a matrix holding the image pixels
           source_triangles_list: a list holding the triangles tuples
           target_triangles_list: a list holding the triangles tuples
           num_frames: the number of intermediate images to create
    output: a list of images between source and target images according to
    number of frames to create
    """
    image_list = []
    
    for frame in range(num_frames):
        alpha = frame / (num_frames-1)
        image_list.append(create_intermediate_image(alpha, size, source_image,
                  target_image, source_triangles_list, target_triangles_list))
    
    return image_list


# until here should be submitted by 25.12.2014

