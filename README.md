# Traffic-sign-Recognition-using-YOLOv8

This project is a Traffic Sign Recognition system powered by the YOLOv8 model, designed to detect and recognize various traffic signs in real-time from video input. The system provides both visual and auditory feedback, aiding in Advanced Driver Assistance Systems (ADAS).

Features
Real-time traffic sign recognition using YOLOv8.
Supports a wide range of traffic signs, including speed limits, stop signs, and traffic lights.
Generates voice alerts for recognized traffic signs using pyttsx3.
Annotates recognized signs on the video with bounding boxes and confidence scores.
Processes video input and outputs annotated video with predictions.
Recognizable Traffic Signs
Green Light
Red Light
Speed Limits (10–120 km/h)
Stop Sign
Getting Started
Prerequisites
Ensure you have the following installed:

Python 3.7 or higher
Required Python libraries (install using the instructions below)
Installation
Clone the repository:

#Copy
git clone https://github.com/your-username/traffic-sign-recognition.git
cd traffic-sign-recognition
Install the required dependencies:

#code
pip install -r requirements.txt
Download the YOLOv8 weights file and place it in the project directory:

#code
wget https://github.com/ultralytics/yolov8/releases/download/v8.0/yolov8n.pt

Usage
Running the Project
Place your input video in the project directory and update its name in the main() function of prediction.py:

python
Copy code
cap = cv2.VideoCapture("input_video.mp4")  # Replace with your video file
Run the script:

bash
Copy code
python prediction.py
View the results:

Annotated video will be saved as output_video.mp4.
Real-time predictions will be displayed in a window with bounding boxes and labels.
Voice Feedback
The system uses pyttsx3 to provide voice alerts for each recognized traffic sign, ensuring a user-friendly experience.

Output Example
Recognized Traffic Sign: Speed Limit 50
Bounding Box: Drawn on the video.
Voice Feedback: "Sign is Speed Limit 50. You should Maintain or adjust speed to 50 km/h."
Customization
Modify classes in prediction.py to add/remove traffic sign classes.
Update actions to customize voice alerts for different signs.
Acknowledgments
Ultralytics YOLOv8: https://github.com/ultralytics/ultralytics
pyttsx3: Python Text-to-Speech library for auditory feedback.
