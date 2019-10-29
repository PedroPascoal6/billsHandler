try:
    from PIL import \
        Image
except ImportError:
    import Image
import pytesseract


# If you don't have tesseract executable in your PATH, include the following:
# pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

def convert(image_path):
    # Simple image to string
    return pytesseract.image_to_string(Image.open(image_path))

# def get_bill_value(data):