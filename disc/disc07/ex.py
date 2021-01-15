# Object Oriented Programming
# Programming paradim 
# Treat data s objects

# class: a template for creating objects
# instance: a single object created from a class
# instance attribute: a property of an object, specific to an instance
# class attribute: a property of an object, shared by all instances of a class
# method: an action (function) that all instances of a class may perform 
# When functions belong to a specific object, they are said to be methods. 


class Student: 
    students = 0 # this is a class attribute
    def __init__(self, name, ta): 
        self.name = name # this is an instance attribute
        self.understanding = 0
        Student.students += 1
        print("There are now", Student.students, "students")
        ta.add_student(self)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class Professor: 
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student 

    def assist(self, student):
        student.understanding += 1


class MinList: 
    """A list that can only pop smallest element. """
    def __init__(self):
        self.items = []
        self.size = 0

    def append(self, item):
        """Appends an item to the MinList
        >>> m = MinList()
        >>> m.append(4)
        >>> m.append(2)
        >>> m.size
        2
        """
        self.items.append(item)
        self.size += 1
    
    def pop(self):
        """Removes and returns the smallest item from the MinList
        >>> m = MinList()
        >>> m.append(4)
        >>> m.append(1)
        >>> m.append(5)
        >>> m.pop()
        1
        >>> m.size
        2
        """
        result = min(self.items)
        self.items.remove(result)
        self.size -= 1
        return result


class Email: 
    """Every email object has 3 instance attributes: the message, the sender name, 
    and the recipient name. 
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.message = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name 

class Server: 
    """Each Server has an instance attribute clients, which is a dictionary that associates
    client names with client objects. 
    """
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Take an email and put it in the inbox of the client it is addressed to.
        """
        client = self.clients[email.recipient_name]
        client.recieve(email)

    def register_client(self, client, client_name):
        """Take a client object and client_name and adds them to the clients instance attribute. 
        """
        self.clients[client_name] = client 


class Client: 
    """Every Client has instance attrbiutes name (which is used for addressing emails to the client), 
    server (which is used to send emails out to other clients), and inbox (a list of all emails the
    client has received).
    """
    def __init__(self, server, name): 
        self.inbox = []
        
        self.server = server
        self.name = name
        self.server.reigster_client(self, self.name)

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the given recipient client. 
        """ 
        email = Email(msg, self.name, recipient_name)
        self.server.send(email)

    def receive(self, email):
        """Take an email and add it to the inbox of this client. 
        """
        self.inbox.append(email)


# Inheritance
class Pet(): 
    def __init__(self, name, owner):
        self.is_alive = True
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    
    def talk(self):
        print(self.name)

class Dog(Pet):
    def talk(self):
        print(self.name + ' says woof!')

class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self, name, owner)
        self.lives = lives 

    def talk(self):
        """ Print out a cat's greeting.

        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        print(self.name + ' says meow!')

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is_alive' becomes
        False. If this is called after lives has reacher zero, print out that the cat
        has no more lives to lose. 
        """
        if not self.is_alive:
            print("The cat has no more lives to lose.")
        else: 
            self.lives -= 1
            if self.lives == 0:
                self.is_alive = False 

class NoisyCat(Cat):
    """A Cat that repeats things twice."""
    #def __init__(self, name, owner, lives=9)
    # this method is not necessary as no new instance attributes are defined
    # Use Cat.__init__(self, name, owner, lives=9) by default

    def talk(self):
        """Talks twice as much as a regular cat.

        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        for _ in range(2):
            Cat.talk(self)

    def __repr__(self):
        """The interpreter-readable representation of a NoisyCat

        >>> muffin = NoisyCat('Muffin', 'Catherine')
        >>> repr(muffin)
        "NoisyCat('Muffin', 'Catherine')"
        >>> muffin
        NoisyCat('Muffin', 'Catherine')
        """
        return "NoisyCat({}, {})".format(repr(self.name), repr(self.owner))
