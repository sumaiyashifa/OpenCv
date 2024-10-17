import cv2 as cv
#capture vdo
# abc=cv.VideoCapture(0)
# while(True):
#     ret ,frame=abc.read()
#     cv.imshow("abc" , frame)
#     #close the vdo
#     if cv.waitKey(1) & 0xFF==ord('q'):
#         break
#     abc.release()
# cv.destroyAllWindows()




# Open the video capture
abc = cv.VideoCapture(0)
if not abc.isOpened():
    print("Failed to open the camera.")
    exit()

frame_w = int(abc.get(3))  # Width
frame_h = int(abc.get(4))  # Height

# Use mp4v codec for MP4 format
vdo_cod = cv.VideoWriter_fourcc(*'mp4v')  # Change from 'XVID' to 'mp4v'
vdo_output = cv.VideoWriter("Captured_vdo.mp4", vdo_cod, 30, (frame_w, frame_h))

while True:
    ret, frame = abc.read()
    if ret:
        vdo_output.write(frame)
        cv.imshow("Camera Feed", frame)

        # Close the video with 'q'
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Failed to read frame.")
        break

# Release resources
abc.release()
vdo_output.release()
cv.destroyAllWindows()
print("Video capture successful")
