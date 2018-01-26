import TotalPriced
import ClientsList
from compare import expect


@given(u'I go to search Total priced')
def step_impl(context):
    print(" I go to search total priced  ")

@when(u'I put the "{ClientName}"')
def step_impl(context,ClientName):
    context.ClientName = str(ClientName)

@when(u'I put "{UserId}"')
def step_impl(context,UserId):
    context.UserId = str(UserId)

@then(u'I get this total priced "{TotalPrice}"')
def step_impl(context, TotalPrice):
    context.TotalPrice = str(TotalPrice)
    totalPrice = TotalPriced.getPriced(context.UserId)
    name = ClientsList.getName(context.UserId)
    expect(name).to_equal(context.ClientName)
    expect(str(totalPrice)).to_equal(str(context.TotalPrice))




@given(u'I go to search to the Client {Name}')
def step_impl(context,Name):
    ClientsList.addClient(Name)
    context.Name = Name

@when(u'I put the ClientName {searchName}')
def step_impl(context,searchName):
    context.searchName = searchName
    context.Name = ClientsList.getName(str(context.searchName))

@then(u'I should have a message that say "Exist client"')
def step_impl(context):
    expect(str(context.Name)).to_equal(str(context.searchName))
