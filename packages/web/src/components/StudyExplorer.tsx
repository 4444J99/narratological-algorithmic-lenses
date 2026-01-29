import { useState, useEffect } from 'react'
import { useParams, Link } from 'react-router-dom'
import { fetchStudies, fetchStudy, type Study, type StudySummary } from '../api/client'

export default function StudyExplorer() {
  const { studyId } = useParams()
  const [studies, setStudies] = useState<StudySummary[]>([])
  const [selectedStudy, setSelectedStudy] = useState<Study | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    fetchStudies()
      .then(setStudies)
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false))
  }, [])

  useEffect(() => {
    if (studyId) {
      setLoading(true)
      fetchStudy(studyId)
        .then(setSelectedStudy)
        .catch((err) => setError(err.message))
        .finally(() => setLoading(false))
    } else {
      setSelectedStudy(null)
    }
  }, [studyId])

  if (loading) {
    return <div className="loading">Loading...</div>
  }

  if (error) {
    return <div className="error">{error}</div>
  }

  if (selectedStudy) {
    return (
      <div className="study-detail">
        <Link to="/">&larr; Back to all studies</Link>
        <h2>{selectedStudy.creator}</h2>
        <p className="work">{selectedStudy.work}</p>
        <span className="category">{selectedStudy.category}</span>

        <section>
          <h3>Axioms ({selectedStudy.axioms.length})</h3>
          {selectedStudy.axioms.map((axiom) => (
            <div key={axiom.id} className="axiom-card">
              <strong>{axiom.id}: {axiom.name}</strong>
              <p>{axiom.statement}</p>
            </div>
          ))}
        </section>

        <section>
          <h3>Algorithms ({selectedStudy.core_algorithms.length})</h3>
          {selectedStudy.core_algorithms.map((algo) => (
            <div key={algo.name} className="algorithm-card">
              <strong>{algo.name}</strong>
              <p>{algo.purpose}</p>
              <Link to={`/algorithms/${selectedStudy.id}/${encodeURIComponent(algo.name)}`}>
                View Details
              </Link>
            </div>
          ))}
        </section>

        <section>
          <h3>Diagnostic Questions ({selectedStudy.diagnostic_questions.length})</h3>
          {selectedStudy.diagnostic_questions.map((q) => (
            <div key={q.id} className="question-card">
              <strong>{q.id}</strong>
              <p>{q.question}</p>
              <small>Valid if: {q.valid_if}</small>
            </div>
          ))}
        </section>
      </div>
    )
  }

  return (
    <div className="study-explorer">
      <h2>Narratological Studies</h2>
      <p>Explore 14 studies extracting narrative algorithms from master storytellers.</p>

      <div className="study-list">
        {studies.map((study) => (
          <Link key={study.id} to={`/study/${study.id}`} className="study-card">
            <h3>{study.creator}</h3>
            <div className="category">{study.category}</div>
            <div className="stats">
              <span>{study.axiom_count} axioms</span>
              <span>{study.algorithm_count} algorithms</span>
            </div>
          </Link>
        ))}
      </div>
    </div>
  )
}
