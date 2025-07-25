import { gql } from '@apollo/client';
import * as Apollo from '@apollo/client';
export type Maybe<T> = T | null;
export type InputMaybe<T> = Maybe<T>;
export type Exact<T extends { [key: string]: unknown }> = { [K in keyof T]: T[K] };
export type MakeOptional<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]?: Maybe<T[SubKey]> };
export type MakeMaybe<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]: Maybe<T[SubKey]> };
export type MakeEmpty<T extends { [key: string]: unknown }, K extends keyof T> = { [_ in K]?: never };
export type Incremental<T> = T | { [P in keyof T]?: P extends ' $fragmentName' | '__typename' ? T[P] : never };
const defaultOptions = {} as const;
/** All built-in and custom scalars, mapped to their actual values */
export type Scalars = {
    ID: { input: string; output: string };
    String: { input: string; output: string };
    Boolean: { input: boolean; output: boolean };
    Int: { input: number; output: number };
    Float: { input: number; output: number };
    DateTime: { input: any; output: any };
};

export type ProductInput = {
    name: Scalars['String']['input'];
    price: Scalars['Int']['input'];
    quality: QualityEnum;
    socialClubId: Scalars['ID']['input'];
};

export enum QualityEnum {
    Bad = 'BAD',
    Good = 'GOOD',
    Ok = 'OK',
}

export type SocialClubInput = {
    name: Scalars['String']['input'];
    street: Scalars['String']['input'];
};

type Person_GuestType_Fragment = { __typename: 'GuestType'; id: string; firstName: string; lastName: string };

type Person_MemberType_Fragment = { __typename: 'MemberType'; id: string; firstName: string; lastName: string };

export type PersonFragment = Person_GuestType_Fragment | Person_MemberType_Fragment;

export type SocialClubFragment = {
    __typename: 'SocialClubType';
    id: string;
    name: string;
    street: string;
    zip: string;
    people: Array<
        | { __typename: 'GuestType'; id: string; firstName: string; lastName: string }
        | { __typename: 'MemberType'; id: string; firstName: string; lastName: string }
    >;
};

export type CreateOrUpdateSocialClubMutationVariables = Exact<{
    pk?: InputMaybe<Scalars['ID']['input']>;
    inp: SocialClubInput;
}>;

export type CreateOrUpdateSocialClubMutation = {
    __typename: 'Mutation';
    createOrUpdateSocialClub: {
        __typename: 'SocialClubType';
        id: string;
        name: string;
        street: string;
        zip: string;
        people: Array<
            | { __typename: 'GuestType'; id: string; firstName: string; lastName: string }
            | { __typename: 'MemberType'; id: string; firstName: string; lastName: string }
        >;
    };
};

export type SocialClubQueryVariables = Exact<{
    pk: Scalars['ID']['input'];
}>;

export type SocialClubQuery = {
    __typename: 'Query';
    socialClub: {
        __typename: 'SocialClubType';
        id: string;
        name: string;
        street: string;
        zip: string;
        people: Array<
            | { __typename: 'GuestType'; id: string; firstName: string; lastName: string }
            | { __typename: 'MemberType'; id: string; firstName: string; lastName: string }
        >;
    };
};

export type SocialClubsQueryVariables = Exact<{ [key: string]: never }>;

export type SocialClubsQuery = {
    __typename: 'Query';
    socialClubs: Array<{
        __typename: 'SocialClubType';
        id: string;
        name: string;
        street: string;
        zip: string;
        people: Array<
            | { __typename: 'GuestType'; id: string; firstName: string; lastName: string }
            | { __typename: 'MemberType'; id: string; firstName: string; lastName: string }
        >;
    }>;
};

export type CounterSubscriptionVariables = Exact<{ [key: string]: never }>;

export type CounterSubscription = { __typename: 'Subscription'; count: number };

export type MessageSubscriptionVariables = Exact<{ [key: string]: never }>;

export type MessageSubscription = { __typename: 'Subscription'; message: string };

export type SocialClubChangesSubscriptionVariables = Exact<{ [key: string]: never }>;

export type SocialClubChangesSubscription = {
    __typename: 'Subscription';
    socialClub: {
        __typename: 'SocialClubType';
        id: string;
        name: string;
        street: string;
        zip: string;
        people: Array<
            | { __typename: 'GuestType'; id: string; firstName: string; lastName: string }
            | { __typename: 'MemberType'; id: string; firstName: string; lastName: string }
        >;
    };
};

