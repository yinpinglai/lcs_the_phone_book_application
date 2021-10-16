def ComplexJSONEncoder(obj):
  if hasattr(obj, 'toDict'):
    return obj.toDict()
  else:
    raise TypeError('Object of type %s with value of %s is not JSON serializeable' % (type(obj), repr(obj)))
