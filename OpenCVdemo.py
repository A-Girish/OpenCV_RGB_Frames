import sys
import time
import cv2

SOURCE = sys.argv[1] if len(sys.argv) > 1 else 0     # 0 = first camera, or a video file path
SHOW = "--headless" not in sys.argv                     # no window on a Pi without a screen

cap = cv2.VideoCapture(int(SOURCE) if str(SOURCE).isdigit() else SOURCE)
if not cap.isOpened():
    sys.exit(f"cannot open {SOURCE}: check the cable, the index, or the file path")
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)                   # ask for 640x480 (the camera may refuse)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

frames, t0 = 0, time.time()
while True:
    ok, frame = cap.read()                               # frame: (h, w, 3) uint8, BGR
    if not ok:
        break 
    frame = cv2.flip(frame, 1)                                           # end of file or camera unplugged
    frames += 1
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)       # most algorithms want one channel
    # // RED frame
    # red_frame = frame.copy()
    # red_frame[:, :, 0] = 0  # Remove Blue
    # red_frame[:, :, 1] = 0  # Remove Green

    # #  Green Frame
    # Green_frame = frame.copy()
    # Green_frame[:, :, 2] = 0  # Remove Red
    # Green_frame[:, :, 0] = 0  # Remove Blue

    # #  Blue frame
    # Green_frame = frame.copy()
    # Green_frame[:, :, 2] = 0  # Remove Red
    # Green_frame[:, :, 0] = 0  # Remove Blue
    

    # small = cv2.resize(Green_frame, (320, 240))
    small = cv2.resize(gray, (320, 240))                 # 4x fewer pixels = ~4x faster
    if frames % 30 == 0:
        fps = frames / (time.time() - t0)
        print(f"{frames} frames, {fps:.1f} FPS, size {frame.shape}, mean brightness {small.mean():.0f}")
    if SHOW:
        # cv2.imshow("camera", Green_frame)
        cv2.imshow("camera", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    if frames == 1:
        # cv2.imwrite("Green_frame.jpg", Green_frame)            # evidence that the camera works
        cv2.imwrite("First_frame.jpg", frame)  

cap.release()
if SHOW:
    cv2.destroyAllWindows()
print(f"done: {frames} frames")