import behave
behave.use_step_matcher('re')

@given(u'I put the number of habitants "(?P<value>[0-9]{1,3}(,[0-9]{3})*)"')
def step_impl(context,value):
    print(value)
