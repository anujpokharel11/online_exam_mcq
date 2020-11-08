

def addMCQ(form):
    mcq = form.save(commit=False)
    mcq.save()
    return mcq


