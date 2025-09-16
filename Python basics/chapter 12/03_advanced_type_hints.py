from typing import List,Tuple,Dict,Union,Set

# List of integers
numbers: List[int] = [1,2,3,4,5]

# tuple of a string and an integer
person: Tuple[str,int] = ("Alice",30)

# Dictionary with string keys and integer values
scores: Dict[str,int] = {"Alice":90, "bob":85}

#Union type for variables that can hol multiple types
identifier: Union[int,str]= "ID123"
identifier = 12345 #also valid