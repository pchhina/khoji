import Link from 'next/link'
import styles from '../styles/Nav.module.css'

export default function Nav() {
    return (
        <nav className={styles.nav}>
            <ul>
                <li>
                    <Link href='/'>Home</Link>
                    <Link href='/sprints'>Sprints</Link>

                </li>
            </ul>
        </nav>
    )
}