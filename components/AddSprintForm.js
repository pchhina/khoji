import { useState } from 'react'
import { useRouter } from 'next/router';
import styles from '../styles/UIKit.module.css'

export default function AddSprintForm(props) {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");

  const router = useRouter();


  async function handleFormSubmit(event) {
    event.preventDefault();
    props.action(); // close the form
    router.push('/sprints')
  }

  return (
    <div className={styles.modalContainer}>
      <div className={styles.modal}>
      <form onSubmit={handleFormSubmit}>
        <input type="text" value={title} onChange={event => setTitle(event.target.value)} placeholder="enter title..." name="title" /> 
        <input type="text" value={description} onChange={event => setDescription(event.target.value)} placeholder="enter description" name="description" /> 
        <input type="submit" value="Submit" />

      <button onClick={props.action}>Cancel</button>
      </form>
      </div>
    </div>
  )

}