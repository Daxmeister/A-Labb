# A-Labben

#######################################################################################################################
# Skapar classes som håller koll på våra tre datastrukturer
#######################################################################################################################

class Queue_tester():
    '''En klass som fungerar som en Queue.'''

    def __init__(self):
        '''Vid initiering skapas en lista som agerar grund för vår queue.'''
        self.queue = []

    def enqueue(self, number):
        '''Lägger till en integer i slutet av listan.'''
        self.queue.append(int(number))

    def dequeue(self):
        '''Tar bort det första elementet i listan och returnerar.'''
        if len(self.queue) == 0:    # Eftersom vi inte kan ta bort från en tom lista
            return -1
        else:
            return self.queue.pop(0)

class Stack_tester():
    '''Fungerar som en stack.'''

    def __init__(self):
        '''Implementationen är baserad på en lista.'''
        self.stack = []

    def push(self, number):
        '''Lägger till en integer i slutet av listan.'''
        self.stack.append(int(number))

    def pop(self):
        '''Tar bort och returnerar sista elementet i stacken.'''
        if len(self.stack) == 0:    # Eftersom vi inte kan ta bort från en tom lista
            return -1
        else:
            length = len(self.stack) - 1  # Minus ett eftersom vi börjar räkna listor från 0
            return self.stack.pop(length)   # Tar bort det sista elementet i listan.



class Priority_queue_tester():
    '''En klass för en prioritetskö.'''

    def __init__(self):
        '''Implementationen baseras på en lista.'''
        self.priority_queue = []

    def enqueue(self, number):
        '''Lägger till en integer i slutet av listan.'''
        self.priority_queue.append(int(number))

    def delMax(self):
        '''Returnerar och tar bort den högsta integern i listan.'''
        if len(self.priority_queue) == 0:    # Eftersom vi inte kan ta bort från en tom lista
            return -1
        else:
            largest = 0
            index_of_largest = 0
            for item_index in range(len(self.priority_queue)):  # Söker upp det största värdet i listan.
                if self.priority_queue[item_index] > largest:
                    largest = self.priority_queue[item_index]
                    index_of_largest = item_index
            return self.priority_queue.pop(index_of_largest)

#######################################################################################################################
# Jämförande funktion
#######################################################################################################################

class Compare_overlord():
    '''En class som hanterar alla datatyper och jämförelser och beräkningar med dessa.'''

    def __init__(self):
        '''Skapar ett object för varje datastruktur samt en variabel som håller koll på om
        vår input och output är förenbar med den datastrukturen'''
        self.queue = Queue_tester()
        self.stack = Stack_tester()
        self.priority_queue = Priority_queue_tester()
        self.it_could_be_queue = True
        self.it_could_be_stack = True
        self.it_could_be_priority_queue = True

    def add_number(self, number):
        '''Adderar siffran (som får vara i string format) till alla datastrukturer. '''
        self.queue.enqueue(number)
        self.stack.push(number)
        self.priority_queue.enqueue(number)

    def remove(self, sought_number):
        '''Tar bort en siffra från alla tre datastrukturer och jämför med den sökta siffran.
        Om det som returneras inte stämmer överens med det vi söker vet vi att det inte kan vara den datastrukturen
        och ändrar variabeln som håller koll på om det kan vara den datastrukturen till "false". '''
        queue_number = self.queue.dequeue()
        stack_number = self.stack.pop()
        priority_queue_number = self.priority_queue.delMax()

        if queue_number != sought_number:
            self.it_could_be_queue = False
        if stack_number != sought_number:
            self.it_could_be_stack = False
        if priority_queue_number != sought_number:
            self.it_could_be_priority_queue = False

    def final_statement(self):
        '''Denna funktion returnerar ett string statement på fördefinierat format baserat på vilka datastrukturer som
        fortfarande är förenliga med den input och output vi fått.'''
        if self.it_could_be_queue == False and self.it_could_be_stack == False and self.it_could_be_priority_queue == False:
            return "impossible" # Om ingen av de tre datastrukturerna är förenliga med input och output.

        # Kommande tre gäller om endast en är sann och de andra två falska.
        if self.it_could_be_queue == True and self.it_could_be_stack == False and self.it_could_be_priority_queue == False:
            return "queue"

        if self.it_could_be_queue == False and self.it_could_be_stack == True and self.it_could_be_priority_queue == False:
            return "stack"

        if self.it_could_be_queue == False and self.it_could_be_stack == False and self.it_could_be_priority_queue == True:
            return "priority queue"

        else:
            return "not sure"   # Hit kommer vi om två eller tre av datastrukturerna är förenliga med input och output.

