import cv2

#number show.
def show(number):

    im = cv2.imread("picture/%d.jpg"%number,0)
    cv2.imshow("%d"%number,im)
    cv2.waitKey(1)
    cv2.moveWindow("%d"%number, 4340, 1000)
    #print(im)

def show_str(str):
    if str == "start":
        im = cv2.imread("picture/start.jpg")

    elif str == "end":
        im = cv2.imread("picture/end.jpg")

    elif str == "answer":
        im = cv2.imread("picture/answer.jpg")

    elif str == "break":
        im = cv2.imread("picture/break.jpg")

    elif str == "speech":
        im = cv2.imread("picture/speech.jpg")

    elif str == "nospeech":
        im = cv2.imread("picture/nospeech.jpg")

    elif str == "freedom":
        im = cv2.imread("picture/freedom.jpg")

    elif str == "question":
        im = cv2.imread("picture/question.jpg")


    cv2.imshow(str,im)
    cv2.waitKey(1)
    cv2.moveWindow(str, 4340, 1000)

def show_ans(n):
    im = cv2.imread("picture/answer_%d.jpg"%n)
    cv2.imshow("answer_%d"%n,im)
    cv2.waitKey(1)
    cv2.moveWindow("answer_%d"%n,4340,1000)