export const PersonFragmentDoc = gql`
    fragment Person on PersonInterface {
        id
        firstName
        lastName
    }
`;
export const SocialClubFragmentDoc = gql`
    fragment SocialClub on SocialClubType {
        id
        name
        street
        zip
        people {
            ...Person
        }
    }
    ${PersonFragmentDoc}
`;
export const CreateOrUpdateSocialClubDocument = gql`
    mutation CreateOrUpdateSocialClub($pk: ID, $inp: SocialClubInput!) {
        createOrUpdateSocialClub(pk: $pk, inp: $inp) {
            ...SocialClub
        }
    }
    ${SocialClubFragmentDoc}
`;
export type CreateOrUpdateSocialClubMutationFn = Apollo.MutationFunction<
    CreateOrUpdateSocialClubMutation,
    CreateOrUpdateSocialClubMutationVariables
>;

/**
 * __useCreateOrUpdateSocialClubMutation__
 *
 * To run a mutation, you first call `useCreateOrUpdateSocialClubMutation` within a React component and pass it any options that fit your needs.
 * When your component renders, `useCreateOrUpdateSocialClubMutation` returns a tuple that includes:
 * - A mutate function that you can call at any time to execute the mutation
 * - An object with fields that represent the current status of the mutation's execution
 *
 * @param baseOptions options that will be passed into the mutation, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options-2;
 *
 * @example
 * const [createOrUpdateSocialClubMutation, { data, loading, error }] = useCreateOrUpdateSocialClubMutation({
 *   variables: {
 *      pk: // value for 'pk'
 *      inp: // value for 'inp'
 *   },
 * });
 */
export function useCreateOrUpdateSocialClubMutation(
    baseOptions?: Apollo.MutationHookOptions<CreateOrUpdateSocialClubMutation, CreateOrUpdateSocialClubMutationVariables>
) {
    const options = { ...defaultOptions, ...baseOptions };
    return Apollo.useMutation<CreateOrUpdateSocialClubMutation, CreateOrUpdateSocialClubMutationVariables>(
        CreateOrUpdateSocialClubDocument,
        options
    );
}
export type CreateOrUpdateSocialClubMutationHookResult = ReturnType<typeof useCreateOrUpdateSocialClubMutation>;
export type CreateOrUpdateSocialClubMutationResult = Apollo.MutationResult<CreateOrUpdateSocialClubMutation>;
export type CreateOrUpdateSocialClubMutationOptions = Apollo.BaseMutationOptions<
    CreateOrUpdateSocialClubMutation,
    CreateOrUpdateSocialClubMutationVariables
>;
export const SocialClubDocument = gql`
    query SocialClub($pk: ID!) {
        socialClub(pk: $pk) {
            ...SocialClub
        }
    }
    ${SocialClubFragmentDoc}
`;

/**
 * __useSocialClubQuery__
 *
 * To run a query within a React component, call `useSocialClubQuery` and pass it any options that fit your needs.
 * When your component renders, `useSocialClubQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useSocialClubQuery({
 *   variables: {
 *      pk: // value for 'pk'
 *   },
 * });
 */
export function useSocialClubQuery(
    baseOptions: Apollo.QueryHookOptions<SocialClubQuery, SocialClubQueryVariables> &
        ({ variables: SocialClubQueryVariables; skip?: boolean } | { skip: boolean })
) {
    const options = { ...defaultOptions, ...baseOptions };
    return Apollo.useQuery<SocialClubQuery, SocialClubQueryVariables>(SocialClubDocument, options);
}
export function useSocialClubLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<SocialClubQuery, SocialClubQueryVariables>) {
    const options = { ...defaultOptions, ...baseOptions };
    return Apollo.useLazyQuery<SocialClubQuery, SocialClubQueryVariables>(SocialClubDocument, options);
}
export function useSocialClubSuspenseQuery(
    baseOptions?: Apollo.SkipToken | Apollo.SuspenseQueryHookOptions<SocialClubQuery, SocialClubQueryVariables>
) {
    const options = baseOptions === Apollo.skipToken ? baseOptions : { ...defaultOptions, ...baseOptions };
    return Apollo.useSuspenseQuery<SocialClubQuery, SocialClubQueryVariables>(SocialClubDocument, options);
}
export type SocialClubQueryHookResult = ReturnType<typeof useSocialClubQuery>;
export type SocialClubLazyQueryHookResult = ReturnType<typeof useSocialClubLazyQuery>;
export type SocialClubSuspenseQueryHookResult = ReturnType<typeof useSocialClubSuspenseQuery>;
export type SocialClubQueryResult = Apollo.QueryResult<SocialClubQuery, SocialClubQueryVariables>;
export const SocialClubsDocument = gql`
    query SocialClubs {
        socialClubs {
            ...SocialClub
        }
    }
    ${SocialClubFragmentDoc}
`;

