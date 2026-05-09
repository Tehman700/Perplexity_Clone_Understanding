import { useState } from 'react'
import './App.css'

function App() {
  const [query, setQuery] = useState('')

  function handleSearch() {
    fetch('http://localhost:8000/conversation', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query })
    })
  }

  return (
    <div className="app">
      <h1>Purplexity.ai</h1>
      <input
        type="text"
        value={query}
        onChange={e => setQuery(e.target.value)}
        placeholder="Ask anything..."
      />
      <button onClick={handleSearch}>Search</button>
    </div>
  )
}

export default App
