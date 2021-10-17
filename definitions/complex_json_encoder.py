def ComplexJSONEncoder(obj):
  '''
    For serializing the complex nested object into a dictionary object.
    If object has 'toDict' method, it will be called during serialzing the content of JSON.

    Returns:
      - result: Dictionary the dictionary of the nested object.

    Raises:
      - TypeError: If the nested object has not defined the toDict method yet. 
  '''
  if hasattr(obj, 'toDict'):
    return obj.toDict()
  else:
    raise TypeError('Object of type %s with value of %s is not JSON serializeable' % (type(obj), repr(obj)))
