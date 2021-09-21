import numpy as np 
import matplotlib.pyplot as plt
import cv2

# Read 2D Feature points of the image2(manually extracted)
image_2_data2d = np.array([[1128.,536.], 
                          [1128.,536.],
                          [1076.,533.],
                          [1076.,533.],
                          [369.,545.],
                          [369.,545.],
                          [584.,642.],
                          [584.,642.],
                          [1213.,8.],
                          [1100.,667.],
                          [1100.,667.],
                          [909.,92.],
                          [764.,406.],
                          [764.,406.],
                          [946.,311.],
                          [946.,311.],
                          [1133.,238.],
                          [736.,622.],
                          [736.,622.],
                          [826.,623.]])
# Alternatively, you can achieve it from "image2data2d.npy" file, just uncomment line below
# image_2_data2d = np.load('image2data2d.npy')

# Read 2D Feature points of the image3(manually extracted)
image_3_data2d = np.array([[1173.,560.],
                          [1173.,560.],
                          [1115.,563.],
                          [1115.,563.],
                          [10.,558.],
                          [10.,558.],
                          [331.,676.],
                          [331.,676.],
                          [1221.,1.],
                          [1134.,757.],
                          [1134.,757.],
                          [780.,1.],
                          [567.,386.],
                          [567.,386.],
                          [878.,274.],
                          [878.,274.],
                          [1131.,178.],
                          [531.,645.],
                          [531.,645.],
                          [940.,612.]])

# Alternatively, you can achieve it from "image3data2d.npy" file, just uncomment line below
# image_3_data2d = np.load('image3data2d.npy')

# Let's load 2D feature points of image1 & 3D points in world coordinate system
data_2d = np.load('vr2d.npy')
data_3d = np.load('vr3d.npy')
print('2D Shape: {}'.format(data_2d.shape))
print('3D Shape: {}'.format(data_3d.shape))

# Both 2D & 3D point arrays are in 3D format. I reshape them to 2D(we do not need 3rd dimension which is empty)
data_2d = data_2d.reshape(20,2)
data_3d = data_3d.reshape(20,3)

# Let's read images
image_1 = cv2.imread('img1.png',cv2.IMREAD_COLOR)
image_2 = cv2.imread('img2.png',cv2.IMREAD_COLOR)
image_3 = cv2.imread('img3.png',cv2.IMREAD_COLOR)

size = image_1.shape  #Image shape 
focal_length = 100  #Given focal length
dist_coeffs = np.zeros((4,1)) #Given distortion(zero matrix)
center = (size[1]/2, size[0]/2) #Middle points of the image matrix

#Camera matrix calculation with focal length and center points
camera_matrix = np.array(
                         [[focal_length, 0, center[0]],
                         [0, focal_length, center[1]],
                         [0, 0, 1]], dtype = "double"
                         )
print("Camera Matrix :\n {0}".format(camera_matrix))

# Let's calculate Camera Pose(rotation+translation matrixes) for Image_1 by given 3D & 2D feature points, distortion and camera matrix.
(success, rotation_vector, translation_vector) = cv2.solvePnP(data_3d, data_2d, camera_matrix, dist_coeffs, flags=cv2.SOLVEPNP_ITERATIVE)
print('SUCCES for Image1=={}'.format(success))
print("Rotation Vector for Image1:\n {0}".format(rotation_vector))
print("Translation Vector for Image1:\n {0}".format(translation_vector))

# Let's calculate Camera Pose(rotation+translation matrixes) for Image_2 by given 3D & 2D feature points, distortion and camera matrix.
(success, rotation_vector_2, translation_vector_2) = cv2.solvePnP(data_3d, image_2_data2d, camera_matrix, dist_coeffs, flags=cv2.SOLVEPNP_ITERATIVE)
print('SUCCESFULL for Image2=={}'.format(success))
print("Rotation Vector for Image2:\n {0}".format(rotation_vector_2))
print("Translation Vector for Image3:\n {0}".format(translation_vector_2))

# Let's calculate Camera Pose(rotation+translation matrixes) for Image_3 by given 3D & 2D feature points, distortion and camera matrix.
(success, rotation_vector_3, translation_vector_3) = cv2.solvePnP(data_3d, image_3_data2d, camera_matrix, dist_coeffs, flags=cv2.SOLVEPNP_ITERATIVE)
print('SUCCESFULL for Image3=={}'.format(success))
print("Rotation Vector for Image3:\n {0}".format(rotation_vector_3))
print("Translation Vector for Image3:\n {0}".format(translation_vector_3))


trans2_1 = translation_vector_2-translation_vector # Translation matrix of Image2 w.r.t. Image1
trans3_1 = translation_vector_3-translation_vector # Translation matrix of Image3 w.r.t. Image1
rotat2_1 = rotation_vector_2-rotation_vector #  Rotation matrix of Image2 w.r.t. Image1
rotat3_1 = rotation_vector_3-rotation_vector #  Rotation matrix of Image3 w.r.t. Image1
trans1 = np.array([0,0,0]) #Translation matrix of Image1(Assume that translation matrix of Image1 is zeros which means we use as reference point)

# Let's create a 3D figure
fig = plt.figure(figsize = (16, 16))
ax = plt.axes(projection = '3d')
ax.set_title('TRANSLATION RESPECT TO CAM POS 1 IN IMAGE 1')
# Let's scatter the points inside figure two visualize the points.
i1 = ax.scatter(trans1[0],trans1[1],trans1[2], 'green',s=1000)
i2 = ax.scatter(-trans2_1[0],trans2_1[1],-trans2_1[2], 'blue',s=1000,marker='*')
i3 = ax.scatter(-trans3_1[0],trans3_1[1],-trans3_1[2], 'red',s=1000,marker='*')
# Plotting lines from camera pose in Image1 to camera pose in other Images.
ax.plot([-trans2_1[0],trans1[0]], [trans2_1[1],trans1[1]], [-trans2_1[2],trans1[2]],'--', color='red')
ax.plot([-trans3_1[0],trans1[0]], [trans3_1[1],trans1[1]], [-trans3_1[2],trans1[2]],'-.', color='red')
# Legending on figure
ax.legend((i1,i2,i3),('img1Cam1= {}'.format(trans1),'img2Cam2= {}'.format(trans2_1),'img3Cam3= {}'.format(trans3_1)))
# Axis Names
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
#ax.view_init(60, 0)
plt.show()

rotat1 = np.array([0,0,0])

fig = plt.figure(figsize = (16, 16))
ax = plt.axes(projection = '3d')
ax.set_title('Rotation RESPECT TO CAM POS 1 IN IMAGE 1')
# Let's scatter the points inside figure two visualize the points.
i1 = ax.scatter(rotat1[0],rotat1[1],rotat1[2], 'green',s=1000)
i2 = ax.scatter(rotat2_1[0],rotat2_1[1],rotat2_1[2], 'blue',s=1000,marker='*')
i3 = ax.scatter(rotat3_1[0],rotat3_1[1],rotat3_1[2], 'red',s=1000,marker='*')
ax.plot([rotat2_1[0],rotat1[0]], [rotat2_1[1],rotat1[1]], [rotat2_1[2],rotat1[2]],'--', color='red')
ax.plot([rotat3_1[0],rotat1[0]], [rotat3_1[1],rotat1[1]], [rotat3_1[2],rotat1[2]],'-.', color='red')
# Legending on figure
ax.legend((i1,i2,i3),('img1Cam1= {}'.format(trans1),'img2Cam2= {}'.format(trans2_1),'img3Cam3= {}'.format(trans3_1)))
# Axis Names
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
#ax.view_init(60, 0)
plt.show()