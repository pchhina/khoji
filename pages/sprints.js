import AddSprintButton from '../components/AddSprintButton.js';
import {useState} from 'react'

export default function Sprints() {
  const [sprints, setSprints] = useState([]);

    console.log(sprints)
    return (
        <div>
          <AddSprintButton />
            <h1>List of Sprints</h1>
            <ul>
                {sprints.map(item => <li key={item._id}>{item.title}{item.description}</li>)}
            </ul>
        </div>
    )
}
