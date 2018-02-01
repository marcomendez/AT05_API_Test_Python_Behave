import yaml

global info_yaml
generic_environment = yaml.load(open('config/environment.yml'))

def before_all(context):
    context.host = generic_environment['host']
    context.name = generic_environment['name']
    context.password = generic_environment['password']
    print("*************BEFORE ALL***********")
    print(context.host)
    print(context.name)
    print(context.password)
    print("**********************************")

def before_feature(context,feature):
    if 'try' in feature.tags:
        print("//////////// FEATURE TRY TAGS")
    if 'Test' in feature.name:
        print("________________________FEATURE TEST_____________________")


def before_scenario(context,scenario):
    if 'tag_scenario' in scenario.tags:
        print("**********_____________////////SCENARIO TAGS////////____________")
    if 'Test' in scenario.name:
        print("----------------SCENARIO TEST-------------------------------")


def before_step(context,step):
    print("STEP",step.name)
    print("STEP KEYWORD", step.keyword)
    print("STEP STATUS", step.status)



