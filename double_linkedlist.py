from emptydouble_linkedlist import EmptyDoubleLinkedListError

class DoubleLinkedList:
    
    class __Node:
        
        def __init__(self, value, /):
            
            self.value = value
            self.next = None
            self.prev = None
            
    def __init__(self, *values):
        
        self.__head = None
        self.__last = None
        self.__length = 0
        self.__start(*values)
    
    def __start(self, *values):
        
        for value in values:
            if isinstance(value, (list, tuple, set)):
                for val in value:
                    self.append(val)
            elif isinstance(value, (str, bool, int, float)):
                self.append(value)
            else:
                  raise TypeError(f'Unsupported value type {type(value).__name__}')
            
    def __repr__(self):
        
        if self.__length == 0:
            return 'Empty DoubleLinkedList'
        result = '->'.join([f'{value:^4}' for value in self])
        return result
    
    def __len__(self) -> int:
        
        return self.__length
    
    def __iter__(self):
        
        self.__current = self.__head
        return self
    
    def __next__(self):
        
        if self.__current is not None:
            value, self.__current =  self.__current.value, self.__current.next
            return value
        else:
            raise StopIteration
    
    def __getitem__(self, index):
        
        index = self.__normalize_index(index)
        if index <= self.__length // 2:
            current = self.__head
            for i in range(index):
                current =  current.next
            return current.value
        current = self.__last
        for i in range((self.__length - 1 - index)):
            current = current.prev
        return current.value
    
    def __setitem__(self, index, value):
        
        index = self.__normalize_index(index)
        if index <= self.__length // 2:
            current = self.__head
            for i in range(index):
                current = current.next
            current.value = value
            return None
        current = self.__last
        for i in range((self.__length - 1 - index)):
            current = current.prev
        current.value = value
    
    def __delitem__(self, index):
        
        index = self.__normalize_index(index)
        if index <= (self.__length // 2):
            current = self.__head
            for i in range(index):
                current = current.next
            if index == 0:
                self.__head = self.__head.next
                self.__length -= 1
                if self.__head is not None:
                    self.__head.prev = None
                    current.next, current.prev = None, None
                return None
            if current.next is not None:
                current.next.prev = current.prev
            current.prev.next = current.next
            current.next, current.prev = None, None
            self.__length -= 1
            return None
        current = self.__last
        if index == self.__length - 1:
            self.__last = self.__last.prev
            if self.__last is not None:
                self.__last.next = None
            current.next, current.prev = None, None
            self.__length -= 1
            return None
        for i in range((self.__length - 1 - index)):
            current = current.prev
        current.prev.next = current.next
        current.next.prev = current.prev
        current.next, current.prev = None, None
        self.__length -= 1
    
    def __contains__(self, item) -> bool:
        
        for value in self:
            if value == item:
                return True
        return False
    
    def __normalize_index(self, index, /) -> int:
        
        if not isinstance(index, int):
            raise ValueError('index must be of type int')
        index = (self.__length + index) if index < 0 else index
        if self.__length == 0:
            raise EmptyDoubleLinkedListError('An empty DoubleLinkedList was referenced.')
        if index >= self.__length:
            raise IndexError('reference outside the index range')
        return index
            
    def __check_length(self):
        
        if self.__length == 0:
            raise EmptyDoubleLinkedListError('Empty DoubleLinkedList')
    
    def append(self, value, /):
        
        if self.__length:
            new_node = DoubleLinkedList.__Node(value)
            new_node.prev = self.__last
            self.__last.next = new_node
            self.__last = new_node
        else:
            self.__head = DoubleLinkedList.__Node(value)
            self.__last = self.__head
        self.__length += 1
    
    def insert(self, index, value, /):
        
        if not isinstance(index, int):
            raise ValueError('index must be of type int')
        index = (self.__length + index) if index < 0 else index
        if index > self.__length:
            raise IndexError('reference outside the index range')
        new_node = DoubleLinkedList.__Node(value)
        if index == 0:
            if self.__length == 0:
                self.__head, self.__last = new_node, new_node
            else:
                new_node.next = self.__head
                self.__head.prev = new_node
                self.__head = new_node
            self.__length += 1
            return None
        if index == self.__length:
            return self.append(value)
        if index <= (self.__length // 2):
            current = self.__head
            for i in range(index):
                current = current.next
            new_node.next = current
            new_node.prev = current.prev
            current.prev.next = new_node
            current.prev = new_node
            self.__length += 1
            return None
        current = self.__last
        for i in range((self.__length - 1 - index)):
            current = current.prev
        new_node.next = current
        new_node.prev = current.prev
        current.prev.next = new_node
        current.prev = new_node
        self.__length += 1
    
    def extend(self, dlinked_list, /):
        
        if isinstance(dlinked_list, DoubleLinkedList) is False:
            raise TypeError(f'An object of type {type(dlinked_list).__name__} is not accepted, an object of type DoubleLinkedList can be inserted')
        for value in dlinked_list:
            self.append(value)
    
    def index(self, value, start=0, stop=-1, /) -> int:
        
        stop = self.__length if stop == -1 else stop
        for index, val in enumerate(self):
            if start <= index and index < stop and value == val:
                return index
        raise ValueError('No such value exists in DoubleLinkedList')
    
    def remove(self, value, /):
        
        self.__check_length()
        if self.__head.value == value:
            if self.__length == 1:
                self.__head, self.__last = None, None
            else:
                self.__head = self.__head.next
                self.__head.prev = None
            self.__length -= 1
            return None
        current = self.__head.next
        while current is not None:
            if current.value == value:
                current.prev.next = current.next
                self.__length -= 1
                if current == self.__last:
                    self.__last = current.prev
                    current.prev, current.next = None, None
                    return None
                current.prev, current.next = None, None
                return None
            current = current.next
        raise ValueError('No such value exists in DoubleLinkedList')
    
    def pop(self):
        
        self.__check_length()
        old_obj = self.__last
        if self.__length == 1:
            self.__head, self.__last = None, None
        else:
            self.__last = self.__last.prev
            self.__last.next = None
        self.__length -= 1
        return old_obj.value
    
    def clear(self):
        
        self.__head, self.__last = None, None
        self.__length = 0        