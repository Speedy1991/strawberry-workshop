import { lazy, StrictMode, Suspense } from 'react'
import { createRoot } from 'react-dom/client'
import { ApolloProvider } from '@apollo/client'
import { client } from './client/client.ts'
import {RouteObject, RouterProvider, createBrowserRouter} from 'react-router-dom'

const AppPage = lazy(() => import('./pages/App'))
const SocialClubDetailsPage = lazy(() => import('./pages/SocialClubDetails'))

const Loading = () => {
  return <div>Loading</div>
}

const routes: RouteObject[] = [{
  path: '/app/',
  element: <Suspense fallback={<Loading />}>
    <AppPage />
  </Suspense>,
  errorElement: <div>Error</div>
}, {
  path: '/app/:socialClubId/',
  element: <Suspense fallback={<Loading />}>
    <SocialClubDetailsPage />
  </Suspense>,
  errorElement: <div>Error</div>
}]

createRoot(document.getElementById('root')!).render(
  <StrictMode>
      <ApolloProvider client={client}>
        <RouterProvider router={createBrowserRouter(routes)} />
      </ApolloProvider>
  </StrictMode>,
)
