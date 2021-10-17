from tkinter import *
from tkinter import simpledialog, ttk
from tkinter.messagebox import askyesno, showinfo, showwarning, showerror

from definitions.contact import Contact
from definitions.contacts_storage import ContactsStorage
from definitions.contact_trie_tree import ContactTrieTree

class PhoneBookApplication():
  '''
    The Phone Book Application object structure
  '''

  def __init__(self) -> None:
    '''
      Initializes the phone book application by the constructor method
    '''
    self.root = Tk()
    self.contact_trie_tree = ContactTrieTree()
    self.contacts_tree_view = ttk.Treeview(self.root)
    self.contacts_storage = ContactsStorage()
    self.init_state()
    self.configure_root_window()
    self.build_layout()
    self.root.mainloop()

  def init_state(self) -> None:
    '''
      Initializes the internal state, retrieve and reload serialized contacts from the JSON file
    '''
    retrieved_contacts = self.contacts_storage.retrieve_contacts_from_json()
    for contact in retrieved_contacts:
      self.contact_trie_tree.insert_contact(contact)
    self.contacts = retrieved_contacts
    self.search_term = StringVar()
    self.previous_search_term = ''
    self.sorting_order = 1
    self.button_styles = {
      'highlightbackground': '#3E4149',
    }

  def configure_root_window(self) -> None:
    '''
      Configures the root window
    '''
    self.root.title('LCS - The Phone Book Application')
    self.root.geometry('560x480')

  def export_all_contacts_to_external_storage(self) -> None:
    '''
      Exports all contact objects to the external JSON file.
    '''
    if self.contacts != None:
      self.contacts = self.contact_trie_tree.sort_contacts(self.contacts)
      self.contacts_storage.write_contacts_to_json(self.contacts)

  def render_tree_view(self) -> None:
    '''
      Renders the contacts tree view layout
    '''
    keyword = self.search_term.get().strip()
    if keyword == None or keyword == '':
      contacts = self.contact_trie_tree.retrieve_all_contacts()
    else:
      contacts = self.contact_trie_tree.search_contacts(keyword=keyword)
    
    sorted_contacts = self.contact_trie_tree.sort_contacts(contacts, self.sorting_order)
    for item in self.contacts_tree_view.get_children():
      self.contacts_tree_view.delete(item)
    for contact in sorted_contacts:
      self.contacts_tree_view.insert('', 'end', values=(contact.name, contact.phone))

  def handle_add_a_contact_button_clicked(self) -> None:
    '''
      Handled when the add a contact button has been clicked event
    '''
    name = simpledialog.askstring(title='Test', prompt='What\'s the name of contact?')
    phone = simpledialog.askstring(title='Test', prompt='What\'s the phone number of contact?')
    if name == '' or phone == '':
      res = showwarning(title='Warning', message='Name or phione number is empty!')
      if res == 'ok':
        self.handle_add_a_contact_button_clicked()
      return

    new_contact = Contact(name, phone)
    try:
      has_inserted = self.contact_trie_tree.insert_contact(new_contact)
      if has_inserted:
        self.render_tree_view()
        self.contacts.append(new_contact)
        self.export_all_contacts_to_external_storage()
        showinfo(title='Success', message='{}\'s contact has been inserted successfully'.format(name))
      else:
        showerror(title='Failed', message='Unable to insert a new contact record into the application')
    except Exception as e:
      showerror(title='Internal Error', message=e)

  def handle_on_search_contacts_entry_changed(self, event):
    '''
      Handles on the search contacts by given keyword 
    '''
    value = self.search_term.get().strip()
    has_changed = self.previous_search_term != value
    if has_changed:
      self.render_tree_view()
    self.previous_search_term = value
  
  def build_layout(self) -> None:
    '''
      Builds the layout for the phone book application
    '''
    def _build_search_contacts_entry():
      search_contacts_label = Label(self.root, text='Search by name:')
      search_contacts_label.place(x=50, y=10)
      search_contacts_entry = Entry(
        self.root,
        width=30,
        bd=3,
        textvariable=self.search_term,
      )
      search_contacts_entry.bind('<KeyRelease>', self.handle_on_search_contacts_entry_changed)
      search_contacts_entry.place(x=200, y=10)

    def _build_add_a_contact_button():
      add_a_contact_button = Button(
        self.root,
        self.button_styles,
        text='Add a contact',
        command=self.handle_add_a_contact_button_clicked,
      )
      add_a_contact_button.place(x=50, y=50)

    def _build_contacts_tree_view():
      def _handle_column_clicked(idx):
        def _handle_sorting():
          if idx == 0:
            self.sorting_order = -1 if self.sorting_order == 1 else 1
            self.render_tree_view()
        return _handle_sorting
      columns = ('Name', 'Phone Number')
      self.contacts_tree_view.configure(columns=columns, show='headings')
      for idx, column in enumerate(columns):
        self.contacts_tree_view.heading(column, text=column, command=_handle_column_clicked(idx))
      self.contacts_tree_view.configure(selectmode='extended')
      self.contacts_tree_view.place(x=50, y=100)
      self.render_tree_view()

      def _handle_delete_selected_contacts():
        for selected_item in self.contacts_tree_view.selection():
          item_dict = self.contacts_tree_view.item(selected_item)
          row_values = item_dict['values']
          name = row_values[0] if len(row_values) > 0 else None
          phone = row_values[1] if len(row_values) > 1 else None
          if name == None or phone == None:
            showerror(title='Unexpected error', message='Name or phone number is empty')
          else:
            confirmation = askyesno(title='Action can not be reverted', message='Are you sure to remove {}\'s contact?'.format(name))
            if confirmation == False:
              continue
            contact = Contact(name, phone)
            try:
              self.contact_trie_tree.delete_contact(contact)
              if contact in self.contacts:
                self.contacts.remove(contact)
                self.export_all_contacts_to_external_storage()
              self.render_tree_view()
              showinfo(title='Success', message='{}\'s contact has been deleted'.format(contact.name))
            except Exception as e:
              showerror(title='Internal Error', message=e)

      delete_selected_contacts_button = Button(
        self.root,
        self.button_styles,
        text='Remove selected contacts',
        command=_handle_delete_selected_contacts
      )
      delete_selected_contacts_button.place(x=50, y=320)
    
    _build_search_contacts_entry()
    _build_add_a_contact_button()
    _build_contacts_tree_view()
