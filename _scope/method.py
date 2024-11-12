def post(req, field, default=None):
  return req.POST.get(field, default)

def get(req, field, default=None):
  return req.GET.get(field, default)