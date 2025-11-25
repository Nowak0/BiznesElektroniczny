import random
import string
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def random_string(prefix="", n=6, digits=False):
    if digits:
        return prefix + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(n))
    else:
        return prefix + ''.join(random.choice(string.ascii_lowercase) for _ in range(n))


def short_delay(min_s=0.5, max_s=1):
    time.sleep(random.uniform(min_s, max_s))


def wait_for(driver, locator, timeout=15, condition=ec.presence_of_element_located):
    return WebDriverWait(driver, timeout).until(condition(locator))