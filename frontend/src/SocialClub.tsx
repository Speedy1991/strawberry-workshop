import { useNavigate } from 'react-router-dom';
import { SocialClubFragment, useCreateOrUpdateSocialClubMutation } from './client/generated/graphql';

interface SocialClubProps {
    socialClub: SocialClubFragment;
    withDetails: boolean;
}

export const SocialClub = ({ socialClub, withDetails }: SocialClubProps) => {
    const navigate = useNavigate();
    const [createOrUpdateSocialClubMutation] = useCreateOrUpdateSocialClubMutation();


    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const onSubmit = async (e: any) => {
         e.preventDefault();
        const formData = new FormData(e.target);
        // yep this is ugly but ok for our demonstration case :)
        const name = formData.get('name') as string
        const street = formData.get('street') as string
        await createOrUpdateSocialClubMutation({variables: {pk: socialClub.id, inp: {name, street}}})
    }

    return (
        <div>
            <h1>Social Club</h1>
            <p>ID: {socialClub.id}</p>
            <p>Name: {socialClub.name}</p>
            {withDetails ? (
                <>
                    <p>Street: {socialClub.street}</p>
                    <p>Zip: {socialClub.zip}</p>
                    <p>People Count: {socialClub.people.length}</p>
                    <form style={{display: 'flex', flexDirection: 'column', gap: '10px', maxWidth: '200px'}} onSubmit={onSubmit}>
                        <input name="name" type="text" placeholder='Name' />
                        <input name="street" type="text" placeholder='Street'/>
                        <button type='submit'>Speichern</button>
                    </form>
                </>
            ) : (
                <button onClick={() => navigate(`/app/${socialClub.id}/`)}>Details</button>
            )}
        </div>
    );
};
