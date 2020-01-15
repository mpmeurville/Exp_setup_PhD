# Exp_setup_PhD

capture_python.py: allows to take pictures at a regular time interval. Can enable / disable autofocus and set the image quality
video_python.py: records and saves a video over a defined amount of time, in Grayscales, enable / disable autofocus. 
both_cap_vid.py: Allows to take a video over a defined time and take simultaneously pictures every xx seconds, and save them, while controlling focus, image quality, video codec etc. Adds a timestamp on both captures and for each video frame. 


“set_default_settings_both_cams.py”: regroups determine_brightness_from_pictures.py, determine_focus_from_pictures.py and determine_contrast_from_pictures.py. Aims at making captures for each value of focus, brightness and contrast from a given list. Then, by looking at the pictures taken from both cams, choosing good default parameters for each webcam is easier. 