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


## Sample

Query:
```
{
  socialClubs {
    id
    name
    street
    zip
  }
  products {
    id
    name
    price
    quality
  }
}
```

Result:

```
{
  "data": {
    "socialClubs": [
      {
        "id": "1",
        "name": "Social Club No. 0",
        "street": "Social Street 0",
        "zip": "97453"
      },
      {
        "id": "2",
        "name": "Social Club No. 1",
        "street": "Social Street 1",
        "zip": "19565"
      },
      ...
    ],
    "products": [
      {
        "id": "1",
        "name": "Marsh Wintercress",
        "price": 5,
        "quality": "BAD"
      },
      {
        "id": "2",
        "name": "Eagle Poisonberry",
        "price": 13,
        "quality": "OK"
      },
      ...
    ]
  }   
```