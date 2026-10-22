import { Routes, Route, Link } from 'react-router-dom'
import Home from './pages/Home/Home'
import Stats from './pages/Stats/Stats'

function App() {
  return (
    <div>
      <h1>Manajemen Buku</h1>
      <nav>
        <Link to="/">Home</Link> | <Link to="/stats">Statistik</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/stats" element={<Stats />} />
      </Routes>
    </div>
  )
}

export default App