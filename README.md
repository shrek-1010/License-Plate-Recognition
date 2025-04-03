# License Plate Recognition System

This Python script implements a real-time license plate recognition system using your computer's webcam. It uses OpenCV for video capture and EasyOCR for text detection.

## Features

- Real-time video capture from webcam
- Automatic license plate detection
- Text recognition with confidence threshold
- Visual feedback with bounding boxes and detected text
- Simple exit mechanism

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- EasyOCR

## Installation

1. Install the required packages:
```bash
pip install opencv-python easyocr
```

## Usage

1. Run the script:
```bash
python chidi.py
```

2. The program will open your webcam and start detecting license plates in real-time
3. Detected license plates will be highlighted with green bounding boxes
4. The recognized text will be displayed above the bounding box
5. Press 'q' to quit the program

## Notes

- The confidence threshold is set to 0.5 (50%) to filter out false positives
- Make sure your webcam is properly connected and accessible
- Good lighting conditions will improve recognition accuracy
- The program is optimized for English text recognition

## License

This project is open source and available under the MIT License. 