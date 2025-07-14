# Exercise 2

Fix the [settings.py](https://github.com/Speedy1991/strawberry-workshop/blob/main/strawberry_workshop/settings.py#L4): `exercise2`

## Problem
At the moment we can't query anything related (e.g. _members_, _guests_, _products_) on the _SocialClubType_


## TODO

- [types.py](https://github.com/Speedy1991/strawberry-workshop/blob/main/exercise2/schema/types.py)

## Questions
```
@strawberry.field()
random_names(self, info: MyInfo) -> <???>:
    return None if True else ["Peter", "Paul", "Amy"]

@strawberry.field()    
number(self, info: MyInfo) -> <???>:
    return None if True else 1
```
Find the matching return Type
