import os
import cv2

path = "C:\\Users\\mauri\\Desktop\\Fase 3\\103_Pressure_Coef_Build_Dynamic_X_X_Cut_Pressure_Coef_folder\\103_Pressure_Coef_Build_Dynamic_X_X_Cut_Pressure_Coef_folder\\"
files = sorted(os.listdir(path))

img_array =[]

for i in range(0,len(files)):
    files_name=files[i]
    files_address=path+files_name

    img =cv2.imread(files_address)
    img_array.append(img)

alto, ancho = img.shape[:2]

video = cv2.VideoWriter("video.mp4",cv2.VideoWriter_fourcc(*'mp4v'),10,(ancho,alto))

for i in range(0,len(files)):
    video.write(img_array[i])


video.release()