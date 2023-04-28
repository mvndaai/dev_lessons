# Automate the page using python

We started into 3 "languages" of HTML, CSS, and Javascript. Those all work together in a browser to make a website. There are lots of languages that you can use to run things on your computer. A popular one, especially for automation, is Python

This lessing we will use python and webdriver to make your computer automatically open up a browser, navigate to your form from lesson 3 and fill in the form and click submit.


## Steps

### Setup

Open a terminal and type `python` or `python3` to see if you have python installed. If not download and install it.
https://www.python.org/downloads/

Once that is installed install the package that for automation called [`webdriver`](https://pypi.org/project/webdriver-manager/) using `pip` or `pip`
```bash
pip3 install webdriver-manager
```

To run that file you will type in your terminal

```bash
python3 automate_from.py
```

### Opening a page

Add imports to your file. These are functions you can use that you do not define yourself. We are importing `time` which lets us `sleep`, aka pause, and `selenium/webdriver` for automation.
```python
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
```

In order for your browser to be controlled by script you need an program called `ChromeDriver`. This line will automatically install that before doing anything else. There are similar functions for Firefox and other browers but Chrome is the easiest.
```py
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
```

To open a file use `driver.get` and pass the URL
```py
driver.get("http://localhost:5500/lesson_03/")
```

Let's print out the title of the page jsut so we know we are in the right place
```py
print('Title:', driver.title)
```

If you want to add a test that will fail the script if things do not match use `assert`
```py
assert(driver.title == 'Form')
```

Then `sleep` for 3 seconds so we can actually see what is happening
```py
time.sleep(3)
```

### Automation

Like how in JavaScript we used `document.querySelector` webdriver has a function called `driver.find_element`. We will use that. To interact with the page. It takes two arguments, how we are finding the element and what is being found. The how can be lots of things but we will use `By.ID`, `By.CSS_SELECTOR`, and `By.XPATH`. CSS selector is the same as our css with `#` for id and `.` for class. XPATH is another common way that you can copy from Chrome.

Start by typing something into your input using `send_keys`
```py
driver.find_element(By.ID, 'text').send_keys('Test Name')
```

Next type in a number. But because it has a default value we need to clear it first
```py
el_num = driver.find_element(By.XPATH, '//input[@name="number"]')
el_num.clear()
el_num.send_keys('7')
```
That xpath says find a tag of `input` with an attribute `name=number`. If you don't know the tag type you can use `*` for anything.


Next we can click on our radio button. Radio, checkboxes, and buttons all use the `click` function.
```py
driver.find_element(By.CSS_SELECTOR, '#radio_false').click()
```

The hardest input to interact with is our `select`. We can select by either `visible_text` or the hidden `value`. If you want to know the current value call `_el.get_attribute('value')` on the element.
```py
select = Select(driver.find_element(By.ID, 'select'))
print('original selected value:', select._el.get_attribute('value'))
select.select_by_value('C')
time.sleep(1) # wait before changing another
select.select_by_visible_text('Alpha')
time.sleep(1)
```

Lastly we will click on the submit button and wait a few seconds on to see what happened.
```py
driver.find_element(By.ID, 'form').submit()
time.sleep(10) # wait before closing
```

Try out your new python script!

## Notes
* In Chrome you can find xpath and css selectors by right clicking on something on the page then clicking `Inspect`. In the `Elements` tab of the dev tools that pops up right click again then click `Copy >` If you want xpath click `Copy XPath` and if you want a css selector click `Copy selector`.
    * In the `Elements` tab you can click `ctrl`+`f` to open find and paste the selector. That should highlight the element in your html.

* Javascript does functions using `{}` but [python just uses spacing](https://www.w3schools.com/python/python_functions.asp).
