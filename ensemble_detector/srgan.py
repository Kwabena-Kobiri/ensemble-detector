import cv2
import time
import imutils
import time

# image = cv2.imread('../test images/blur 2.jpg')
# resized_image = imutils.resize(image, width=400)
# # print(image[0])
# # print()
# # print(resized_image[0])

# model = cv2.dnn_superres.DnnSuperResImpl_create()

# start = time.time()
# model.readModel('ESPCN_x2.pb')
# model.setModel('espcn',2)
# enhanced_espcn = model.upsample(resized_image)
# end = time.time()
# print('Time spent in enhancing image with ESPCN is: ', end-start)
# cv2.imshow('ESPCN',enhanced_espcn)
# cv2.imshow('Original',resized_image)


# start = time.time()
# model.readModel('FSRCNN_x2.pb')
# model.setModel('fsrcnn',2)
# enhanced_fsrcnn = model.upsample(resized_image)
# end = time.time()
# print('Time spent in enhancing image with FSRCNN is: ', end-start)
# cv2.imshow('FSRCNN',enhanced_fsrcnn)

# cv2.imshow( "Original", resized_image)

##################### ENHANCING VIDEO QUALITY #################################
# vid = cv2.VideoCapture('../test images/video 1.mp4')

# model = cv2.dnn_superres.DnnSuperResImpl_create()
# model.readModel('ESPCN_x2.pb')
# model.setModel('espcn',2)

# while True:
#     ret, frame = vid.read()
    
#     resized_frame = imutils.resize(frame, width=400)
#     enhanced_espcn = model.upsample(resized_frame)
    
#     cv2.imshow('Original', resized_frame)
#     cv2.imshow('Enhanced', enhanced_espcn)
    
#     key = cv2.waitKey(10) & 0xFF
    
#     if key == ord("q"):
#         break

# cv2.waitKey(0)
cv2.destroyAllWindows()