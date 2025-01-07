from dataclasses import dataclass, field
from faker import Faker as Fake

@dataclass
class User:
    role: str
    status: str
    password: str = field(default_factory=Fake().password)
    username: str = field(default_factory=Fake().user_name)
    employee_name: str = "Shiva Kumar Gupta"

    def __post_init__(self):
        if not self.username:
            self.username = Fake().user_name()

    def __str__(self):
        return f'User(username={self.username}, password={self.password}, role={self.role}, status={self.status}, employee_name={self.employee_name})'

    def __repr__(self):
        return f'User(username={self.username}, password={self.password}, role={self.role}, status={self.status}, employee_name={self.employee_name})'