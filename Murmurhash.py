import mmh3
import glob
""" Libraries:
            mmh3 - The library that has the murmurhash function in third version.
            glob - The library that helps us to check if the files are in the same directory """

""" The next class will have all the methods and properties which are required to build
    the desired system. """
class MurmurHash:
    def __init__(self, m: str, k: str) -> None:
        self.slots = m
        self.table = [0] * self._slots
        self.functions = k

    """A simple getter to the number of slots the user has inserted. """
    @property
    def slots(self) -> None:
        return self._slots

    """ The next setter makes sure that the number of slots that the user has picked is valid. """
    @slots.setter
    def slots(self, m: str) -> None:
        while not m.isdigit() or int(m) <= 0:
            print("You entered an invalid number of slots, please try again: ")
            m = input()
        self._slots = int(m)

    """ A simple getter to the number of functions the user has inserted. """
    @property
    def functions(self) -> None:
        return self._functions

    """ The next setter makes sure that the number of functions that the user has picked is valid. """
    @functions.setter
    def functions(self, k: str) -> None:
        while not k.isdigit() or not int(k):
            print("You entered an invalid number of functions, please try again: ")
            k = input()
        self._functions = int(k)

    """ Summary: 
                The next method inserts all the elements into the table.
                Once an element is inside the table, the element of the compartment turns from '0' to '1'.
        Parameters:
                Data: The data parameter is a list. In order to insert the elements from the file into the table
                    I had to put every element from the file in a different compartment inside a list. 
        Return: The method returns boolean statement as a convention is python.
                It's truly a void function. """
    def insert(self, data: list) -> bool:
        for word in data:
            for function in range(0, self._functions):
                table_index = mmh3.hash(word, function) % self._slots
                self.table[table_index] = 1
        return True

    """ Summary:
                The next method checks if all the elements in the file are also in the table.
                The checking system is according to the question requirements.
        Parameters:
                Data: The data parameter is a list. Same as above, it order to check every element in the file
                I had to put each word in a different compartment.
        Return: The method returns either words that were checked but not in the table, or a message to the user
                says that all the elements are indeed in the table. """
    def in_table(self, data: list) -> bool:
        for word in data:
            for function in range(0, self._functions):
                table_index = mmh3.hash(word, function) % self._slots
                if not self.table[table_index]:
                    print("The element: " + word + " is not in the table.\n")
                    return False
        print("All the objects which are in the file are also in the table")
        return True

""" Summary:
            The next function checks if the file even exists in the directory.
            If not, it will show a message on the screen that the file cannot be found
    Parameters:
            File1, and file2, are both strings that the user inserts.
            File1 is the file with all the elements that the user wants to insert into the table.
            File2 is the file with all the elements that the user wants to check if they are in the table.
    Return:
            The function returns a boolean statement.
            If at least one of the files cannot be found, it will send a false statement, otherwise true.  """
def files_exist(file1: str, file2: str) -> bool:
    if not glob.glob(file1) or not glob.glob(file2):
        print(f'At least one of the files doesn\'t found.')
        return False
    return True


""" The main function where everything runs from """
if __name__ == "__main__":
    """ Simply asks the user to give 'm' slots to the table, and 'k' hash function that will be used later on. """
    m = input('Please enter the number of slots in the table: ')
    k = input('Please enter the number of functions you would like to use: ')

    file1 = input('First, enter the file with the objects you\'d like to insert to the table\n')
    file2 = input('Now, enter the file with the objects that will be checked if they are in the table\n')
    """ In case one of the files do not exist and 'files_exist' is False then the program will be shut down. """
    if not files_exist(file1, file2):
        raise FileNotFoundError
    """ Two lists that help with inserting each element into the table, and checking each element if it's in the table. """
    data1, data2 = [], []
    with open(file1) as f1:
        data1 = f1.readline().split(', ')
    with open(file2) as f2:
        data2 = f2.readline().split(', ')

    murmurhash = MurmurHash(m, k)
    murmurhash.insert(data1)
    status = murmurhash.in_table(data2)
    if not status:
        exit(1)
