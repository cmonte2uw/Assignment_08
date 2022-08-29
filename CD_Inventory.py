#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# CMontejo, 2022-Aug-27, copied file
# CMontejo, 2022-Aug-28, created CD class, updated docstrings, added code for the rest of the sections
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        __init__ (cd_id, cd_title, cd_artist): -> None
        getcd_id(): -> cd_id
        getcd_title(): -> cd_title
        getcd_artist(): -> cd_artist
        __str__(): -> None
        add_cd(lst_Inventory, cd_id, cd_title, cd_artist): -> (new CD inventory item)
        
    """
    #--Constructor--#
    def __init__(self, cd_id, cd_title, cd_artist):
        self.cd_id = cd_id
        self.cd_title= cd_title
        self.cd_artist = cd_artist

    #--Properties--#
    @property
    def getcd_id(self):
        return self.cd_id
    
    @property
    def getcd_title(self):
        return self.cd_title
    
    @property
    def getcd_artist(self):
        return self.cd_artist
    
    #--Methods--#    
    def __str__(self):
        pass

    @staticmethod
    def add_cd(lst_Inventory, cd_id, cd_title, cd_artist):
        """Adds new CD to the table
        
        Args:
            lstOfCDObjects (list of lists): 2D table to hold CD Inventory data
            strID (string): ID number for the CD
            strTitle (string): Title of the CD
            strArtist (string): Artist for the CD 
        
        Returns:
            None.
            """
        intID = int(float(cd_id))
        dicRow = {'ID': intID, 'Title': cd_title, 'Artist': cd_artist}
        lst_Inventory.append(dicRow)
        IO.show_inventory(lst_Inventory)
    
# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:
        None.

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name,lst_Inventory): -> (a list of CD objects)

    """
    @staticmethod
    def load_inventory(file_name, lst_Inventory):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            lstOfCDObjects (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        try:
            lst_Inventory.clear()  # this clears existing data and allows to load data from file
            objFile = open(file_name, 'r')
            for line in objFile:
                data = line.strip().split(',')
                dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
                lst_Inventory.append(dicRow)
            objFile.close()
        except FileNotFoundError:
            print('Existing inventory file not found.\n')
            pass

    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        """Function to manage data ingestion from a list of dictionaries to a file
    
        Reads the data from a 2D table (list of dictionaries) identified as lstTbl into a file.
    
        Args:
            file_name (string): name of file used to read the data from
            lstOfCDObjects (list of dict): 2D data structure (list of dicts) that holds the data during runtime
    
        Returns:
            None.
        """
        objFile = open(strFileName, 'w')
        for row in lstOfCDObjects:
            lstValues = list(row.values())
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()
    pass

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output
    properties:
        None.
        
    methods:
        print_menu(): -> None
        menu_choice(): -> (menu choice)
        show_inventory(lst_Inventory): -> None
        new_cd(): -> (new CD Inventory item)
    """

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] Load Inventory from File\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to File\n[x] Exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x
        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(lst_Inventory):
        """Displays current inventory table

        Args:
            lstOfCDObjects (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.
        """
        print()  # Add extra space for layout
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in lst_Inventory:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')
        print()  # Add extra space for layout
    
    @staticmethod
    def new_cd():
        """Get user input for a new CD
        
        Args:
            None.
        
        Returns:
            None.
        """
        while True: #Added error handling to force user to enter an integer for the ID
            strID = input('Enter ID: ').strip()
            try:
                intID = (int(float(strID)))
                break
            except ValueError:
                print('Please enter an integer\n')
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        CD.add_cd(lstOfCDObjects, intID, strTitle, strArtist)

# -- INTERFACE -- #
# 1. When program starts, read in the currently saved Inventory
FileIO.load_inventory(strFileName, lstOfCDObjects)

# 2. Start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

# 3. Process menu selection
    # 3.1 Process exit first
    if strChoice == 'x':
        break
        
    # 3.2 Process to load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('Type \'yes\' to continue and reload from file. Otherwise reload will be canceled\n')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.load_inventory(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # Start loop back at top
        
    # 3.3 Process to add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist and add item to the table
        IO.new_cd()
        continue  # Start loop back at top
        
    # 3.4 Process to display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # Start loop back at top
        
    # 3.5 Process to save inventory to file
    elif strChoice == 's':
        # 3.5.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.5.2 Process choice
        if strYesNo == 'y':
            # 3.5.2.1 Save data
           FileIO.save_inventory(strFileName, lstOfCDObjects)
           pass
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # Start loop back at top
        
    # 3.6 Catch-all should not be possible, as user choice gets vetted in I/O, but to be safe:
    else:
        print('General Error')

