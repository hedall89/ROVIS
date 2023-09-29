import numpy
import cv2

# Capturing video through webcam
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
webcam.set(cv2.CAP_PROP_FPS, 60)
ObjectOnImage = False

while (1):
    # Reading the video from the
    # webcam in image frames
    _, imageFrame = webcam.read()

    HSV_image = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
    # GUL isoleret
    lower_bound = numpy.array([20, 50, 50])
    upper_bound = numpy.array([35, 255, 255])

    mask = cv2.inRange(HSV_image, lower_bound, upper_bound)
    res = cv2.bitwise_and(imageFrame, imageFrame, mask=mask)

    # Grøn isoleret
    lower_bound_green = numpy.array([80, 101, 0])
    upper_bound_green = numpy.array([98, 255, 255])

    mask_Green = cv2.inRange(HSV_image, lower_bound_green, upper_bound_green)
    res_Green = cv2.bitwise_and(imageFrame, imageFrame, mask=mask_Green)

    # Rød isoleret
    lower_bound_red1 = numpy.array([0, 50, 50])
    upper_bound_red1 = numpy.array([7, 255, 255])
    lower_bound_red2 = numpy.array([160, 50, 50])
    upper_bound_red2 = numpy.array([180, 255, 255])

    mask_red1 = cv2.inRange(HSV_image, lower_bound_red1, upper_bound_red1)
    mask_red2 = cv2.inRange(HSV_image, lower_bound_red2, upper_bound_red2)
    mask_red = cv2.add(mask_red1, mask_red2)
    res_red = cv2.bitwise_and(imageFrame, imageFrame, mask=mask_red)

    # Blå isoleret

    lower_bound_blue = numpy.array([95, 50, 50])
    upper_bound_blue = numpy.array([130, 255, 255])

    mask_blue = cv2.inRange(HSV_image, lower_bound_blue, upper_bound_blue)
    res_blue = cv2.bitwise_and(imageFrame, imageFrame, mask=mask_blue)


    combined = cv2.add(res, res_blue)
    combined1 = cv2.add(combined, res_red)
    combined_final = cv2.add(combined1, res_Green)


    Red = cv2.countNonZero(mask_red)
    Blue = cv2.countNonZero(mask_blue)
    Green = cv2.countNonZero(mask_Green)
    Yellow = cv2.countNonZero(mask)

    if _ and not ObjectOnImage:

        if Red > 120000:
            print("Objektet er rødt: ")
            ObjectOnImage = True

        if Blue > 50000:
            print("Objektet er Blå: ")
            ObjectOnImage = True

        if Green > 30000:
            print("Objektet er Grøn: ")
            ObjectOnImage = True

        if Yellow > 30000:
            print("Objektet er Yellow ")
            ObjectOnImage = True


    if Red < 1000 and Blue < 1000 and Green < 1000 and Yellow < 1000:
        ObjectOnImage = False


    # Print line på imageframe
    font = cv2.FONT_HERSHEY_DUPLEX
    color = (255, 255, 255)  # red

    text = "ergo"
    position = (10, 10)

    cv2.putText(imageFrame, text, position, font,fontScale=0.5, color=color,thickness=1)
    cv2.putText(combined_final, text, position, font,fontScale=0.5, color=color,thickness=1)

    cv2.imshow("combined", combined_final)
    cv2.imshow("Original", imageFrame)


    if cv2.waitKey(10) & 0xFF == ord('q'):
        webcam.release()
        cv2.destroyAllWindows()
        break

