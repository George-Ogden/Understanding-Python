import cv2
import time, os

# image = cv2.imread("Python.png")
# # print(image)
# image = cv2.resize(image,(500,500))
# cv2.imshow("image",image)

cap = cv2.VideoCapture("video.mp4")
scale = 0.5
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) * scale)
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) * scale)
fps = int(cap.get(cv2.CAP_PROP_FPS))
# print(w,h,fps)

if not os.path.exists("output"):
    os.mkdir("output")
writer = cv2.VideoWriter("output.mp4",cv2.VideoWriter_fourcc(*"mp4v"),fps,(w,h))
i = 1
result, image = cap.read()
while result:
    image = cv2.resize(image,(0,0),fx=scale,fy=scale)
    cv2.rectangle(image,(w-100,0),(w,40),(0,0,0),-1)
    cv2.putText(image,f"{i:03}",(w-80,30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    # cv2.imwrite(f"output/{i:03}.jpg",image)
    writer.write(image)
    i += 1
    cv2.imshow("image",image)
    cv2.waitKey(1)
    result, image = cap.read()

cap.release()
cv2.destroyAllWindows()
# while True:
#     cv2.waitKey(1)
#     time.sleep(1)