#######################################################################################################################
# Koden som utför algoritmen
#######################################################################################################################



def run_program(filename):
    '''Funktionen som kör hela programmet.'''
    counter = 0
    with open(filename, 'r') as file:
        for line in file:
            if counter == 0:
                comparison_object = Compare_overlord()
                counter = int(line.strip())
    
            else:
                stripped_line = line.strip()
                line_list = stripped_line.split(' ')
                for index in range(len(line_list)):
                    line_list[index] = int(line_list[index])
                if line_list[0] == 1:
                    comparison_object.add_number(line_list[1])
                else:
                    comparison_object.remove(line_list[1])
                counter -= 1
                if counter == 0:    # Triggas endast sista gången
                    print(comparison_object.final_statement())



#run_program('guessthedatastructure_sample.txt')
#run_program('ismall.txt')



def run_program_input():
    counter = 0
    while True:
        long_line = input()
        line = long_line.strip()
        if counter == 0:
            comparison_object = Compare_overlord()
            counter = int(line.strip())

        else:
            stripped_line = line.strip()
            line_list = stripped_line.split(' ')
            for index in range(len(line_list)):
                line_list[index] = int(line_list[index])
            if line_list[0] == 1:
                comparison_object.add_number(line_list[1])
            else:
                comparison_object.remove(line_list[1])
            counter -= 1
            if counter == 0:  # Triggas endast sista gången
                print(comparison_object.final_statement())
#run_program('guessthedatastructure_sample.txt')




def run_program_input_medbreak():
    while True:
        counter = 0
        try:
            long_line = input()
            line = long_line.strip()
            if counter == 0:
                comparison_object = Compare_overlord()
                counter = int(line.strip())

            else:
                stripped_line = line.strip()
                line_list = stripped_line.split(' ')
                for index in range(len(line_list)):
                    line_list[index] = int(line_list[index])
                if line_list[0] == 1:
                    comparison_object.add_number(line_list[1])
                else:
                    comparison_object.remove(line_list[1])
                counter -= 1
                if counter == 0:  # Triggas endast sista gången
                    print(comparison_object.final_statement())
        except (ValueError, EOFError):
            break

#######################################################################################################################
# Koden som utför algoritmen
#######################################################################################################################
import sys


def run_program_stdin():
    '''Funktion som används för att bli godkänd vid kattis. Den kör programmet och är gjord för standard input.'''

    counter = 0 # Denna variabel håller kolla på när vi fortfarande har ett och samma input fall.

    for line in user_input: # Itererar igenom alla rader av input. Slutar läsa in vid EOF.

        if counter == 0:  # När vi kommer till ett nytt case kommer vi hit. Vi skapar nytt object och ställer countern.
            comparison_object = Compare_overlord()
            counter = int(line.strip()) # Antal rader som vi kan förvänta oss för detta enskilda case.

        else:   # Hit kommer vi för varje rad inom ett case.
            stripped_line = line.strip()
            line_list = stripped_line.split(' ')
            for index in range(len(line_list)): # För om alla siffror från string till inttegers.
                line_list[index] = int(line_list[index])

            if line_list[0] == 1:   # Om vi har ett case där vi ska lägga till något till datastrukturerna.
                comparison_object.add_number(line_list[1])
            else:   # Om vi ska ta ut något ifrån listorna och jämföra med den tänkta outputen.
                comparison_object.remove(line_list[1])
            counter -= 1    # Räknar ned antalet rader inom ett case.
            if counter == 0:  # Triggas endast sista gången, då utvärderar objektet vilka datastrukturer som är rimliga.
                print(comparison_object.final_statement())


# Här nedan utförs programmet.
user_input = sys.stdin.readlines()
run_program_stdin()

