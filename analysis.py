#threshold midline has to be adjusted based on image...

import cv2
import os

def get_image(image_path):
    image = cv2.imread(image_path) #reads image in and returns openCV matrix
    if image is None:
        print(f"error with image path at {image_path}")
    return image

def convert(image, outputs="outputs"):    #convert image to greyscale and place in folder
    greyscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    #if output folder exists save file there
    os.makedirs(outputs, exist_ok=True)

    grayscale_path = os.path.join(outputs, "grayscale.jpg")
    cv2.imwrite(grayscale_path, greyscale_image)
    return greyscale_image


'''threshold image, pixels with <70 intensity set to 0, otherwise set it to 255'''
def threshold(outputs, midline, greyscale): 
    _, threshold_image = cv2.threshold(greyscale, midline, 255, cv2.THRESH_BINARY)
    #if output folder exists save file there
    os.makedirs(outputs, exist_ok=True)
    threshold_path = os.path.join(outputs, "threshold.jpg")

    try:
        cv2.imwrite(threshold_path, threshold_image)
    except Exception as e:
        print(f"Error saving the image: {0}")
        return None
    return threshold_image

#calculates percetage of land
def land_percentage(threshold_image):
    land_pixels = cv2.countNonZero(threshold_image) #count land pixels
    total_pixels = threshold_image.size
    land_percent = (land_pixels/total_pixels) * 100
    
    water_percent = 100 - land_percent
    return land_percent, water_percent

def main():
    outputs = "outputs"
    
    image = get_image(image_path="data/image01.jpg")
    greyscale = convert(image, outputs)
                        #adjust midline number here
    result = threshold(outputs, 130, greyscale)

    if result is not None:
        land, water = land_percentage(result)
        print(f"\nArea is:\n{land:.2f}% land\n{water:.2f}% water")
    else: 
        print("failed to load image")

main()