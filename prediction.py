import cv2
from ultralytics import YOLO
import pyttsx3

# Updated dictionary of classes
classes = ['Green Light', 'Red Light', 'Speed Limit 10', 'Speed Limit 100', 'Speed Limit 110',
           'Speed Limit 120', 'Speed Limit 20', 'Speed Limit 30', 'Speed Limit 40',
           'Speed Limit 50', 'Speed Limit 60', 'Speed Limit 70', 'Speed Limit 80',
           'Speed Limit 90', 'Stop']

# Load the pre-trained YOLO model
model = YOLO("yolov8n.pt")


def predict_traffic_sign_from_frame(frame):
    results = model.predict(source=frame, imgsz=416, conf=0.5, iou=0.7)
    return results

actions = {
    "Green Light": "Proceed and continue moving.",
    "Red Light": "Stop.",
    "Speed Limit 10": "Reduce speed to 10 km/h.",
    "Speed Limit 100": "Maintain or adjust speed to 100 km/h.",
    "Speed Limit 110": "Maintain or adjust speed to 110 km/h.",
    "Speed Limit 120": "Maintain or adjust speed to 120 km/h.",
    "Speed Limit 20": "Reduce speed to 20 km/h.",
    "Speed Limit 30": "Reduce speed to 30 km/h.",
    "Speed Limit 40": "Reduce speed to 40 km/h.",
    "Speed Limit 50": "Maintain or adjust speed to 50 km/h.",
    "Speed Limit 60": "Maintain or adjust speed to 60 km/h.",
    "Speed Limit 70": "Maintain or adjust speed to 70 km/h.",
    "Speed Limit 80": "Maintain or adjust speed to 80 km/h.",
    "Speed Limit 90": "Maintain or adjust speed to 90 km/h.",
    "Stop": "Stop the vehicle completely and proceed when safe."
}

engine = pyttsx3.init() # object creation
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)   # 1 for female

def main():
    cap = cv2.VideoCapture("WhatsApp Video 2024-07-15 at 00.33.27_71f46aa9.mp4")  # Use a video file

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Get the video frame width and height
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Define the codec and create VideoWriter object
    out = cv2.VideoWriter('output_video2.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))
    labels = [""]

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        predicted_sign = predict_traffic_sign_from_frame(frame)
        for result in predicted_sign:
            boxes = result.boxes.xyxy.cpu().numpy()  # Convert to numpy array
            confs = result.boxes.conf.cpu().numpy()  # Convert to numpy array
            classes_ids = result.boxes.cls.cpu().numpy()  # Convert to numpy array
            for i, box in enumerate(boxes):
                x1, y1, x2, y2 = box.astype(int)
                conf = confs[i]
                cls = int(classes_ids[i])
                label = f"{classes[cls]} {conf:.2f}"
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 6)
                cv2.putText(frame, label, (x1, y1 - 25), cv2.FONT_HERSHEY_SIMPLEX, 1.7, (0, 255, 0), 6)
                
                if label in actions:
                    action = actions[label]
                    engine.say(f"Sign is {label}. You should {action}")
                    engine.runAndWait()

        # Write the frame into the file 'output_video.mp4'
        out.write(frame)
        
        cv2.imshow('Traffic Sign Recognition', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
