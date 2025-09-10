import cv2 as cv

def process_video(video_path):
    cap = cv.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error opening video.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert to gray
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Threshold
        _, thresh = cv.threshold(gray, 235, 255, cv.THRESH_BINARY)

        # Find contours
        contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        # Draw red rectangles
        for c in contours:
            x, y, w, h = cv.boundingRect(c)
            if w > 2 and h > 2:
                cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv.imshow("Video Flare Detection", frame)

        # Exit on 'q'
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

# Call this with your video file path
process_video("C:/Users/eamann.miled2/Downloads/multi-flares.mp4") 