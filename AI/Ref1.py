from typing import TypedDict, Union, Optional, Any

class Movie(TypedDict):
    name : str
    year : int

mov = Movie(name="Avengers Endgame", year=2019)

# x can be an int like 5 or a float like 3.14
def square(x: Union[int, float]) -> float:
    return x * x

# here, name can be empty
def hello_msg(name: Optional[str]) -> None:
    if name is None:
        print("Hi stranger!")
    else:
        print(f"Hello {name}!")

#here, x can be any type
def print_val(x: Any):
    print(x)

# takes in x and multiplies itself
sqr = lambda x: x*x
sqr(10)

#more example of lambda
nums = [1,2,3,4,5]
sqr2 = list(map(lambda x: x*x, nums))
