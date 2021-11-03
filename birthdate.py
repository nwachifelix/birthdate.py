from datetime import date
 
def myage(birthdate):
    days_in_year = 365   
    age = int((date.today() - birthdate).days / days_in_year)
    return age
         
print(f"I am {myage(date(1989, 5, 5))} years old. ")

