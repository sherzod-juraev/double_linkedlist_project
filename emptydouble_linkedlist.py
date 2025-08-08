class EmptyDoubleLinkedListError(Exception):
    
    def __init__(self, *args):
        
        super().__init__(*args)
        self.__notes = list(args)
    
    def __str__(self):
        return f'{' | '.join(str(note) for note in self.__notes)}'