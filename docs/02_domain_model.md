# Domain Model

## Entities

### Task
Fields:
- `id` (integer)
- `title` (string)
- `description` (string)
- `status` (enum: `todo`, `doing`, `done`)
- `priority` (enum: `low`, `medium`, `high`)
- `effort_sp` (story points: {1,2,3,5,8,13})
- `dependencies` (list of task ids)
- `created_at` (timestamp, ISO-8601)

## Core rules (expected)
1. Dependencies must not form cycles (A -> B -> A).
2. A task should not move to `done` if its dependencies are not `done`.
3. `effort_sp` must be restricted to the allowed set.
4. Title must be non-empty and reasonably short.

Note: the code currently does **not** enforce all rules. These are candidates for future issues.
