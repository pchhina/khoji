import Nav from './Nav.js'
import styles from '../styles/Layout.module.css'

export default function Layout(props) {
    return (
        <>
                <Nav />
        <div className={styles.conatiner}>
            <main className={styles.main}>
                {props.children}
            </main>
        </div>
        </>
    )
}