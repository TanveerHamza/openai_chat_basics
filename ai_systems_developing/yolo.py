from ultralytics import YOLO
import cv2

# Load YOLOv8 (nano for speed, small for accuracy)
model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(".mp4")

cv2.namedWindow("Detection System", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize for faster processing
    frame = cv2.resize(frame, (1280, 720))

    results = model(frame)
    annotated_frame = results[0].plot()

    # Counters
    people_count = 0
    car_count = 0
    bike_count = 0
    cycle_count = 0

    for box in results[0].boxes:
        cls = int(box.cls[0])

        if cls == 0:   # person
            people_count += 1
        elif cls == 1:  # bicycle
            cycle_count += 1
        elif cls == 2:  # car
            car_count += 1
        elif cls == 3:  # motorcycle
            bike_count += 1

    # Display counts
    cv2.putText(annotated_frame,
                f"People: {people_count} | Cycles: {cycle_count} | Bikes: {bike_count} | Cars: {car_count}",
                (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.resizeWindow("Detection System", 1920, 1080)
    cv2.imshow("Detection System", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()