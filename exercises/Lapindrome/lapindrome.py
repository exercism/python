class lapindrome():
    # Constructor for accepting string
    def __init__(self,string):
        self.string=string
        pass
    #Function to check  Lapindrome
    def chk_lapindrome(self):
        l=len(self.string)
        if l == 1:
            return None
        elif l%2==0:
            return self.lapin_for_even(l)
        else:
            return self.lapin_for_odd(l)
        pass
    '''
for length is even string is divided
    into two equal parts and
    then check the frequency of characters'''
    def lapin_for_even(self,length):
        l = length // 2
        #slicing the string in two equal half
        first= self.string[0 : l]
        second= self.string[l:]
        #sorted both first and second strings
        first_sorted = sorted(first)
        sec_sorted = sorted(second)
        #list to string conversion
        first = "".join(first_sorted)
        second = "".join(sec_sorted)

        if first == second:
            return True
        else:
            return False
        pass
      '''
for length is odd string is divided
    into two parts i.e. first 0 to length/2 and second length/2 + 1 to l
    then check the frequency of characters'''
    def lapin_for_odd(self,length):
        l = length // 2
        first= self.string[0 : l]
        second= self.string[l+1:]

        first_sorted = sorted(first)
        sec_sorted = sorted(second)

        first = "".join(first_sorted)
        second = "".join(sec_sorted)

        if first == second:
            return True
        else:
            return False
        pass
    
    pass
