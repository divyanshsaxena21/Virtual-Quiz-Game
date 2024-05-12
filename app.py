from flask import Flask, render_template, Response
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
from dbconnector import DatabaseOperations
app = Flask(__name__)
cap = cv2.VideoCapture(0)

detector = HandDetector(detectionCon=0.9)


@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/video_feed')
def video_feed():
    return Response(frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

def frames():
    class MCQ:
        def __init__(self, data):
            self.qNo = data[0]
            self.question = data[1]
            self.choice1 = data[2]
            self.choice2 = data[3]
            self.choice3 = data[4]
            self.choice4 = data[5]
            self.answer = int(data[6])
            self.userAns = None

        def update(self, cursor, bboxs):
            for x, bbox in enumerate(bboxs):
                x1, y1, x2, y2 = bbox
                if x1 < cursor[0] < x2 and y1 < cursor[1] < y2:
                    self.userAns = x + 1
                    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), cv2.FILLED)

    databaseConnection = DatabaseOperations()
    dataAll = databaseConnection.getQuestionsFromDatabase("demo")
    databaseConnection.closeConnetion()

    mcqList = [MCQ(q) for q in dataAll]
    qNo = 0
    qTotal = len(mcqList)

    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        new_width = 1200  # Adjust this value based on your preference
        new_height = 700
        img = cv2.resize(img, (new_width, new_height))
        hands, img = detector.findHands(img, flipType=False)

        if qNo < qTotal:
            mcq = mcqList[qNo]
            # img, bbox = cvzone.putTextRect(img, mcq.qNo, [100, 100], 2, 2, offset=50, border=5)
            img, bbox = cvzone.putTextRect(img, mcq.question, [150, 100], 2, 2, offset=50, border=5)
            img, bbox1 = cvzone.putTextRect(img, mcq.choice1, [150, 300], 2, 2, offset=50, border=5)
            img, bbox2 = cvzone.putTextRect(img, mcq.choice2, [800, 300], 2, 2, offset=50, border=5)
            img, bbox3 = cvzone.putTextRect(img, mcq.choice3, [150, 600], 2, 4, offset=50, border=5)
            img, bbox4 = cvzone.putTextRect(img, mcq.choice4, [800, 600], 2, 2, offset=50, border=5)

            if hands:
                lmList = hands[0]['lmList']
                cursor = lmList[8]
                p1 = (lmList[8][0], lmList[8][1])
                p2 = (lmList[12][0], lmList[12][1])
                length, _, img = detector.findDistance(p1, p2, img)

                if length < 60:
                    mcq.update(cursor, [bbox1, bbox2, bbox3, bbox4])

        else:
            score = sum(1 for mcq in mcqList if mcq.answer == mcq.userAns)
            score = round((score / qTotal) * 100, 2)
            img, _ = cvzone.putTextRect(img, "Quiz Completed", [250, 300], 2, 2, offset=50, border=5)
            img, _ = cvzone.putTextRect(img, f"Your Score: {score}%", [700, 300], 2, 2, offset=50, border=5)
            print(score)

        ret, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        cv2.waitKey(1)
        # cap.release()



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5475)

