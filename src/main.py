import argparse
import cv2
import os

def parse_arguments():
    parser = argparse.ArgumentParser(description= "Sat Image analysis")
    parser.add_argument("image_path", help= "Path to image file")
    return parser.parse_args()

def analyze_image(image_path, outputs_folder):
    image = cv2.imread(image_path)

    if image is None:
        print("Error. please check file path")
        return None, None
    
    #convert image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    grayscale_path = os.path.join(outputs_folder, "grayscale.jpg")
    cv2.imwrite(grayscale_path, grayscale_image)

    #pixels with <70 intensity set to 0, otherwise set it to 255
    _, threshold_image = cv2.threshold(grayscale_image, 70, 255, cv2.THRESH_BINARY)

    threshold_path = os.path.join(outputs_folder, "threshold.jpg")
    cv2.imwrite(threshold_path, threshold_image)
    
    #calculate % of land v water
    land_percentage = calculate_land_percentage(threshold_image)
    water_percentage = 100 - land_percentage
    return land_percentage, water_percentage

def calculate_land_percentage(image):
    land_pixels = cv2.countNonZero(image)
    total_pixels = image.size
    land_percentage = (land_pixels/total_pixels) * 100
    return land_percentage

def main():
    args = parse_arguments()
    image_path = args.image_path

    outputs_folder = "outputs"
    os.makedirs(outputs_folder, exist_ok=True)

    land_percentage, water_percentage = analyze_image(image_path, outputs_folder)
    if land_percentage is not None:
        print("Area is {:.2f}% land and {:.2f}% water ".format(land_percentage, water_percentage))
    else:
        print("error analysing image.")

if __name__ ==  "__main__":
    main()