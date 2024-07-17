from dataclasses import dataclass, field

#User
@dataclass
class User:
    name: str
    Card: int
    Admin: bool = False
    Money: float = 100.0

#Menu
Menu = {
    #"NameProduct": 0 # NameProduct , Value,
    "Temaki de Salmão": 18.90,
    "Hot Roll": 16.50,
    "Sushi de Atum": 12.00,
    "Sashimi de Salmão": 20.00,
    "Yakissoba": 25.00,
    "Gyoza": 15.00,
    "Shimeji na Manteiga": 22.00,
    "Sunomono": 10.00,
    "Missoshiru": 8.00,
    "Uramaki Califórnia": 14.00,
    "Nigiri de Camarão": 18.00,
    "Harumaki": 12.00
}
# Este Code Nao foi feito para ser seguro, somente em versoes superiores sera colcao cripitogarfia e .env
pagers = [i for i in range(1, 51)]

admins = [
    {"name":"Quitto","senha":"123"},
]

orders = []

manager = "12345"