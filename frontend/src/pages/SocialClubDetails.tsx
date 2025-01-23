import { useParams } from "react-router-dom"
import { useSocialClubSuspenseQuery } from "../client/generated/graphql"
import { SocialClub } from "../SocialClub"

const SocialClubDetailsPage = () => {
    const {socialClubId} = useParams()
    if(!socialClubId) throw new Error('Programming error - missing socialClubId')
    const {data, error} = useSocialClubSuspenseQuery({variables: {pk: socialClubId}})
    if(error) throw error
    if(!data?.socialClub) return <div>Not Found</div>
    return <SocialClub socialClub={data.socialClub} />
}

export default SocialClubDetailsPage
