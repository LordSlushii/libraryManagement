import cv2

def scan_qr_from_webcam():
    cap = cv2.VideoCapture(0)

    qr_detector = cv2.QRCodeDetector()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        data, bbox, _ = qr_detector.detectAndDecode(frame)

        if data:
            return data
            break

        cv2.imshow("QR Code Scanner", frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
