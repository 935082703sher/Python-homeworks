#Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days
import datetime
def age_calculator(year,month,day):
    if year<int(datetime.datetime.now().year):
        if month<int(datetime.datetime.now().month):
           if day<int(datetime.datetime.now().day):
               print( (datetime.datetime.now().year-year))
           else:
                print( (datetime.datetime.now().year-year-1))
        else:
            print( (datetime.datetime.now().year-year-1))
    else:
        print( (datetime.datetime.now().year-year-1))   
#Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.
def Days_Until_Next_Birthday(year,month,day):
    birthdate=datetime.date(year,month,day)
    today=datetime.datetime.now().date()
    t=today-birthdate
    current_year=datetime.datetime.now().year
    if month>int(datetime.datetime.now().month):
         next_birthday=datetime.date(current_year,month,day)
         remaining=next_birthday-today
         print(remaining.days)
    elif day>int(datetime.datetime.now().day):
         next_birthday=datetime.date(current_year,month,day)
         remaining=next_birthday-today
         print(remaining.days)
    else:
        next_birthday=datetime.date(current_year+1,month,day)
        remaining=next_birthday-today
        print(remaining.days)
    print(t.days,'until this i lived that days')
    print(remaining.days)
#Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.
def Meeting_Scheduler(year,month,day,hour,durationh,durationm):
    meeting=datetime.datetime(year,month,day,hour)
    end=meeting+datetime.timedelta(hours=durationh,minutes=durationm)
    print(end)
#Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.i
import pytz
import time
def timezones(place):
    local=datetime.datetime.now()
    timezone=pytz.timezone(place)
    other=datetime.datetime.now(timezone)
    print(f'local {local}, {place} { other}')
#Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time,
#  and then continuously print the time remaining until that point in regular intervals (e.g., every second).
from IPython.display import clear_output

clear_output(wait=True)
def countdown(year,month,day, hour,minute,second):
    while True:
        local=datetime.datetime.now()
        future=datetime.datetime(year,month,day,hour,minute,second)
        remaning=future-local
        time.sleep(1)
        print(remaning.seconds)
        clear_output(wait=True)
        if local==future:
            break
#Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.
import re 
def enailvalidator(email):
    
    if re.match(r'[\w+]+@[\w.%]+''$',email):
        print(email)
    else:
        print('sorry')
#Phone Number Formatter: Create a program that takes a phone number as input and formats it
#  according to a standard format. For example, convert "1234567890" to "(123) 456-7890".
def phone_number(number):
    
    if len(number)==12 and number[0:3]=='998' :
     print(f'+({number[0:3]})-{number[3:5]}-{number[5:8]}-{number[8:10]}-{number[10:]}')
    else:
        print('it doesn\'t match Uzb number lenght +(###)-##-###-##-##' )
#Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria
#  (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).
def paswordchecker(password):
    count=0

    if len(password)>=8:
        if any(char.isupper() for char in password):
            if  any(char.islower() for char in password):
                if any(char.isdigit() for char in password):
                    print('it is valid')
                else:
                    print('add at least one digit ')
            else:
                print('add at least one lowercase ')
        else:
           print('add at least one uppercase ')        
    else:
        print('the length should be greater than 8')    
# Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input
#  a word, and then search for and print all occurrences of that word in a sample text.
def word_finder(word, text):
    t=re.findall(word,text)
    print(re.findall(word,text),len(t))
#Date Extractor: Write a program that extracts dates from a 
# given text. Ask the user to input a text, and then identify and print all the dates present in the text.'''
d='''Ah, gotcha! Here's a plain text with today's date:
Generated on April 18, 2025
If you want it in another format like 18.04.2025 or with time included, let me know!'''
m=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
def dateextractor(sampletext):
    t=re.findall(r'\d{2}.\d{2}.\d{4}',sampletext)
    m=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    t1=re.findall(r'\d{2}/\d{2}/\d{4}',sampletext)  
    for i in m:
     if   re.findall(f'{i}',sampletext)and    re.findall(r"\d{2}, \d{4}",sampletext) : 
      r=(re.findall(f'{i}',sampletext)+re.findall(r"\d{2}, \d{4}",sampletext))
    print(r,t,t1)
