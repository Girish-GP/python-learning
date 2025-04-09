from typing import List,Tuple,Dict,Union

a : int = 12
test: str = "Harry"

def sum(num1:int,num2:int) -> int:
    return num1+num2

print(a)
print(test)
print(sum(1,2))


#list of integers
numbers : List[int] = [1,2,3,4]

#Tuple of string and int
person: Tuple[str,int] = ("Alice",30)

#Dictionary with str keys and int values
scores: Dict[str,int] = {
    "Alice":30,
    "Bob":40
}

#Union type for variables that can hold multiple types
identifier: Union[str,int] = "ID123"