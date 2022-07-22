import {sprints} from '../../../data'

export default function handler(req, res) {
  if (req.method === 'GET') {
    res.status(200).json(sprints)
  } else if (req.method === 'POST') {
    const data = req.body.formInputs; // data in body.formInput is 'property name' we set while sending data to this api
    console.log(data);
    sprints.push(data);
    res.status(201).json(data);
  }
}