def new_dec(org_func):

    def wrap_func():
        print("Statement before org_func")

        org_func()

        print("Statement after org_func")

    return wrap_func

def org_func():

    print("Original func")


wrapped_func = new_dec(org_func)

wrapped_func()