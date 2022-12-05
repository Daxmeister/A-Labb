# A-Labben

#######################################################################################################################
# Skapar classes som håller koll på våra tre datastrukturer
#######################################################################################################################

class Queue_tester():

    def __init__(self):
        self.queue = []

    def enqueue(self, number):
        self.queue.append(number)

    def dequeue(self):
        return self.queue.pop(0)

class Stack_tester():

    def __init__(self):
        self.stack = []

    def push(self, number):
        self.stack.append(number)

    def pop(self):
        length = len(self.stack)
        return self.stack.pop(length)

class Priority_queue_tester():
    def __init__(self):
        self.priority_queue = []

    def enqueue(self, number):
        self.priority_queue.append(number)

    def delMax(self):
        largest = 0
        index_of_largest = 0
        for item_index in range(len(self.priority_queue)):
            if self.priority_queue[item_index] > largest:
                largest = priority_queue[item_index]
                index_of_largest = item_index
        return self.priority_queue.pop(index_of_largest)

#######################################################################################################################
# Jämförande funktion
#######################################################################################################################

class Compare_overlord():

    def __init__(self):
        self.queue = Queue_tester()
        self.stack = Stack_tester()
        self.priority_queue = Priority_queue_tester()
        self.it_could_be_queue = True
        self.it_could_be_stack = True
        self.it_could_be_priority_queue = True

    def add_number(self, number):
        self.queue.enqueue(number)
        self.stack.push(number)
        self.priority_queue.enqueue(number)

    def remove(self, sought_number):
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



def input_reader(filename):

    comparison_object = Compare_overlord
    number_of_line = int(input())
    for counter in number_of_line:
        line = input()
        line_list = line.split(' ')
        if line_list[0] == 1:
            comparison_object.add_number(line_list[1])
        else:
            comparison_object.remove(line_list[1])
    print(comparison_object.final_statement())
