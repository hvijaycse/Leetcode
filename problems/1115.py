from typing import List, Optional, Any, Dict
from threading import Thread

class FooBar:
    def __init__(self, n):
        self.n = n
        
        a = Thread(target=self.foo, args=(self.n))
        b = Thread(target=self.bar, args=(self.n))

        a.run()
        b.run()



    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            
            # printFoo() outputs "foo". Do not change or remove this line.
        	printFoo()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            
            # printBar() outputs "bar". Do not change or remove this line.
        	printBar()