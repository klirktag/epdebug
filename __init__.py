import inspect

def hello():
    print("hello world")

def methods_from_object(the_object):
    print("class name is ")
    print(the_object.__class__.__name__)
    # https://stackoverflow.com/questions/697320/how-do-i-get-the-filepath-for-a-class-in-python
    print("file is "+inspect.getfile(the_object.__class__))
    # Found here
    # https://stackoverflow.com/questions/34439/finding-what-methods-a-python-object-has
    properties_all = [property_name for property_name in dir(the_object)]

    method_list=[]
    property_list=[]

    for property_name in properties_all:
        if callable(getattr(the_object, property_name)):
            method_list.append(property_name)
        else:
            property_list.append(property_name)


    for method_name in method_list:
        print("method "+method_name)

    for property_name in property_list:
        print("property "+property_name)