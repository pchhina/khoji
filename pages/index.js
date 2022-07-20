import Head from 'next/head'
import styles from '../styles/Home.module.css'

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Khoji | Home </title>
        <meta name="description" content="Discover your passions!" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>

        <h1 className={styles.title}>
        Welcome to Khoji!
        </h1>

        <p className={styles.description}>
        Let&apos;s Go!
        </p>

      </main>

    </div>
  )
}
