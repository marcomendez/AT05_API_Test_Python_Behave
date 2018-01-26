import behave
import re

behave.use_step_matcher('re')

@given(u'I go to create a new gmail account')
def step_impl(context):
    print(" I go to Create a new Gmail account")

@given(u'I put name (?P<nameValue>[A-Za-z]*) and last (?P<lastValue>[A-Za-z]*)')
def step_impl(context,nameValue,lastValue):
    print("put name and last name")

@given(u'I put my username (?P<userName>[A-Za-z0-9_]*)')
def step_impl(context,userName):
    print("this is my username ",userName)

@given(u'I put my Password (?P<passw>[A-Za-z0-9@#/\$%*^*&+=]{8,16})')
def step_impl(context,passw):
    print("password")

@given(u'I put my the self password (?P<passw>[A-Za-z0-9@#/\$%*^&+=]{8,16})')
def step_impl(context, passw):
    print("password equals")


@given(u'I put my day brithday Day (?P<day>1[0-9]{1,31}) Month (?P<month>January|February|March|April|May|June|July|August|September|October|November|December) Year (?P<year>19[0-9]{2}|20[0-9]{2})')
def step_impl(context,day,month,year):
    print("brithday",day,month,year)

#@given(u'I choose Genler (?P<genler>[A-Za-z]*)')
@given(u'I choose Genler (?P<genler>Male|Female|Other|Rather not say)')
def step_impl(context,genler):
    print("Genler",genler)

@given(u'I put my Phono (?P<phono>\+[0-9]{0,15})')
def step_impl(context,phono):
    print(" my phono",phono)

@given(u'I put my current email address (?P<myEmail>[a-z0-9]+\@gmail.com*)')
def step_impl(context,myEmail):
    print("my my current email address",myEmail)

@given(u'I my Location (?P<myLocation>[A-Za-z]*)')
def step_impl(context,myLocation):
    print("My location",myLocation)

@when(u'I press the Button Next step')
def step_impl(context):
    print("Next step pressed")

@then(u'It should me to a page for notifacy me that my new account was created')
def step_impl(context):
    print("new a account succesful")

