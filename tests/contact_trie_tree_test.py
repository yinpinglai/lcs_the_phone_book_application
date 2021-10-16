import sys
import os.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')

import json
import unittest
from definitions.contact import Contact
from definitions.contact_trie_tree import ContactTrieTree
from definitions.complex_json_encoder import ComplexJSONEncoder

class ContactTrieTreeTestCase(unittest.TestCase):

  def __init__(self, methodName: str = ...) -> None:
    super().__init__(methodName=methodName)

  def test_init_contact_trie_tree(self) -> None:
    contact_trie_tree = ContactTrieTree()
    self.assertEqual(contact_trie_tree.root.character, '')
    self.assertEqual(len(contact_trie_tree.root.children), 26)
    
  def test_inserting_one_contact_object(self) -> None:
    contact = Contact(name='Jack', phone='6741-0374')
    contact_trie_tree = ContactTrieTree()
    insertion_result = contact_trie_tree.insert_contact(contact=contact)
    contact_trie_tree_serialized_json = contact_trie_tree.toJSON()
    expected_result = json.dumps({
      "character": "",
      "has_ended": False,
      "children": [
        {
          "character": "a",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "b",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "c",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "d",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "e",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "f",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "g",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "h",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "i",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "j",
          "has_ended": False,
          "children": [
            {
              "character": "a",
              "has_ended": False,
              "children": [
                {
                  "character": "c",
                  "has_ended": False,
                  "children": [
                    {
                      "character": "k",
                      "has_ended": True,
                      "children": [],
                      "contact_list": [
                        {
                          "name": "Jack",
                          "phone": "6741-0374"
                        }
                      ]
                    }
                  ],
                  "contact_list": []
                }
              ],
              "contact_list": []
            }
          ],
          "contact_list": []
        },
        {
          "character": "k",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "l",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "m",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "n",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "o",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "p",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "q",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "r",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "s",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "t",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "u",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "v",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "w",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "x",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "y",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "z",
          "has_ended": False,
          "children": [],
          "contact_list": []
        }
      ],
      "contact_list": []
    })
    self.assertEqual(insertion_result, True)
    self.assertEqual(contact_trie_tree_serialized_json, expected_result)

  def test_deleting_one_contact_object(self) -> None:
    contact = Contact(name='Jack', phone='6741-0374')
    contact_trie_tree = ContactTrieTree()
    insertion_result = contact_trie_tree.insert_contact(contact=contact)
    deletion_result = contact_trie_tree.delete_contact(contact=contact)
    contact_trie_tree_serialized_json = contact_trie_tree.toJSON()
    expected_result = json.dumps({
      "character": "",
      "has_ended": False,
      "children": [
        {
          "character": "a",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "b",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "c",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "d",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "e",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "f",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "g",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "h",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "i",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "j",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "k",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "l",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "m",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "n",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "o",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "p",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "q",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "r",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "s",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "t",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "u",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "v",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "w",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "x",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "y",
          "has_ended": False,
          "children": [],
          "contact_list": []
        },
        {
          "character": "z",
          "has_ended": False,
          "children": [],
          "contact_list": []
        }
      ],
      "contact_list": []
    })
    self.assertEqual(insertion_result, True)
    self.assertEqual(deletion_result, True)
    self.assertEqual(contact_trie_tree_serialized_json, expected_result)

  def test_retriving_all_contacts(self) -> None:
    contact_trie_tree = ContactTrieTree()
    contact = Contact(name='Jack', phone='6741-0374')
    insertion_result = contact_trie_tree.insert_contact(contact=contact)
    self.assertEqual(insertion_result, True)

    contact = Contact(name='Peter', phone='5563-0312')
    insertion_result = contact_trie_tree.insert_contact(contact=contact)
    self.assertEqual(insertion_result, True)

    contact = Contact(name='Stanley', phone='3312-0324')
    insertion_result = contact_trie_tree.insert_contact(contact=contact)
    self.assertEqual(insertion_result, True)

    all_contacts = contact_trie_tree.retrieve_all_contacts()
    all_contacts_serialized_json = json.dumps(all_contacts, default=ComplexJSONEncoder)
    expected_results = json.dumps([
      { 'name': 'Jack', 'phone': '6741-0374' },
      {"name": "Peter", "phone": "5563-0312"},
      {"name": "Stanley", "phone": "3312-0324"}
    ])
    self.assertEqual(all_contacts_serialized_json, expected_results)

  def test_searching_contacts(self) -> None:
    contact_trie_tree = ContactTrieTree()
    contact = Contact(name='Jack', phone='6741-0374')
    insertion_result = contact_trie_tree.insert_contact(contact=contact)
    self.assertEqual(insertion_result, True)

    search_results = contact_trie_tree.search_contacts(keyword='Jay')
    expected_results = []
    self.assertEqual(search_results, expected_results)

    search_results = contact_trie_tree.search_contacts(keyword='Ja')
    search_results_serialized_json = json.dumps(search_results, default=ComplexJSONEncoder)

    expected_results = json.dumps([
      { 'name': 'Jack', 'phone': '6741-0374' }
    ])
    self.assertEqual(search_results_serialized_json, expected_results)
  
  def test_sorting_contacts(self) -> None:
    contact_trie_tree = ContactTrieTree()
    contact = Contact(name='Jay', phone='9999-1111')
    insertion_result = contact_trie_tree.insert_contact(contact=contact)
    self.assertEqual(insertion_result, True)

    contact = Contact(name='Jack', phone='6741-0374')
    insertion_result = contact_trie_tree.insert_contact(contact=contact)
    self.assertEqual(insertion_result, True)


    search_results = contact_trie_tree.search_contacts(keyword='Ja')
    sorted_results = contact_trie_tree.sort_contacts(contacts=search_results)
    sorted_results_serialized_json = json.dumps(sorted_results, default=ComplexJSONEncoder)

    expected_result = json.dumps([
      { 'name': 'Jack', 'phone': '6741-0374'} ,
      { 'name': 'Jay', 'phone': '9999-1111' }
    ])
    self.assertEqual(sorted_results_serialized_json, expected_result)

if __name__ == '__main__':
  unittest.main()
