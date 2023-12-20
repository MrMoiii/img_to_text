# How to use

Press the `Backspace` key to initiate the image capture process.
After pressing Backspace, the program will wait for the next `two mouse clicks to define the rectangular area for image capture`. Click on two points to form a rectangle.
The program will capture the specified image and process it to extract text using Tesseract OCR.
The extracted `text will be copied to the clipboard` automatically. You can paste the text wherever needed using the standard paste command (`Ctrl+V or Cmd+V`).

# Installation

To use this program, follow the steps below:

## 1. Install Dependencies

Make sure to install all the necessary dependencies by running the following command:

```bash
pip install pynput Pillow pytesseract pyperclip
```

## 2. Configure Tesseract OCR

This program utilizes Tesseract OCR for optical character recognition. Ensure you have Tesseract OCR installed on your system. You can download it from the official site: [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).

Additionally, make sure to update the path to Tesseract OCR in the code. Modify the following line in the script:

```python
pytesseract.pytesseract.tesseract_cmd = r"Path\to\tesseract.exe"
```

Replace `"Path\to\tesseract.exe"` with the actual path to your Tesseract OCR executable.
