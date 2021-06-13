#! python3
# import the necessary packages
from imutils.video import FPS
import imutils
import cv2

videoFile = "file path to your video"

# initialize tracker objects
tracker = cv2.TrackerCSRT_create
# tracker = cv2.TrackerKCF_create

# initialize video feed from file and pause on the first frame
vs = cv2.VideoCapture(videoFile)
fps = None
boundBox = None
while True:
    # grab the current frame
    frame = vs.read()
    frame = frame[1]
    # end loop at the end of the video
    if frame is None:
        break
    # resize the frame
    frame = imutils.resize(frame, width=1000)
    (H, W) = frame.shape[:2]
    # show the frame
    cv2.imshow("Frame", frame)
    # if a bounding box has not been established (the first frame) select a bounding box for tracking
    if boundBox is None:
        boundBox = cv2.selectROI("Frame", frame, fromCenter=False,
                               showCrosshair=True)
    # initialize the object tracking algoritm
    tracker.init(frame, boundBox)
    # if tracking works then pull the bounding box coordinates
    if success:
        (x, y, w, h) = [int(v) for v in box]
        cv2.rectangle(frame, (x, y), (x + w, y + h),
                          (0, 255, 0), 2)
    # initialize the FPS counter
    fps = FPS().start()
    # initialize the set of information we'll be displaying on
    # the frame
    info = [
        ("Tracker", tracker),
        ("Success", "Yes" if success else "No"),
        ("FPS", "{:.2f}".format(fps.fps())),
        ]
    # loop over the info tuples and draw them on our frame
    for (i, (k, v)) in enumerate(info):
        text = "{}: {}".format(k, v)
        cv2.putText(frame, text, (10, H - ((i * 20) + 20)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    fps.update()
    fps.stop()
    # establish 's' ket as an E stop
    key = cv2.waitKey(1) & 0xFF
    if key == ord("s"):
        break

