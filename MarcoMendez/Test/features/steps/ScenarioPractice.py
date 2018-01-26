from compare import expect


@given(u'I have ${balance:d} in my account')
def step_impl(context, balance):
    context.balance = int(balance)

@when(u'I choose to withdraw the fixed amount of ${withDraw:d}')
def step_impl(context, withDraw):
    context.withDraw = int(withDraw)

@then(u'I should receive ${cash:d} cash')
def step_impl(context, cash):
   print("cash")

@then(u'the balance of my account should be ${balance2:d}')
def step_impl(context, balance2):
    context.balance2 = balance2
    result = context.balance - context.withDraw
    expect(result).to_equal(context.balance2)
