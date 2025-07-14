# Exercise 1

Fix the [settings.py](https://github.com/Speedy1991/strawberry-workshop/blob/main/strawberry_workshop/settings.py#L4): `exercise1`

## 1) Write TypeDefs
- Open [types.py](https://github.com/Speedy1991/strawberry-workshop/blob/main/exercise1/schema/types.py)
- Fill the fields with the related scalar types

## 2) Write resolvers
- [query.py](https://github.com/Speedy1991/strawberry-workshop/blob/main/exercise1/schema/query.py)

## Questions

```
@strawberry.field()
random_names(self, info: MyInfo) -> <???>:
    return ["Peter", "Paul", "Amy"]

@strawberry.field()    
number(self, info: MyInfo) -> <???>:
    return 5
```

Do you know the related field return types?
