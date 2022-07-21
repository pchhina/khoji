import {sprints} from '../../../data'

export default function handler(req, res) {
    const id = req.query.id;
    const filtered = sprints.filter(sprint => Number.parseInt(sprint.id) === Number.parseInt(id))
    res.status(200).json(filtered[0]);
}