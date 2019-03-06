import cv2
import numpy as np
 
#gray image transformation 
image = cv2.imread("clouds.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Over the Clouds", image)
cv2.imshow("Over the Clouds - gray", gray_image)
cv2.imwrite('grayimage.jpg', gray_image)

#median filter 
median_image = cv2.medianBlur(gray_image,5)
cv2.imshow("Over the Clouds - median", median_image)
cv2.imwrite('median.jpg', median_image)

#min filter
kernel = np.ones((5,5),np.uint8)
min_image = cv2.erode(gray_image,kernel,iterations = 1)
cv2.imshow("Over the Clouds - min", min_image)
cv2.imwrite('min.jpg', min_image)

#max filter 
max_image = cv2.dilate(gray_image,kernel,iterations = 1)
cv2.imshow("Over the Clouds - max",max_image )
cv2.imwrite('max.jpg', max_image)

#laplacian filter 
laplace_image = cv2.Laplacian(median_image,cv2.CV_64F)
cv2.imwrite('laplace.jpg', laplace_image)

#sobel horizontal filter 
sobelh_image = cv2.Sobel(median_image,cv2.CV_64F,1,0,ksize=5)
cv2.imwrite('sobel_h.jpg', sobelh_image)

#sobel vertical filter 
sobelv_image = cv2.Sobel(median_image,cv2.CV_64F,0,1,ksize=5)
cv2.imwrite('sobel_v.jpg', sobelv_image)


cv2.waitKey(0)
cv2.destroyAllWindows()
