import cv2
#Once we import the module, we use the dot notation, “.”, to access the elements(functions) inside the module.
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#to load some predefined data on face frontals from open cv
#classifier means detector(it can classsify anuything as face)
#Cascade is the algorithm(haar casacde algorithm)
webcam = cv2.VideoCapture(0);
#webcam variable has  the video
while True:
    successful_frame_read,frame = webcam.read()
    #successful_frame_read-it is a boolean (T or F)
    #frame- contains the actual image that is currently being read from the webcam
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #show the webcam in graysacle
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #to draw a green rectangle around the face in the current frame
        #(x, y)-top left coordinates of the recatngles
        #(x + w, y + h)-bottom right coordinates of the reactangle
        #(0, 255, 0)-color of the rectangle
        #2-thickness of the rectangle
    cv2.imshow('AI TERST', frame)
    #create a window with name AI TERST and display the webcam video
    key=cv2.waitKey(1)
    #wait key will wait for a key to be pressed and then execute the program
    #u need wait key to display something without it u cant
    if key==83 or key==113:#if key pressed is Q then stop the execution(these are ASCII VALUES)
        break
## When everything done, release the capture
webcam.release()