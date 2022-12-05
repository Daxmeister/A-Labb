# A-Labben

#######################################################################################################################
# Skapar classes som håller koll på våra tre datastrukturer
#######################################################################################################################

class Queue_tester():

    def __init__(self):
        self.queue = []

    def enqueue(self, number):
        self.queue.append(int(number))

    def dequeue(self):
        if len(self.queue) == 0:    # Eftersom vi inte kan ta bort från en tom lista
            return -1
        else:
            return self.queue.pop(0)

class Stack_tester():

    def __init__(self):
        self.stack = []

    def push(self, number):
        self.stack.append(int(number))

    def pop(self):
        if len(self.stack) == 0:    # Eftersom vi inte kan ta bort från en tom lista
            return -1
        else:
            length = len(self.stack) - 1  # Minus ett eftersom vi börjar räkna listor från 0
            return self.stack.pop(length)



class Priority_queue_tester():
    def __init__(self):
        self.priority_queue = []

    def enqueue(self, number):
        self.priority_queue.append(int(number))

    def delMax(self):
        if len(self.priority_queue) == 0:    # Eftersom vi inte kan ta bort från en tom lista
            return -1
        else:
            largest = 0
            index_of_largest = 0
            for item_index in range(len(self.priority_queue)):
                if self.priority_queue[item_index] > largest:
                    largest = self.priority_queue[item_index]
                    index_of_largest = item_index
            return self.priority_queue.pop(index_of_largest)

#######################################################################################################################
# Jämförande funktion
#######################################################################################################################

class Compare_overlord():

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
            return "impossible"

        if self.it_could_be_queue == True and self.it_could_be_stack == False and self.it_could_be_priority_queue == False:
            return "queue"

        if self.it_could_be_queue == False and self.it_could_be_stack == True and self.it_could_be_priority_queue == False:
            return "stack"

        if self.it_could_be_queue == False and self.it_could_be_stack == False and self.it_could_be_priority_queue == True:
            return "priority queue"

        else:
            return "not sure"

#######################################################################################################################
# Annat jox
#######################################################################################################################



def run_program(filename):
    number_of_lines = 0
    first_time = True
    with open(filename, 'r') as file:
        for line in file:
            if number_of_lines == 0:
                if not first_time: # För att undvika att printa första gången
                    print(comparison_object.final_statement())  # Printar ut FÖREGÅENDE
                comparison_object = Compare_overlord()
                number_of_lines = int(line.strip())
    
            else:
                first_time = False
                stripped_line = line.strip()
                line_list = stripped_line.split(' ')
                for index in range(len(line_list)):
                    line_list[index] = int(line_list[index])
                if line_list[0] == 1:
                    comparison_object.add_number(line_list[1])
                else:
                    comparison_object.remove(line_list[1])
                number_of_lines -= 1
    print(comparison_object.final_statement())  # Printar ut den allra sista

run_program('guessthedatastructure_sample.txt')
