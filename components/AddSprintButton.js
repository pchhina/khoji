import {useState} from 'react'
import AddSprintForm from './AddSprintForm';

export default function AddSprintButton(props) {
  const [showForm, setShowForm] = useState(false);

  function handleSprintAdd() {
    setShowForm(true);
  }

  function handleFormClose() {
    setShowForm(false);
  }

  return (
    <>
      <div>
        <button onClick={handleSprintAdd}>Add Sprint</button>
      </div>
      {showForm && <AddSprintForm action={handleFormClose}/>}
    </>
  )

}