import AddSprintButton from '../components/AddSprintButton.js';

export default function sprints({data}) {
    console.log(data)
    return (
        <div>
          <AddSprintButton />
            <h1>List of Sprints</h1>
            <ul>
                {data.map(item => <li key={item.id}>{item.title}</li>)}
            </ul>
        </div>
    )
}

export async function getStaticProps() {
    const res = await fetch('http:/localhost:3000/api/sprints')
    const data = await res.json();
    return {
        props: {
            data
        }
    }
}