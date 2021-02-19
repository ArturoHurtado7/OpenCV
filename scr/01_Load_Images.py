import numpy
import cv2
import os

base_folder = 'Photos'
base_name = 'Maimy_'
base_ext = '.png'



def load_images_from_folder(path, type):
    images = []
    for filename in os.listdir(path):
        img = cv2.imread(os.path.join(path,filename), type)
        if img is not None:
            images.append(img)
    return images

def save_images_from_data(path, images):
    i = 0
    for image in images:
        path_dir = os.path.join(path,base_name+str(i)+base_ext)
        print(path_dir)
        cv2.imwrite(path_dir,image)
        #print(base_name+str(i))
        i += 1

def main ():
    # Carga Imagenes a color
    try:
        images = load_images_from_folder(base_folder, 1)
        for image in images:
            cv2.imshow("image", image)
            cv2.waitKey(0)      # unlimited time, until a key is press
            # cv2.waitKey(1000)   # 1 sec
    
        # Carga Imagenes a blanco y negro
        images = load_images_from_folder(base_folder, 0)
        for image in images:
            cv2.imshow("image", image)
            #cv2.waitKey(0) # unlimited time
            cv2.waitKey(1000) # 1 sec
    except Exception as e:
        print(10, 'Error: Loading image from ', base_folder, e)
    
    save_images_from_data(base_folder,images)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

