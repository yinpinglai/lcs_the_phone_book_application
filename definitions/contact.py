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

  def __eq__(self, compareable_contact) -> bool:
    '''
      Overrides the __eq__ method for comparison among contact objects

      Parameters:
        - comparable_contact: The contact object used for comparsion
    '''
    return self.name == compareable_contact.name and self.phone == compareable_contact.phone

  def toDict(self) -> dict:
    '''
      Converts the contact object into dictionary object
    '''
    return {
      'name': self.name,
      'phone': self.phone  
    }
