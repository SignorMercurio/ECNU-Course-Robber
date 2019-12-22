# ECNU Course Robber

During the **3rd** round of course selection in ECNU, students are required to select their courses as fast as they can in order to have their favourite course selected. Hence I wrote this tiny script gain an advantage(in other words, cheating) over others.

## Requirements

- Python Libs:
  - `selenium`
  - `Pillow`
  - `pytesseract`
  - `retrying`
- `Tesseract-OCR`
- `chrome-driver.exe`

Note that the directory of `Tesseract-OCR` and `chrome-driver.exe` needs to be in _PATH_.

## Usage

```bash
$ python courseRobber.py
```

Then minimize your Chrome window and proceed on your work.

## Principles

Using `selenium` and `chromedriver` to control Chrome and simulate clicking, in order to bypass anti-spider mechanism. `Pillow` and `pytesseract` are utilized to bypass the weak CAPTCHA in the login page. `retrying` is involved due to slow response time of IDC.

## Notes

- You may also run this script in `phantom.js` with corresponding driver.
- The script could possibly fail due to poor network performance.
- Minimizing Chrome browser does not matter.
- This script is **NOT** the one to blame if you fail to have your favorite course selected, neither is the author of the script.

## Acknowledgement

- Inspired by [this repo](https://github.com/YULuoOo/ECNUCourseSelection)
