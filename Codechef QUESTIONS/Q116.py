class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

my_list = [1, 2, 3, 4, 5]
my_iter = MyIterator(my_list)

for item in my_iter:
    print(item)


'''     "Creating iterator in python":-

In Python, you can create your own iterator using a class that implements two special methods: __iter__() and __next__().

Here's a simple example of how to create iterator in python. In this example:

We define a class MyIterator that implements the iterator protocol.
The __init__() method initializes the iterator with the data and sets the index to 0.
The __iter__() method returns the iterator itself, as required by the iterator protocol.
The __next__() method returns the next element in the data. If there are no more elements, it raises a StopIteration exception.
We instantiate MyIterator with a list and then iterate over it using a for loop. The loop automatically calls __next__() until StopIteration is raised.'''