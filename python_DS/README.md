HASHING-
The hash() method returns the hash value of an object if it has one.

* Hash values are just integers which are used to compare dictionary keys during a dictionary lookup quickly.

* Internally, hash() method calls __hash__() method of an object which are set by default for any object. We'll look at this later.

* The syntax of hash() method is:
        hash(object)
		
* How hash() works for custom objects?

* hash() method internally calls __hash__() method. So, any objects can override the __hash__() for custom hash values.

* But for correct hash implementation, __hash__() should always return an integer. And, both __eq__() and __hash__() methods have to be implemented.

BINARY SEARCH-
* Search a sorted array by repeatedly dividing the search interval in half. 

* Begin with an interval covering the whole array. 

* If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. 

* Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.



