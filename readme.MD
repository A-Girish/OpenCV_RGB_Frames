
# OpenCV RGB Frames

## About

This project demonstrates basic image processing using Python and OpenCV. A webcam is used to capture live frames, and individual colour channels are extracted by modifying the image pixel values.

## Experiments

The same camera capture program was used for all experiments. Only the image processing section of the code was changed to extract different colour channels.

1. Original Frame - Captured and saved the original camera image.
2. Red Frame - Removed Blue and Green channels.
3. Green Frame - Removed Blue and Red channels.
4. Blue Frame - Removed Green and Red channels.

## Implementation

OpenCV uses BGR format instead of RGB.

| Colour | Channel Index |
|---|---|
| Blue | 0 |
| Green | 1 |
| Red | 2 |

Individual channels were accessed using NumPy array indexing. Unwanted channels were set to zero to isolate the required colour.

## Output

The resulting images were saved separately:

- original.jpg
- red.jpg
- green.jpg
- blue.jpg

## Requirements

- Python
- OpenCV
- Webcam

Install OpenCV using:

```bash
pip install opencv-python
```

Run the program using:

```bash
python OpenCVdemo.py
```

Press `q` to close the camera window.

## Learning Outcomes

- Understanding image frames in OpenCV.
- Learning BGR colour representation.
- Accessing individual colour channels.
- Manipulating image pixel values.
- Saving processed frames separately.
