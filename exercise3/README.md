# Exercise 3

Fix the [settings.py](https://github.com/Speedy1991/strawberry-workshop/blob/main/strawberry_workshop/settings.py#L4): `exercise3`

## Refactor

We have a lot of boilerplate code - we can do better!! Use two approaches:
- instanciate the type via a class method `from_obj`
- use strawberry `Private` fields


## TODO

- [types.py](https://github.com/Speedy1991/strawberry-workshop/blob/main/exercise3/schema/types.py)

## Questions

- What are the advantages/differences between `from_obj` and `Private`?


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