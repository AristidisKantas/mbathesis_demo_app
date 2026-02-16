import Board from "./pages/Board";

export default function App() {
  return (
    <div style={{ padding: 24, fontFamily: "system-ui, sans-serif" }}>
      <h2>Mini Backlog Manager</h2>
      <p style={{ maxWidth: 900 }}>
        This UI is intentionally minimal. It supports agentic experiments by providing
        a realistic but small project surface.
      </p>
      <Board />
    </div>
  );
}
