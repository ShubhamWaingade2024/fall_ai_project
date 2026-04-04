from ultralytics import YOLO
import cv2
import os
import time

class FallDetector:

    def __init__(self):

        base=os.path.dirname(__file__)

        model_path=os.path.join(base,"model","best.pt")

        self.model=YOLO(model_path)


    def detect(self,path):

        cap=cv2.VideoCapture(path)

        start=None

        confidence=0

        while cap.isOpened():

            ret,frame=cap.read()

            if not ret:
                break

            results=self.model(frame,verbose=False)

            detected=False

            for r in results:

                if r.boxes is None:
                    continue

                for box in r.boxes:

                    cls=int(box.cls[0])

                    conf=float(box.conf[0])

                    if cls==0:

                        detected=True

                        confidence=conf


            if detected:

                if start is None:

                    start=time.time()

                if time.time()-start>=10:

                    cap.release()

                    return True,confidence

            else:

                start=None


        cap.release()

        return False,confidence