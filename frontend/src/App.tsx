import {useCounterSubscription, useSocialClubQuery} from "./client/generated/graphql"

const App = () => {
    const pk = '1'
    const {data, loading, error} = useSocialClubQuery({variables: {pk}})
    const {data: counterData} = useCounterSubscription()
    if (loading) return <div>Loading ...</div>
    if (error) return <div>Error</div>
    return <div>
        <p>Wow</p>
        {data?.socialClub.persons.map(person => <div key={person.id}>{`${person.firstName} - ${person.lastName}`}</div>)}
        <div>Counter</div>
        {counterData && <div>{counterData.count}</div>}
    </div>
}

export default App