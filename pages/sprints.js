import AddSprintButton from '../components/AddSprintButton.js';
import {useState, useEffect} from 'react'
import { getSession, signIn} from "next-auth/react"

export default function Sprints({data}) {
  const [loading, setLoading] = useState(true)
  useEffect(() => {
    const securePage = async() => {
      const session = await getSession()
      if(!session) {
        signIn()
      } else {
        setLoading(false)
      }
    }
    securePage()

  }, [])
  if (loading) {
    return <h2>Loading...</h2>
  }
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