export type Status = "todo" | "doing" | "done";
export type Priority = "low" | "medium" | "high";

export type Task = {
  id: number;
  title: string;
  description: string;
  status: Status;
  priority: Priority;
  effort_sp: number;
  dependencies: number[];
  created_at: string;
};

export async function fetchTasks(): Promise<Task[]> {
  const res = await fetch("/tasks");
  if (!res.ok) throw new Error("Failed to fetch tasks");
  return res.json();
}
