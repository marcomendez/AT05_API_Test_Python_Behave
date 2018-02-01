import behave
from compare import expect

behave.use_step_matcher('re')





@given(u'I put my Country (?P<value>[A-Za-z_]*)')
def step_impl(context, value):
    print("This is my country:", value,context.name)
    expect(str(context.name)).to_equal(str("marco"))


