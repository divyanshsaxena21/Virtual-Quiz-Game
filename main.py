from dbconnector import DatabaseOperations
import cv2
import cvzone
import time
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.9)

image_path = "C:\DIVYANSH\miniproject\Code-Backend\static\images\processed.jpg"

# Load the image using imread() from OpenCV
image = cv2.imread(image_path)

# mage = cv2.imread('image.jpg')
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
# print(dataAll) **Data is already in the required format
databaseConnection.closeConnetion()

# Create Object for each MCQ
mcqList = []
for q in dataAll:
    mcqList.append(MCQ(q))

qNo = 0
qTotal = len(mcqList)
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)
    if qNo<qTotal:
        mcq = mcqList[qNo]
        img, bbox = cvzone.putTextRect(img, mcq.question, [100, 100], 2, 2, offset=50, border=5)
        img, bbox1 = cvzone.putTextRect(img, mcq.choice1, [200, 300], 2, 2, offset=50, border=5)
        img, bbox2 = cvzone.putTextRect(img, mcq.choice2, [600, 300], 2, 2, offset=50, border=5)
        img, bbox3 = cvzone.putTextRect(img, mcq.choice3, [200, 500], 2, 4, offset=50, border=5)
        img, bbox4 = cvzone.putTextRect(img, mcq.choice4, [600, 500], 2, 2, offset=50, border=5)
        if hands:
            lmList = hands[0]['lmList']
            cursor = lmList[8]

            p1 = (lmList[8][0],lmList[8][1])
            p2 = (lmList[12][0], lmList[12][1])
            length, info, img = detector.findDistance(p1, p2, img)

            if length<40:
                mcq.update(cursor,[bbox1,bbox2,bbox3,bbox4])
                if mcq.userAns is not None:
                    time.sleep(0.3)
                    qNo+=1
    else:
        score = 0
        for mcq in mcqList:
            if mcq.answer == mcq.userAns:
                score+=1
        score=round((score/qTotal)*100,2)
        img, _ = cvzone.putTextRect(img,"Quiz Completed",[250,300],2,2, offset=50, border=5)
        img, _ = cvzone.putTextRect(img,f"Your Score: {score}%", [700,300], 2,2, offset=50, border=5)
        print(score)
    #Draw Progress Bar
    # barVal = 150+ (950//qTotal) + qNo
    # cv2.rectangle(img,(150,600),(barVal,650),(0,255,0),cv2.FILLED)
    # cv2.rectangle(img,(150,600),(1100,650),(255,0,255),5)

    # Set Image path
    # image = ""
    #
    # # Apply Gaussian blur to the image
    # blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
    #
    # # Display the original and blurred images using imshow
    # plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Original')
    # plt.subplot(122), plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB)), plt.title('Blurred')
    # plt.show()
    # # Display the image using imshow() from OpenCV
    # return(cv2.imshow("GAME", img))
    cv2.imshow("",img)
    cv2.waitKey(1)

