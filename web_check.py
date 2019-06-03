from urllib import request
import time
import re
import os; 
from bs4 import BeautifulSoup,Tag,CData;
from webbot import Browser

while True:
    web = Browser()
    web.go_to("https://my.unsw.edu.au/active/studentClassEnrol/courses.xml")
    web.click('Sign on')
    web.type('z5151465' , into='USER ID')
    web.type("Sword450869241_" , into='Password' , id='passwordFieldId')
    web.click('Agree and sign on')
    web.click('Sign on')
    web.click('My Student Profile')
    web.click('Update Your Enrolment')
    web.click('Update Enrolment')
    web.click('Term 2 2019')
    content = web.get_page_source()
    if "Course GSOE9340 is full." in content:
        os.system('say "WOW WOW WOW."'); 
    web.quit()
    time.sleep(5)