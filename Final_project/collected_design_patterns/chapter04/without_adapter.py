
from external import Musician, Dancer

 
class Club: 
    def __init__(self, name): 
        self.name = name 
 
    def __str__(self): 
        return f'the club {self.name}' 
 
    def organize_event(self): 
        return 'hires an artist to perform for the people' 
    
def main(): 

    objects = [Club('Jazz Cafe'), Musician('Roy Ayers'), Dancer('Shane Sparks')]
    
    for obj in objects:
        
        if hasattr(obj, 'play'):
            print(f'{obj} {obj.play()}') 
        elif hasattr(obj, 'dance'):            
            print(f'{obj} {obj.dance()}') 
        else :
            print(f'{obj} {obj.organize_event()}') 

  
if __name__ == "__main__": 
    main()