Certainly, here's the installation section in English for your `readme.md` file:

# Installation

To use this program, follow the steps below:

## 1. Install Dependencies

Make sure to install all the necessary dependencies by running the following command:

```bash
pip install pynput Pillow pytesseract pyperclip
```

## 2. Configure Tesseract OCR

This program utilizes Tesseract OCR for optical character recognition. Ensure you have Tesseract OCR installed on your system. You can download it from the official site: [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).

Additionally, make sure to update the path to Tesseract OCR in the code. Modify the following line in your script:

```python
pytesseract.pytesseract.tesseract_cmd = r"Path\to\tesseract.exe"
```

Replace `"Path\to\tesseract.exe"` with the actual path to your Tesseract OCR executable.
