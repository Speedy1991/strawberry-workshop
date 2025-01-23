import { FieldPolicy, FieldReadFunction, TypePolicies, TypePolicy } from '@apollo/client/cache';
export type GuestTypeKeySpecifier = ('firstName' | 'id' | 'lastName' | 'rating' | 'socialClub' | GuestTypeKeySpecifier)[];
export type GuestTypeFieldPolicy = {
    firstName?: FieldPolicy<any> | FieldReadFunction<any>;
    id?: FieldPolicy<any> | FieldReadFunction<any>;
    lastName?: FieldPolicy<any> | FieldReadFunction<any>;
    rating?: FieldPolicy<any> | FieldReadFunction<any>;
    socialClub?: FieldPolicy<any> | FieldReadFunction<any>;
};
export type MemberTypeKeySpecifier = ('age' | 'firstName' | 'id' | 'lastName' | 'socialClub' | MemberTypeKeySpecifier)[];
export type MemberTypeFieldPolicy = {
    age?: FieldPolicy<any> | FieldReadFunction<any>;
    firstName?: FieldPolicy<any> | FieldReadFunction<any>;
    id?: FieldPolicy<any> | FieldReadFunction<any>;
    lastName?: FieldPolicy<any> | FieldReadFunction<any>;
    socialClub?: FieldPolicy<any> | FieldReadFunction<any>;
};
export type MutationKeySpecifier = ('createOrUpdateProduct' | MutationKeySpecifier)[];
export type MutationFieldPolicy = {
    createOrUpdateProduct?: FieldPolicy<any> | FieldReadFunction<any>;
};
export type PersonInterfaceKeySpecifier = ('firstName' | 'id' | 'lastName' | 'socialClub' | PersonInterfaceKeySpecifier)[];
export type PersonInterfaceFieldPolicy = {
    firstName?: FieldPolicy<any> | FieldReadFunction<any>;
    id?: FieldPolicy<any> | FieldReadFunction<any>;
    lastName?: FieldPolicy<any> | FieldReadFunction<any>;
    socialClub?: FieldPolicy<any> | FieldReadFunction<any>;
};
export type ProductTypeKeySpecifier = ('id' | 'name' | 'price' | 'quality' | 'socialClub' | ProductTypeKeySpecifier)[];
export type ProductTypeFieldPolicy = {
    id?: FieldPolicy<any> | FieldReadFunction<any>;
    name?: FieldPolicy<any> | FieldReadFunction<any>;
    price?: FieldPolicy<any> | FieldReadFunction<any>;
    quality?: FieldPolicy<any> | FieldReadFunction<any>;
    socialClub?: FieldPolicy<any> | FieldReadFunction<any>;
};
export type QueryKeySpecifier = ('currentDateTime' | 'products' | 'socialClub' | 'socialClubs' | QueryKeySpecifier)[];
export type QueryFieldPolicy = {
    currentDateTime?: FieldPolicy<any> | FieldReadFunction<any>;
    products?: FieldPolicy<any> | FieldReadFunction<any>;
    socialClub?: FieldPolicy<any> | FieldReadFunction<any>;
    socialClubs?: FieldPolicy<any> | FieldReadFunction<any>;
};
export type SocialClubTypeKeySpecifier = ('id' | 'name' | 'persons' | 'products' | 'street' | 'zip' | SocialClubTypeKeySpecifier)[];
export type SocialClubTypeFieldPolicy = {
    id?: FieldPolicy<any> | FieldReadFunction<any>;
    name?: FieldPolicy<any> | FieldReadFunction<any>;
    persons?: FieldPolicy<any> | FieldReadFunction<any>;
    products?: FieldPolicy<any> | FieldReadFunction<any>;
    street?: FieldPolicy<any> | FieldReadFunction<any>;
    zip?: FieldPolicy<any> | FieldReadFunction<any>;
};
export type SubscriptionKeySpecifier = ('count' | 'currentTime' | 'message' | 'socialClub' | SubscriptionKeySpecifier)[];
export type SubscriptionFieldPolicy = {
    count?: FieldPolicy<any> | FieldReadFunction<any>;
    currentTime?: FieldPolicy<any> | FieldReadFunction<any>;
    message?: FieldPolicy<any> | FieldReadFunction<any>;
    socialClub?: FieldPolicy<any> | FieldReadFunction<any>;
};
export type StrictTypedTypePolicies = {
    GuestType?: Omit<TypePolicy, 'fields' | 'keyFields'> & {
        keyFields?: false | GuestTypeKeySpecifier | (() => undefined | GuestTypeKeySpecifier);
        fields?: GuestTypeFieldPolicy;
    };
    MemberType?: Omit<TypePolicy, 'fields' | 'keyFields'> & {
        keyFields?: false | MemberTypeKeySpecifier | (() => undefined | MemberTypeKeySpecifier);
        fields?: MemberTypeFieldPolicy;
    };
    Mutation?: Omit<TypePolicy, 'fields' | 'keyFields'> & {
        keyFields?: false | MutationKeySpecifier | (() => undefined | MutationKeySpecifier);
        fields?: MutationFieldPolicy;
    };
    PersonInterface?: Omit<TypePolicy, 'fields' | 'keyFields'> & {
        keyFields?: false | PersonInterfaceKeySpecifier | (() => undefined | PersonInterfaceKeySpecifier);
        fields?: PersonInterfaceFieldPolicy;
    };
    ProductType?: Omit<TypePolicy, 'fields' | 'keyFields'> & {
        keyFields?: false | ProductTypeKeySpecifier | (() => undefined | ProductTypeKeySpecifier);
        fields?: ProductTypeFieldPolicy;
    };
    Query?: Omit<TypePolicy, 'fields' | 'keyFields'> & {
        keyFields?: false | QueryKeySpecifier | (() => undefined | QueryKeySpecifier);
        fields?: QueryFieldPolicy;
    };
    SocialClubType?: Omit<TypePolicy, 'fields' | 'keyFields'> & {
        keyFields?: false | SocialClubTypeKeySpecifier | (() => undefined | SocialClubTypeKeySpecifier);
        fields?: SocialClubTypeFieldPolicy;
    };
    Subscription?: Omit<TypePolicy, 'fields' | 'keyFields'> & {
        keyFields?: false | SubscriptionKeySpecifier | (() => undefined | SubscriptionKeySpecifier);
        fields?: SubscriptionFieldPolicy;
    };
};
export type TypedTypePolicies = StrictTypedTypePolicies & TypePolicies;
