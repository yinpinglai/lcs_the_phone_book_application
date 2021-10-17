import json
from definitions.complex_json_encoder import ComplexJSONEncoder

class ContactTrieTreeNode:
  """
    The trie tree node of contact object structure
  """

  def __init__(self, character) -> None:
    """
      Initialize the contact trie tree object by the constructor
    """
    self.character = character
    self.has_ended = False
    self.children = {}
    self.contact_list = []
  
  def __str__(self) -> str:
    """
      Overrides the __str__ method of the contact trie tree node object
    """
    return f'''
      ContactTreeNode: (
        character: {self.character},
        has_ended: {self.has_ended},
        children: {self.children.keys()},
        contact_list: {self.contact_list},
      )
    '''

  def toDict(self) -> dict:
    '''
      Converts the contact trie tree node object into dictionray object
    '''
    return {
      'character': self.character,
      'has_ended': self.has_ended,
      'children': list(map(lambda n: n.toDict(), self.children.values())),
      'contact_list': self.contact_list,
    }

  def toJSON(self) -> str:
    '''
      Converts the contact trie tree node object into serialized JSON content
    '''
    return json.dumps({
      'character': self.character,
      'has_ended': self.has_ended,
      'children': list(map(lambda n: n.toDict(), self.children.values())),
      'contact_list': self.contact_list,
    }, default=ComplexJSONEncoder)
