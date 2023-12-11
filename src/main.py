import argparse
import cv2

def parse_arguments():
    parser = argparse.ArgumentParser(description= "Sat Image analysis")
    parser.add_argument("image path", help= "Path to image file")
    return parser.parse_args()

def analyze_image(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Error. please check file path")
        return None
    
    #convert image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #pixels with <125 intensity set to 0, otherwise set it to 255
    _, threshold_image = cv2.threshold(grayscale_image, 125, 255, cv2.THRESH_BINARY)

    #calculate % of land v water
    land_percentage = calculate_land_percentage(threshold_image)
    water_percentage = 100 - land_percentage
    return land_percentage, water_percentage

def calculate_land_percentage(image):
    land_pixels = cv2.countNonZero
    total_pixels = image.size
    land_percentage = (land_pixels/total_pixels) * 100
    return land_percentage






def main():
    args = parse_arguments
    image_path = args.image_path

    land_percentage, water_percentage = analyze_image("image_path")
    if land_percentage is not None:
        print("Area is {:.2f}% land and {:.2f}% water ".format(land_percentage, water_percentage))
    else:
        print("error analysing image.")

if __name__ ==  "__main__":
    main()