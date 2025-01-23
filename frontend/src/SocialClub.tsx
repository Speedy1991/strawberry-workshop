import { useNavigate } from "react-router-dom"
import { SocialClubFragment } from "./client/generated/graphql"

interface SocialClubProps{
    socialClub: SocialClubFragment
}

export const SocialClub = ({socialClub}: SocialClubProps) => {
    const navigate = useNavigate()
    return <div>
        <h1>Social Club</h1>
        <p>ID: {socialClub.id}</p>
        <p>Name: {socialClub.name}</p>
        <p>Street: {socialClub.street}</p>
        <p>Zip: {socialClub.zip}</p>
        <button onClick={() => navigate(`/app/${socialClub.id}/`)}>Details</button>
    </div>
}