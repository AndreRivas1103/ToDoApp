class Todo:
    pass

    def __init__(self, code_id: int, title: str, description: str, completed: bool, tags: list[str]):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []

    def mark_completed(self):
        self.completed: bool = True

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return f"{self.code_id} - {self.title}"


class TodoBook:
    def __init__(self, todos: int):
        self.todos = {}

    def add_todo(self, title: str, description: str, ):
        todos_id = len(self.todos) + 1
        todos_new = Todo(code_id=todos_id, title=title, description=description)
        self.todos[todos_id] = todos_new
        return todos_id


class TodoBook:
    pass
