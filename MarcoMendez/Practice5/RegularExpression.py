import re

#validate the userName.
def userName(name):
    expre = re.compile("[a-z0-9-_]*$")
    result =str(expre.match(name))
    if result != 'None':
        print("Good username")
    else:
        print("Bad username ")

#validate a password usiing regular expressiones.
def password(password):
    expre = re.compile("[a-zA-Z0-9]{8,16}$")
    result = str(expre.match(password))
    if result != 'None':
        print("Good password")
    else:
        print("Bad password")


#validate a email using regular expression.
def email(em):
    expre=re.compile('^[\w]+@[\w-]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2,2})?$')
    result=str(expre.match(em))
    print("Good email" if result!='None' else "Bad email" )



userName("WWWWWWWWW")
userName("marco123_")

password("mmMM77884632m")
password("MM77mm")



email("anything@domain.com")
email("anything@domain.comm")
email("anything@domain.com.bo")
email("anything@domain.com.bom")