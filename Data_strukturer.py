# Här har vi tre classes av data strukturer
class Node():

    def __init__(self, data):
        self.data = data
        self.next = None

# Denna klass är för själva kön. Den innehåller inga noder, endast två pekare (_first och _last) samt metoder
# för att utföra de metoder som uppgiftsbeskrivningen kräver.
class Queue():

    def __init__(self):
        self._first = None
        self._last = None

    # Lägg till nytt element i slutet av listan
    def enqueue(self, int):
        new_node = Node(int)        # Skapar ny nod med datan.
        if self.isEmpty():          # Om det är första elementet. Då blir den både sist och först!
            self._first = new_node
            self._last = new_node
        else:                       # Nu ska bara last pekas om. First pekar kvar på första noden.
            self._last.next = new_node      # Sista noden i listan ska peka på den "nya sista" noden.
            self._last = new_node

    # Tar bort och returnerar första elementet
    def dequeue(self):
        if self.size() == 1:
            self.old_first_element = self._first    # Skapar ny pekare som kommer ihåg vårt första element.
            self._first = self._first.next          # Kommer peka på None
            self._last = None                       # Kommer peka på None. Detta är det speciella med att ha 1 i listan.
            return self.old_first_element.data

        elif self.size() > 1:
            self.old_first_element = self._first
            self._first = self._first.next
            return self.old_first_element.data

        else:
            return None

    # Returnerar True om listan är tom.
    def isEmpty(self):
        return self._first == None

    # Returnerar hur långa linked list är.
    def size(self):
        if self._first == None:
            return 0
        else:
            self.inspected_element = self._first
            counter = 1
            while self.inspected_element.next != None:  # Denna kollar om vårt element är det sista.
                self.inspected_element = self.inspected_element.next # Vi går till nästa element i listan.
                counter += 1
            return counter

    def show_first(self):
        print(self._first.data)

    def show_last(self):
        print(self._last.data)


def Stack():
    pass

def Priority_queue():
    pass





def input_reader(filename):
    for line in filename:
        comparison_object = Compare_overlord
        number_of_lines = int(input())
        for counter in number_of_lines:
            line = input()
            line_list = line.split(' ')
            if line_list[0] == 1:
                comparison_object.add_number(line_list[1])
            else:
                comparison_object.remove(line_list[1])
        print(comparison_object.final_statement())