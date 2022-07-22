import { useState } from 'react'
import { useRouter } from 'next/router';
import styles from '../styles/UIKit.module.css'

export default function AddSprintForm(props) {
  const [id, setId] = useState("");
  const [title, setTitle] = useState("");
  const [status, setStatus] = useState("");
  const [goalId, setGoalId] = useState("");
  const [description, setDescription] = useState("");

  const router = useRouter();

  async function handleFormSubmit(event) {
    event.preventDefault();
    const formInputs = {id, title, status, goalId, description};
    const response = await fetch('/api/sprints', {
      method: 'POST',
      body: JSON.stringify({formInputs}),
      headers: {
        'Content-Type': 'application/json'
      }
    })
    const data = await response.json()
    props.action(); // close the form
    router.push('/sprints')
  }

  return (
    <div className={styles.modalContainer}>
      <div className={styles.modal}>
      <form onSubmit={handleFormSubmit}>
        <input type="number" value={id} onChange={event => setId(event.target.value) } placeholder="enter id..." name="id" /> 
        <input type="text" value={title} onChange={event => setTitle(event.target.value)} placeholder="enter title..." name="title" /> 
        <input type="text" value={status} onChange={event => setStatus(event.target.value)} placeholder="enter status..." name="status" /> 
        <input type="number" value={goalId} onChange={event => setGoalId(event.target.value)} placeholder="enter goad id..." name="goalID" /> 
        <input type="text" value={description} onChange={event => setDescription(event.target.value)} placeholder="enter description" name="description" /> 
        <input type="submit" value="Submit" />

      <button onClick={props.action}>Cancel</button>
      </form>
      </div>
    </div>
  )

}