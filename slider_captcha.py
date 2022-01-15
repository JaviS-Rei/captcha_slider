from PIL import Image
import numpy as np

def get_horizon(path):
    x, y = 0, 0
    threshold = 170
    img = np.array(Image.open(path).convert('L')) < threshold

    bar = np.ones([80], bool)
    for i in range(240-1, 0, -1):
        delta = np.sum(bar ^ img[i,:])
        if delta > 20:
            y=i
            break
        
    bar = np.ones([240], bool)
    for i in range(0, 80):
        delta = np.sum(bar ^ img[:,i])
        if delta > 15:
            x=i
            break
           
    return (x,y)
        

def cmp(path, slider_xy):
    threshold = 235
    match_list = []

    img = np.array(Image.open(path).convert('L')) > threshold
    sample = np.array(Image.open(r'.\sample.png').convert('L')) < 127
    
    for i in range(440-57):
        match = np.sum(sample & img[slider_xy[1]-57:slider_xy[1],i:i+57])
        match_list.append(match)
    return (match_list.index(max(match_list)), slider_xy[1])


def return_left_cornor_xy(img_path, bar_path):
    slider_left_cornor_xy = get_horizon(bar_path)
    block_left_cornor_xy = cmp(img_path, slider_left_cornor_xy)
    distance = block_left_cornor_xy[0] - slider_left_cornor_xy[0]
    print("slider_left_cornor_xy: ", slider_left_cornor_xy)
    print("block_left_cornor_xy: ", block_left_cornor_xy)
    print("distance: ", distance)
    return distance

ret = return_left_cornor_xy(r'.\dataset\A1.png', r'.\dataset\B1.png')
