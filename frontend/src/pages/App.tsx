import {useSocialClubsSuspenseQuery} from "../client/generated/graphql"
import { SocialClub } from "../SocialClub"

const App = () => {
    const {data, error} = useSocialClubsSuspenseQuery()
    if (error) return <div>Error</div>
    return <div>
        {data?.socialClubs.map(club => <SocialClub key={club.id} socialClub={club} />)}
    </div>
}

export default App
