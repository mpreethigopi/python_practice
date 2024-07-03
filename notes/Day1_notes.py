"""
Data types:
Basic:
    String - str " "
    Integer - int
    float - decimals
    Boolean - bool -> True, False - case sentivite
    Complex - i+j whatever in this format considered as complex numbers
    i - imaginary - wont work in python, so it only consider real parts
    j - Real parts
    

Sequence
    List - []
    l=[1,2.5,"heelo",3j. True]
    tuple - ()    
    t=(1,2.5,"heelo",3j. True)
    Python by default consider as a tuple if the variable has multiple values decalred
    without brackets.
    eg:
    T= 1,2.4,"hello", 3j, True

    set - {}
    s=[1,2.5,"heelo",3j. True]


Mapping 
    Dictionary {Key:values}
    D={1:"q",2:34.3,3:5,4:False}
    all data types can be used as key and value expect boolean,it can be used only as value not as key


cmd:
    Single line cmd  - #
    Multi line cmd - """  """ shift+"

    Inline cmd - print("hello") #stng


Variables:
    variable_name=values

Variable name creation rules:
    1. Starts with upper/lower case
    2. Doesn't start with numbers but can be used in middle and end
    3. Special charaters not allowed (_ excluding) eg:credo_systemz
    4. Underscroe not in the begining (eg:   _san)
    5. Spaces are not allowed


type() - to find which datatype the variables are
    eg:
    a="hello"
    print("Value of A:", a)
    print("Type of A:" type(a))


Multiple Variable assignment:
    a=b=c=d = "This is my assignment"
    = means assigning single value to multiple variable

    a,b,c,d="a",2,3j,True
    , means assigning single value to multiple variable, seperated by comma
    Print(a,b,c,d)

    a,b,c,d="a"
    will throw error as variable declared is not matching with values
    4 variables are declared but there is only one variable

    P,q,r,s = "a",2,3j,True,45,"er"
    in this case there are multiple values but there is only 4 variables are declared
    
    
    string,tuple - immutable
    #immutable means - no edit, delete, add, modify, open
    list - mutable 
    mutiable means - edit, delete, add, modify, open

    
"""