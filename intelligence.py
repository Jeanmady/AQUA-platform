# intelligence.py has functions that manipulate map image
import numpy as np # imports numpy library
from skimage import io # imports skimage library


def find_red_pixels(map_filename, upper_threshold, lower_threshold):
    """
    Finds the red pixels from map.png then creates a red pixel map file and represents only the red pixels in white
    parameters: map_filename, upper_threshold, lower_threshold
    return: jpg file of just the red pixels shown in white and array of map
    """
    map_img = io.imread(map_filename) # Reads the map.png
    red_pixel_map = np.ndarray((len(map_img), len(map_img[0]))) # Creates a 2d array for the map image
    for rows in range(0, len(map_img)): # For loop using length of map arrray to iterate thrugh the rows
        for columns in range(0, len(map_img[rows])): # Nested for loop using length of coloumns to iterate through the colouns to find red pixels
            if map_img[rows,columns][0] > upper_threshold and map_img[rows,columns][2] < lower_threshold: # Checks if each pixel meets the requirements for it to be a red pixel
                red_pixel_map[rows,columns] = True # Pixel is red so is coloured white
            else:
                red_pixel_map[rows,columns] = False # Pixel is not red so is blacked out
    io.imsave("data/map-red-pixels.jpg", red_pixel_map) # Saves a copy of the red pixel map into data folder
    return red_pixel_map


def find_cyan_pixels(map_filename, upper_threshold, lower_threshold):
    """
    Finds the cyan pixels from map.png then creates a cyan pixel map file and represents only the cyan pixels in white
    parameters: map_filename, upper_threshold, lower_threshold
    return: jpg file of just the cyan pixels shown in white and array of map
    """
    map_img = io.imread(map_filename) # Reads the map.png
    cyan_pixel_map = np.ndarray((len(map_img), len(map_img[0]))) # Creates a 2d array for the map image
    for rows in range(0, len(map_img)): # For loop using length of map arrray to iterate thrugh the rows
        for columns in range(0, len(map_img[rows])): # Nested for loop using length of coloumns to iterate through the colouns to find cyan pixels
            if map_img[rows,columns][0] < lower_threshold and map_img[rows,columns][2] > upper_threshold: # Checks if each pixel meets the requirements for it to be a cyan pixel
                cyan_pixel_map[rows,columns] = True # Pixel is cyan so is coloured white
            else:
                cyan_pixel_map[rows,columns] = False # Pixel is not cyan so is blacked out
    io.imsave("data/map-cyan-pixels.jpg", cyan_pixel_map) # Saves a copy of the cyan pixel map into data folder
    return cyan_pixel_map

                             


def detect_connected_components_sorted(*args,**kwargs):
    """Your documentation goes here"""
    pass


