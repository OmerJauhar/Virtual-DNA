import cv2
import numpy as np
from mtcnn.mtcnn import MTCNN

# Global variables to store dominant eye colors
mother_dominant_eye_color = None
father_dominant_eye_color = None
child_dominant_eye_color = None

detector = MTCNN()

# Define HSV color ranges for eye colors
class_name = ("Blue", "Blue Gray", "Brown", "Brown Gray", "Brown Black", "Green", "Green Gray", "Other")
EyeColor = {
    class_name[0]: ((166, 21, 50), (240, 100, 85)),
    class_name[1]: ((166, 2, 25), (300, 20, 75)),
    class_name[2]: ((2, 20, 20), (40, 100, 60)),
    class_name[3]: ((20, 3, 30), (65, 60, 60)),
    class_name[4]: ((0, 10, 5), (40, 40, 25)),
    class_name[5]: ((60, 21, 50), (165, 100, 85)),
    class_name[6]: ((60, 2, 25), (165, 20, 65))
}

def check_color(hsv, color):
    if (hsv[0] >= color[0][0]) and (hsv[0] <= color[1][0]) and (hsv[1] >= color[0][1]) and \
    hsv[1] <= color[1][1] and (hsv[2] >= color[0][2]) and (hsv[2] <= color[1][2]):
        return True
    else:
        return False

# Define eye color category rules in HSV space
def find_class(hsv):
    color_id = 7
    for i in range(len(class_name) - 1):
        if check_color(hsv, EyeColor[class_name[i]]) == True:
            color_id = i
    return color_id

def calculate_eye_color_probabilities(parent1_color, parent2_color, child_color):
    # Probabilities based on parent eye colors
    probabilities = {
        ('Brown', 'Brown', 'Brown'): 0.75,
        ('Brown', 'Brown', 'Green'): 0.188,
        ('Brown', 'Brown', 'Blue'): 0.063,
        ('Blue', 'Blue', 'Blue'): 0.99,
        ('Blue', 'Blue', 'Green'): 0.01,
        ('Blue', 'Blue', 'Brown'): 0,
        ('Green', 'Green', 'Green'): 0.75,
        ('Green', 'Green', 'Blue'): 0.25,
        ('Green', 'Green', 'Brown'): 0,
        ('Brown', 'Blue', 'Brown'): 0.5,
        ('Brown', 'Blue', 'Blue'): 0.5,
        ('Brown', 'Blue', 'Green'): 0,
        ('Brown', 'Green', 'Brown'): 0.5,
        ('Brown', 'Green', 'Green'): 0.375,
        ('Brown', 'Green', 'Blue'): 0.125,
        ('Blue', 'Green', 'Blue'): 0.5,
        ('Blue', 'Green', 'Green'): 0.5,
        ('Blue', 'Green', 'Brown'): 0 
    }
    relatedness = probabilities.get((parent1_color, parent2_color, child_color), None)
    return relatedness

def eye_color(image, person_name):
    global mother_dominant_eye_color, father_dominant_eye_color, child_dominant_eye_color
    
    imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, w = image.shape[0:2]
    imgMask = np.zeros((image.shape[0], image.shape[1], 1))
    
    result = detector.detect_faces(image)
    if result == []:
        print(f'Warning: Can not detect any face in the {person_name} image!')
        return

    bounding_box = result[0]['box']
    left_eye = result[0]['keypoints']['left_eye']
    right_eye = result[0]['keypoints']['right_eye']

    eye_distance = np.linalg.norm(np.array(left_eye) - np.array(right_eye))
    eye_radius = eye_distance / 15  # approximate
   
    cv2.circle(imgMask, left_eye, int(eye_radius), (255, 255, 255), -1)
    cv2.circle(imgMask, right_eye, int(eye_radius), (255, 255, 255), -1)

    cv2.rectangle(image, (bounding_box[0], bounding_box[1]),
                  (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]), (255, 155, 255), 2)

    cv2.circle(image, left_eye, int(eye_radius), (0, 155, 255), 1)
    cv2.circle(image, right_eye, int(eye_radius), (0, 155, 255), 1)

    eye_class = np.zeros(len(class_name), float)

    for y in range(0, h):
        for x in range(0, w):
            if imgMask[y, x] != 0:
                eye_class[find_class(imgHSV[y, x])] += 1 

    main_color_index = np.argmax(eye_class[:len(eye_class) - 1])
    total_vote = eye_class.sum()

    dominant_eye_color = class_name[main_color_index]
    
    if person_name == 'Mother':
        mother_dominant_eye_color = dominant_eye_color
    elif person_name == 'Father':
        father_dominant_eye_color = dominant_eye_color
    elif person_name == 'Child':
        child_dominant_eye_color = dominant_eye_color

    print(f"\n\nDominant Eye Color of {person_name}: ", dominant_eye_color)
    print("\n **Eyes Color Percentage **")
    for i in range(len(class_name)):
        print(class_name[i], ": ", round(eye_class[i] / total_vote * 100, 2), "%")
    
    label = 'Dominant Eye Color: %s' % dominant_eye_color  
    cv2.putText(image, label, (left_eye[0] - 10, left_eye[1] - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (155, 255, 0))
    cv2.imshow(f'{person_name} Eye Color Detection', image)
    
    return eye_class

if __name__ == '__main__':
    # Paths to images of mother, father, and child
    mother_image_path = '/home/mubeen/Desktop/Eye-Color-Detection/mother4.jpg'
    father_image_path = '/home/mubeen/Desktop/Eye-Color-Detection/father1.jpg'
    child_image_path = '/home/mubeen/Desktop/Eye-Color-Detection/child22.jpg'
    # Load images
    mother_image = cv2.imread(mother_image_path, cv2.IMREAD_COLOR)
    father_image = cv2.imread(father_image_path, cv2.IMREAD_COLOR)
    child_image = cv2.imread(child_image_path, cv2.IMREAD_COLOR)

    # Detect and analyze eye color for each person
    mother_eye_class = eye_color(mother_image, 'Mother')
    father_eye_class = eye_color(father_image, 'Father')
    child_eye_class = eye_color(child_image, 'Child')

    # Determine detected eye colors
    mother_eye_color = class_name[np.argmax(mother_eye_class)]
    father_eye_color = class_name[np.argmax(father_eye_class)]
    child_eye_color = class_name[np.argmax(child_eye_class)]

    # Determine biological relatedness of the child to the parents
    relatedness = calculate_eye_color_probabilities(mother_dominant_eye_color, father_dominant_eye_color, child_dominant_eye_color)
    if relatedness is not None:
        print(f"The child is biologically related to the parents by approximately {relatedness*100:.2f}%")
    else:
        print("Biological relatedness could not be determined.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

