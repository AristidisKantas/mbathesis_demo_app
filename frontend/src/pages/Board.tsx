import { useEffect, useState } from "react";
import { fetchTasks, Task } from "../api";

function Column({ title, tasks }: { title: string; tasks: Task[] }) {
  return (
    <div style={{ flex: 1, border: "1px solid #ddd", borderRadius: 12, padding: 12 }}>
      <h3>{title}</h3>
      {tasks.map((t) => (
        <div key={t.id} style={{ border: "1px solid #eee", borderRadius: 10, padding: 10, marginBottom: 10 }}>
          <strong>#{t.id} {t.title}</strong>
          <div style={{ fontSize: 13, opacity: 0.8, marginTop: 6 }}>
            SP: {t.effort_sp} • Priority: {t.priority}
          </div>
          <div style={{ fontSize: 13, marginTop: 6 }}>
            Deps: {t.dependencies.length ? t.dependencies.join(", ") : "none"}
          </div>
        </div>
      ))}
    </div>
  );
}

export default function Board() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [err, setErr] = useState<string | null>(null);

  useEffect(() => {
    fetchTasks()
      .then(setTasks)
      .catch((e) => setErr(String(e)));
  }, []);

  const todo = tasks.filter((t) => t.status === "todo");
  const doing = tasks.filter((t) => t.status === "doing");
  const done = tasks.filter((t) => t.status === "done");

  return (
    <div>
      {err && <div style={{ color: "crimson" }}>Error: {err}</div>}
      <div style={{ display: "flex", gap: 12 }}>
        <Column title="To Do" tasks={todo} />
        <Column title="Doing" tasks={doing} />
        <Column title="Done" tasks={done} />
      </div>
      <p style={{ marginTop: 12, fontSize: 13, opacity: 0.75 }}>
        TODO: add filters, error states, optimistic updates, dependency visualization.
      </p>
    </div>
  );
}
