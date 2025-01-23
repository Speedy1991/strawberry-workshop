# Exercise 4

Fix the [settings.py](https://github.com/Speedy1991/strawberry-workshop/blob/main/strawberry_workshop/settings.py#L4): `exercise4`

## Query with Arguments and add custom fields

1) Query/Field Arguments
- Find all members in SocialClub's starting with a specified letter (optional filter)
- Find all socialClubs with at least x members (optional filter)

2) Mutation
- Finalize the create or update mutation 


3) Extra if you are really quick: Is it possible to mock/fake some Product data? Can you also mock/fake SocialClub data?

Example:
```
query SocialClubMembersStartingWithA {
  socialClubs {
    id
    name
    members(startsWith: "a") {
      id
      firstName
      lastName
    }
  }
}

query SocialClubWithAtLeast5Members {
  socialClubs(minMemberCount: 5) {
    name
    id
  }
}

mutation CreateProduct {
  createOrUpdateProduct(
    inp: {pk: 1, name: "Product 1", socialClubId: 5, price: 50, quality: GOOD}
  ) {
    id
    name
    price
    quality
    socialClub {
      id
      name
    }
  }
}
```


## TODO

- [types.py](https://github.com/Speedy1991/strawberry-workshop/blob/main/exercise4/schema/types.py)
- [query.py](https://github.com/Speedy1991/strawberry-workshop/blob/main/exercise4/schema/query.py)
- [mutation.py](https://github.com/Speedy1991/strawberry-workshop/blob/main/exercise4/schema/mutation.py)

