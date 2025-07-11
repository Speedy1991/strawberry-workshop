import { useEffect } from "react"
import {useMessageSubscription, useSocialClubChangesSubscription, useSocialClubsSuspenseQuery} from "../client/generated/graphql"
import { SocialClub } from "../SocialClub"

const App = () => {
    const {data, error} = useSocialClubsSuspenseQuery()
    const {data: messageData} = useMessageSubscription()
    useSocialClubChangesSubscription()

    useEffect(() =>{
        if(!messageData?.message) return
        alert(messageData.message)
    }, [messageData])

    if (error) return <div>Error</div>
    return <div>
        {data?.socialClubs.map(club => <SocialClub key={club.id} socialClub={club} withDetails={false} />)}
    </div>
}

export default App
