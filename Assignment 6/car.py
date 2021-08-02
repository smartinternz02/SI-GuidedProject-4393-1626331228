import cv2

car_classifier=cv2.CascadeClassifier("haarcascade_car.xml")


video=cv2.VideoCapture("car.avi")
frame_width = int(video.get(3))
frame_height = int(video.get(4))
out = cv2.VideoWriter('Output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

while True:
    #capture the first frame
    check,frame=video.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)

    #detect the faces from the video using detectMultiScale function
    cars=car_classifier.detectMultiScale(gray,1.3,5)
    print(cars)
    
    #drawing rectangle boundries for the detected face
    for(x,y,w,h) in cars:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        cv2.imshow('Face detection', frame)
        out.write(frame)
        #picname=datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
        #cv2.imwrite(picname+".jpg",frame)
        
    
    #waitKey(1)- for every 1 millisecond new frame will be captured
    Key=cv2.waitKey(1)
    if Key==ord('q'):
        #release the camera
        #video.release()
        #destroy all windows
        out.release()
        cv2.destroyAllWindows()
        break
