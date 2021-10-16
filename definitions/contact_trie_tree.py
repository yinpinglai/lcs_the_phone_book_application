from definitions.contact_trie_tree_node import ContactTrieTreeNode

class ContactTrieTree(object):
  """
    The contact trie tree object
  """

  def __init__(self) -> None:
    """
      Initializes the contact trie tree object by constructor
    """
    self.root = ContactTrieTreeNode('')

    for i in range(97, 123):
      self.root.children[chr(i)] = ContactTrieTreeNode(chr(i))

  def insert_contact(self, contact) -> bool:
    '''
      Inserts the contact object into the contact trie tree

      Parameters:
        - contact: The Contact object

      Returns:
        - has_performed: The boolean flag of whether the creation has been performed or not 
    '''
    if contact.name == None or contact.name == '':
      raise ValueError('The value of the name attribute is empty')

    current_node = self.root

    for character in contact.name.lower():
      if character in current_node.children:
        current_node = current_node.children[character]
      else:
        new_contact_node = ContactTrieTreeNode(character)
        current_node.children[character] = new_contact_node
        current_node = new_contact_node

    current_node.has_ended = True
    current_node.contact_list.append(contact)
    return True

  def delete_contact(self, contact) -> bool:
    '''
      Deletes the contact object from the contact trie tree

      Parameters:
        - contact: The contact object

      Returns:
        - has_performed: The boolean flag of whether the deletion has been performed or not 
    '''
    if contact.name == None or contact.name == '':
      raise ValueError('The value of the name attribute is empty')

    def _remove_contact_trie_node(node, name, phone, idx) -> bool:
      '''
        Removes the contact trie tree node object form the contact trie tree

        Parameters:
          - children: The children nodes of the current trie tree node object
          - name: The name of the contact object
          - phone: The phone of the contact object
          - idx: The current index of the iteration

        Returns:
          - has_performed: The boolean flag of whether the deletion of the particular tire tree node object has been performed or not
      '''
      if idx == len(name):
        if node.has_ended:
          node.contact_list = list(filter(lambda c: c.phone != phone, node.contact_list))
          if len(node.contact_list) == 0:
            node.has_ended = True
            return True
        else:
          return False
      else:
        if name[idx] in node.children and _remove_contact_trie_node(node.children[name[idx]], name, phone, idx + 1):
          if len(node.children[name[idx]].children.keys()) == 0 and len(node.children[name[idx]].contact_list) == 0:
            if idx > 0:
              del node.children[name[idx]]
            return True
        else:
          return False

    current_node = self.root
    name = contact.name.lower()
    phone = contact.phone
    idx = 0
    return _remove_contact_trie_node(current_node, name, phone, idx)

  def retrieve_all_contacts(self) -> list:
    '''
      Retrieves all contacts from the contact trie tree
      
      Returns:
        - contacts: The list of all contacts
    '''

    def _find_nodes(node, prefix):
      '''
        Finds all nodes stored in the contact trie tree with the desired prefix string.

        Parameters:
          - node: Contact Trie Tree Node Object
          - prefix: The requested prefix string

        Returns:
          - results: An array of all contacts which matched with the desired prefix
      '''
      results = []
      if node.has_ended:
        results.extend(node.contact_list)

      node_children = list(node.children.values())
      for i in range(0, len(node_children)):
        child = node_children[i]
        results.extend(_find_nodes(child, prefix + node.character))
      return results
    
    results = []
    for i in range(97, 123):
      character = chr(i)
      target_node = self.root.children[character]
      results.extend(_find_nodes(target_node, character))
    return results

  def search_contacts(self, keyword) -> list:
    '''
      Searches all contacts by matching the keyword

      Parameters:
        - keyword: The search term string

      Returns:
        - results: The list of all matched with the keyword's contacts
    '''
    if keyword == None or keyword == '':
      raise ValueError('Keyword is empty')

    def _find_nodes(node, prefix):
      '''
        Finds all nodes stored in the contact trie tree with the desired prefix string.

        Parameters:
          - node: Contact Trie Tree Node Object
          - prefix: The requested prefix string

        Returns:
          - results: An array of all contacts which matched with the desired prefix
      '''
      results = []
      if node.has_ended:
        results.extend(node.contact_list)

      node_children = list(node.children.values())
      for i in range(0, len(node_children)):
        child = node_children[i]
        results.extend(_find_nodes(child, prefix + node.character))
      return results

    results = []
    current_node = self.root
    for i in range(0, len(keyword)):
      character = keyword[i].lower()
      if character in current_node.children:
        current_node = current_node.children[character]
      else:
        return results
    results = _find_nodes(current_node, keyword[:-1])
    return results

  def sort_contacts(self, contacts, order=1) -> list:
    '''
      Sorts all contacts in the list 

      Parameters:
        - contacts: A list of contacts
        - order: (optional) The order is used for determing the descending order while sorting the list. By default is 1. 1 equals ascending order. -1 equals deascending order.

      Returns:
        - sorted_results: A sorted list of contacts
    '''
    if len(contacts) == 0:
      return contacts

    def _sort_by_name(contact) -> str:
      '''
        Retrieves the sorting key of contact object
      '''
      return contact.name
    
    if order == 1:
      contacts.sort(key=_sort_by_name)
    elif order == -1:
      contacts.sort(key=_sort_by_name, reverse=True)
    return contacts

  def toDict(self) -> dict:
    '''
      Converts the root node of the contact trie tree into dictionary object
    '''
    return self.root.toDict()

  def toJSON(self) -> str:
    '''
      Converts the root node of the contact trie tree into serialized JSON content
    '''
    return self.root.toJSON()
