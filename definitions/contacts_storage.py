import os, json
from definitions.contact import Contact
from definitions.complex_json_encoder import ComplexJSONEncoder

PROJECT_PATH = os.path.dirname(os.path.abspath(__package__))

class ContactsStorage(object):
  '''
    The contacts storage object
  '''

  def __init__(self) -> None:
    '''
      Initializes the contacts storage object by constructor
    '''
    super().__init__()
    self.storage_filename = 'contacts.json'
    self.storage_filepath = os.path.join(PROJECT_PATH, 'tmp', self.storage_filename)
  
  def write_contacts_to_json(self, contacts) -> None:
    '''
      Writes contact objects to JSON file

      Parameters:
        - contacts: The list of contact object
    '''
    with open(self.storage_filepath, mode='w', encoding='utf8') as file:
      file.write(json.dumps(contacts, default=ComplexJSONEncoder, indent=2))
  
  def retrieve_contacts_from_json(self) -> list:
    '''
      Retrieves contact objects from the JSON file

      Returns:
        - contacts: The list of contact objects
    '''
    with open(self.storage_filepath, mode='r', encoding='utf8') as file:
      try:
        contacts = json.load(file)
        return [Contact(contact['name'], contact['phone']) for contact in contacts]
      except:
        return []
  