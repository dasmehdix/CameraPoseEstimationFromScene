# Aim on this script is visualize the given feature points in images.
# As you know, You gave me the 2D data points for image1.
# I manually extract 2D feature points for image2 & image3.
# You can achieve & load feature points from "image2data2d.npy" and "image3data2d.npy".
# Or, alternatively you can achieve these data points by given arrays.
# Be carefull that images & npy files should be same path with script. If you change the file paths; you have to change it inside the script too..
# Let's visualize some features :)
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

# Create a figure object to visualize images with feature points.
fig = plt.figure(figsize=(16, 8))
rows = 2;columns = 2;
fig.suptitle('2D point cloud visualization on given images')

# Generate multiple subplots which include images with markered feature data points.
plt.subplot(1, 3, 1)
plt.imshow(image_1)
for x,y in data_2d:
    plt.plot(x, y, "og", markersize=10)
plt.title('image1 with 2D feature points')

plt.subplot(1, 3, 2)
plt.imshow(image_2)
for x,y in image_2_data2d:
    plt.plot(x, y, "og", markersize=10,c='blue') 
plt.title('image2 with 2D feature points')

plt.subplot(1, 3, 3)
plt.imshow(image_3)
for x,y in image_3_data2d:
    plt.plot(x, y, "og", markersize=10,c='red')
plt.title('image3 with 2D feature points')

plt.show()