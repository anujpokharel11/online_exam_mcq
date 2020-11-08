
def addTest(form):
    test = form.save(commit=False)
    test.save()
    return test
