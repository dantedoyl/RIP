from radish import given, when, then
from pizzabuilder import Cook

@given("I want to create Cook named {name: w}")
def cook_name(step, name):
    step.context.name = name

@when("I create it")
def create_cook(step):
    step.context.cook = Cook(step.context.name, None, None)

@then("I expect that his name will be {new_name: w}")
def expect_name(step, new_name):
    assert step.context.cook.name == new_name