import { ApolloClient, ApolloLink, InMemoryCache, split } from "@apollo/client"
import {get as getCookies} from 'es-cookie'
import {GraphQLWsLink} from '@apollo/client/link/subscriptions'
import {createClient} from 'graphql-ws'
import {createUploadLink} from 'apollo-upload-client'
import generatedPossibleTypes from './generated/possibleTypes'
import { getMainDefinition } from "@apollo/client/utilities"
import { StrictTypedTypePolicies } from "./generated/clientHelpers"

const createWsLink = () => {
    const wsLink = new GraphQLWsLink(createClient({
      url: `${window.location.protocol === 'http:' ? 'ws' : 'wss'}://${window.location.host}/graphqlws/`,
      connectionParams: () => {
        return {
          csrfToken: getCookies('csrftoken') ?? undefined,
          href: window.location.href,
        }
      },
      keepAlive: 5 * 1000,
      retryAttempts: Infinity,
      shouldRetry: () => true,
      retryWait: async (retries) => {
        const timeToWait = retries > 12 ? 1800 : 2 ** retries
        await new Promise((r) => setTimeout(r, timeToWait * 1000))
      },
    }))
    return wsLink
  }
  
  export const createApolloLink = () => {
    const httpLink = createUploadLink({uri: `/graphql/`}) as unknown as ApolloLink
    const wsLink = createWsLink()
  
    return split(
      ({query}) => {
        const mainDefinition = getMainDefinition(query)
        const isSubscription =
            mainDefinition.kind === 'OperationDefinition' &&
            mainDefinition.operation === 'subscription'
        return isSubscription
      },
      wsLink,
      httpLink,
    )
  }

  
const headerMiddleware = new ApolloLink((operation, forward) => {
  const headers = JSON.parse(
    JSON.stringify({
      'X-CSRFToken': getCookies('csrftoken') ?? undefined,
    }),
  )
  operation.setContext({
    headers,
  })
  return forward(operation);
})

const typePolicies: StrictTypedTypePolicies = {}

export const client = new ApolloClient({
    link: ApolloLink.from([headerMiddleware, createApolloLink()]),
    cache: new InMemoryCache({
      possibleTypes: generatedPossibleTypes.possibleTypes,
      typePolicies,
    }),
    defaultOptions: {
      watchQuery: {
        nextFetchPolicy(lastFetchPolicy) {
          if (
            lastFetchPolicy === 'cache-and-network' ||
            lastFetchPolicy === 'network-only'
          ) {
            return 'cache-first'
          }
          return lastFetchPolicy
        },
      },
    },
  })
  