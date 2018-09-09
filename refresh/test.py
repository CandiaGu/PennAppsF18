
import time
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")


driver.get("https://www.google.com/search?ei=ymiUW8aXFefV5gLftIxo&q=time&oq=time&gs_l=psy-ab.3..0i131i20i263i264j0i67l2j0l7.1702.1932..2090...0.0..0.235.642.0j3j1....3..0....1..gws-wiz.......0i71j35i39j0i131j0i131i20i264j0i20i264.ipZUmMGzpMc");


while(True):
    driver.refresh();
    time.sleep(5);
    print("refreshing...")

