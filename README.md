# Application Container Example (Python)

This is a minimal demonstration of how an **Application Container** (also known as an IoC container or service container) can be implemented in Python. It showcases **automatic dependency injection** using constructor type hints and recursive resolution.

---

## 🧠 Concept

The container automatically resolves dependencies for classes by:

1. Inspecting their `__init__` constructor.
2. Reading the type hints of the parameters.
3. Recursively creating and injecting dependencies based on what's registered in the container.

---

## 🛠 Structure

- `Container`: A simple IoC container class that supports:
  - Binding class references, instances, or factory functions
  - Recursive dependency resolution
  - Automatic constructor injection based on type hints

- `DatabaseConnection`: A simple class that simulates a database connection.

- `UserRepository`: Depends on `DatabaseConnection`.

- `AuthService`: Depends on `UserRepository`.

---

## 🚀 How to Run

1. Make sure you have Python 3.6+ (for type hint support).
2. Run the script:

```bash
python main.py

