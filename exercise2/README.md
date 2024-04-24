# Exercise 2

Fix the [urls.py](https://github.com/Speedy1991/strawberry-workshop/blob/main/core/urls.py#L4): `exercise2.schema.schema`

## Problem
At the moment we can't query anything related (e.g. _members_, _guests_, _products_) on the _SocialClubType_


## TODO

- [types.py](https://github.com/Speedy1991/strawberry-workshop/blob/main/exercise2/schema/types.py)

## Questions
```
@strawberry.field
random_names(self, info: Info) -> <???>:
    return None if True else ["Peter", "Paul", "Amy"]

@strawberry.field    
number(self, info: Info) -> <???>:
    return None if True else 1
```
Find the matching return Type


## Sample

Query:
```
{
  socialClubs {
    id
    name
    members {
      id
      firstName
      lastName
    }
    guests {
      id
      firstName
      lastName
    }
    products {
      id
      name
    }
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
        "members": [
          {
            "id": "2",
            "firstName": "Mathias",
            "lastName": "Hansen"
          },
          ...
        ],
        "guests": [
          {
            "id": "17",
            "firstName": "Vilja",
            "lastName": "Bakkan"
          },
          ...
        ],
        "products": [
          {
            "id": "2",
            "name": "Eagle Poisonberry"
          },
          ...
        ],
      }
    ]
  }
}
```