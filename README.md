### Dynamic Random Field Tester (Selenium)

This script automatically detects all form fields on  
https://app.cloudqa.io/home/AutomationPracticeForm  
and randomly selects **3 fields** to test on each run.

It does not rely on IDs, classes, or element positions.  
Field types are detected dynamically, and the script interacts with them accordingly (text input, checkbox, radio, dropdown, date, etc.). Unsupported types are skipped safely.

---
### Run 
```
pip install requirements.txt
python main.py
```
---
### What It Does
- Scans the page for `<input>`, `<select>`, `<textarea>`
- Filters only visible/usable fields
- Picks 3 fields at random
- Detects each field's type
- Fills or clicks based on behavior
- Completes without relying on hardcoded selectors



