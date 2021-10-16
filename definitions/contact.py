class Contact:
  """
    The contact object structure
  """

  def __init__(self, name, phone) -> None:
    """
      Initialize the contact object by constructor
    """
    self.name = name
    self.phone = phone

  def __str__(self) -> str:
    '''
      Overrides the __str__ method for the contact object
    '''
    return f'''
      Contact: (
        name: {self.name},
        phone: {self.phone},
      )
    '''
  
  def toDict(self) -> dict:
    '''
      Converts the contact object into dictionary object
    '''
    return {
      'name': self.name,
      'phone': self.phone  
    }
