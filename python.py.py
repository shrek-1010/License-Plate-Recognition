import cv2
import easyocr

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'], verbose=False)

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect text (license plates) in the frame
    results = reader.readtext(frame)

    # Draw bounding boxes and display the detected text
    for (bbox, text, prob) in results:
        if prob > 0.5:  # Confidence threshold
            (top_left, top_right, bottom_right, bottom_left) = bbox
            top_left = tuple(map(int, top_left))
            bottom_right = tuple(map(int, bottom_right))

            # Draw the bounding box around the license plate
            cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)

            # Display the detected text (license plate number)
            cv2.putText(frame, text, top_left, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the frame with the bounding boxes and detected text
    cv2.imshow("License Plate Recognition", frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