/**
 * __useSocialClubsQuery__
 *
 * To run a query within a React component, call `useSocialClubsQuery` and pass it any options that fit your needs.
 * When your component renders, `useSocialClubsQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useSocialClubsQuery({
 *   variables: {
 *   },
 * });
 */
export function useSocialClubsQuery(baseOptions?: Apollo.QueryHookOptions<SocialClubsQuery, SocialClubsQueryVariables>) {
    const options = { ...defaultOptions, ...baseOptions };
    return Apollo.useQuery<SocialClubsQuery, SocialClubsQueryVariables>(SocialClubsDocument, options);
}
export function useSocialClubsLazyQuery(baseOptions?: Apollo.LazyQueryHookOptions<SocialClubsQuery, SocialClubsQueryVariables>) {
    const options = { ...defaultOptions, ...baseOptions };
    return Apollo.useLazyQuery<SocialClubsQuery, SocialClubsQueryVariables>(SocialClubsDocument, options);
}
export function useSocialClubsSuspenseQuery(
    baseOptions?: Apollo.SkipToken | Apollo.SuspenseQueryHookOptions<SocialClubsQuery, SocialClubsQueryVariables>
) {
    const options = baseOptions === Apollo.skipToken ? baseOptions : { ...defaultOptions, ...baseOptions };
    return Apollo.useSuspenseQuery<SocialClubsQuery, SocialClubsQueryVariables>(SocialClubsDocument, options);
}
export type SocialClubsQueryHookResult = ReturnType<typeof useSocialClubsQuery>;
export type SocialClubsLazyQueryHookResult = ReturnType<typeof useSocialClubsLazyQuery>;
export type SocialClubsSuspenseQueryHookResult = ReturnType<typeof useSocialClubsSuspenseQuery>;
export type SocialClubsQueryResult = Apollo.QueryResult<SocialClubsQuery, SocialClubsQueryVariables>;
export const CounterDocument = gql`
    subscription Counter {
        count
    }
`;

/**
 * __useCounterSubscription__
 *
 * To run a query within a React component, call `useCounterSubscription` and pass it any options that fit your needs.
 * When your component renders, `useCounterSubscription` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the subscription, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useCounterSubscription({
 *   variables: {
 *   },
 * });
 */
export function useCounterSubscription(baseOptions?: Apollo.SubscriptionHookOptions<CounterSubscription, CounterSubscriptionVariables>) {
    const options = { ...defaultOptions, ...baseOptions };
    return Apollo.useSubscription<CounterSubscription, CounterSubscriptionVariables>(CounterDocument, options);
}
export type CounterSubscriptionHookResult = ReturnType<typeof useCounterSubscription>;
export type CounterSubscriptionResult = Apollo.SubscriptionResult<CounterSubscription>;
export const MessageDocument = gql`
    subscription Message {
        message
    }
`;

/**
 * __useMessageSubscription__
 *
 * To run a query within a React component, call `useMessageSubscription` and pass it any options that fit your needs.
 * When your component renders, `useMessageSubscription` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the subscription, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useMessageSubscription({
 *   variables: {
 *   },
 * });
 */
export function useMessageSubscription(baseOptions?: Apollo.SubscriptionHookOptions<MessageSubscription, MessageSubscriptionVariables>) {
    const options = { ...defaultOptions, ...baseOptions };
    return Apollo.useSubscription<MessageSubscription, MessageSubscriptionVariables>(MessageDocument, options);
}
export type MessageSubscriptionHookResult = ReturnType<typeof useMessageSubscription>;
export type MessageSubscriptionResult = Apollo.SubscriptionResult<MessageSubscription>;
export const SocialClubChangesDocument = gql`
    subscription SocialClubChanges {
        socialClub {
            ...SocialClub
        }
    }
    ${SocialClubFragmentDoc}
`;

/**
 * __useSocialClubChangesSubscription__
 *
 * To run a query within a React component, call `useSocialClubChangesSubscription` and pass it any options that fit your needs.
 * When your component renders, `useSocialClubChangesSubscription` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the subscription, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useSocialClubChangesSubscription({
 *   variables: {
 *   },
 * });
 */
export function useSocialClubChangesSubscription(
    baseOptions?: Apollo.SubscriptionHookOptions<SocialClubChangesSubscription, SocialClubChangesSubscriptionVariables>
) {
    const options = { ...defaultOptions, ...baseOptions };
    return Apollo.useSubscription<SocialClubChangesSubscription, SocialClubChangesSubscriptionVariables>(
        SocialClubChangesDocument,
        options
    );
}
export type SocialClubChangesSubscriptionHookResult = ReturnType<typeof useSocialClubChangesSubscription>;
export type SocialClubChangesSubscriptionResult = Apollo.SubscriptionResult<SocialClubChangesSubscription>;
