import Link from 'next/link'
import styles from '../styles/Nav.module.css'
import { useSession } from "next-auth/react"

export default function Nav() {
  const { data: session } = useSession()
    return (
        <nav className={styles.nav}>
            <ul>
                <li>
                    <Link href='/'>Home</Link>
                    {session && <Link href='/sprints'>Sprints</Link>}
                    {!session && <Link href='/api/auth/signin'>Sign In</Link>}
                    {session && <Link href='/api/auth/signout'>Sign Out</Link>}

                </li>
            </ul>
        </nav>
    )
}