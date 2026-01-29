import { useState, useEffect } from 'react'
import { useParams, Link } from 'react-router-dom'
import { fetchStudy, type Algorithm, type Study } from '../api/client'

export default function AlgorithmViewer() {
  const { studyId, algoName } = useParams()
  const [study, setStudy] = useState<Study | null>(null)
  const [algorithm, setAlgorithm] = useState<Algorithm | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    if (studyId) {
      setLoading(true)
      fetchStudy(studyId)
        .then((data) => {
          setStudy(data)
          if (algoName) {
            const algo = data.core_algorithms.find(
              (a) => a.name === decodeURIComponent(algoName)
            )
            setAlgorithm(algo || null)
          }
        })
        .catch((err) => setError(err.message))
        .finally(() => setLoading(false))
    }
  }, [studyId, algoName])

  if (loading) {
    return <div className="loading">Loading...</div>
  }

  if (error) {
    return <div className="error">{error}</div>
  }

  if (algorithm && study) {
    return (
      <div className="algorithm-detail">
        <Link to="/algorithms">&larr; Back to algorithms</Link>
        <h2>{algorithm.name}</h2>
        <p className="study-info">From: {study.creator}</p>

        <section>
          <h3>Purpose</h3>
          <p className="purpose">{algorithm.purpose}</p>
        </section>

        <section>
          <h3>Pseudocode</h3>
          <pre>{algorithm.pseudocode}</pre>
        </section>

        {algorithm.inputs.length > 0 && (
          <section>
            <h3>Inputs</h3>
            <ul>
              {algorithm.inputs.map((input, i) => (
                <li key={i}>{input}</li>
              ))}
            </ul>
          </section>
        )}

        {algorithm.outputs.length > 0 && (
          <section>
            <h3>Outputs</h3>
            <ul>
              {algorithm.outputs.map((output, i) => (
                <li key={i}>{output}</li>
              ))}
            </ul>
          </section>
        )}
      </div>
    )
  }

  return (
    <div className="algorithm-browser">
      <h2>Algorithm Browser</h2>
      <p>
        Browse formalized narrative algorithms from 14 studies. Select a study to explore
        its algorithms.
      </p>

      {!studyId && (
        <div className="study-selector">
          <p>Select a study to view its algorithms, or browse all algorithms below.</p>
          <Link to="/">View all studies</Link>
        </div>
      )}
    </div>
  )
}
