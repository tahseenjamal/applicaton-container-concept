# app_container_example.py
import inspect


# ----------- Container -----------
class Container:
    def __init__(self):
        self._bindings = {}

    def bind(self, key, value):
        self._bindings[key] = value

    def make(self, key):
        binding = self._bindings.get(key)

        if binding is None:
            raise Exception(f"No binding found for '{key}'")

        if callable(binding) and not isinstance(binding, type):
            return binding()  # Factory function

        if isinstance(binding, type):
            return self._resolve_class(binding)

        return binding  # Direct instance

    def _resolve_class(self, cls):
        signature = inspect.signature(cls.__init__)
        params = list(signature.parameters.values())[1:]  # Skip 'self'

        dependencies = []
        for param in params:
            if param.annotation == param.empty:
                raise Exception(
                    f"Missing type hint for '{param.name}' in {cls.__name__}"
                )

            dep_class = param.annotation
            dep_key = dep_class.__name__.lower()
            dep_instance = self.make(dep_key)
            dependencies.append(dep_instance)

        return cls(*dependencies)


# ----------- Services -----------


class DatabaseConnection:
    def __init__(self):  # ← Add this!
        pass

    def connect(self):
        return "Connected to the database"


class UserRepository:
    def __init__(self, db: DatabaseConnection):
        self.db = db

    def get_user(self):
        return f"User fetched using: {self.db.connect()}"


class AuthService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def login(self, username):
        return f"Logging in {username} → {self.user_repo.get_user()}"


# ----------- App Entry Point -----------

if __name__ == "__main__":
    container = Container()

    # Bind services
    container.bind("databaseconnection", DatabaseConnection)
    container.bind("userrepository", UserRepository)
    container.bind("authservice", AuthService)

    # Resolve and use AuthService
    auth = container.make("authservice")
    print(auth.login("john@example.com"))






