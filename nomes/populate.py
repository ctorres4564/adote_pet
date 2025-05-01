from .models import NomePet

def popular_nomes():
    nomes = [
        "Rex", "Luna", "Thor", "Mel", "Max", "Bidu", "Nina", "Tico", "Mingau", "Bolinha",
        "Pipoca", "Bella", "Chico", "Fofinho", "Lili", "Tigrão", "Doguinho", "Miau", "Ziggy", "Simba",
        "Tom", "Jerry", "Pitoco", "Nico", "Lola", "Pandora", "Bob", "Meg", "Belinha", "Cookie",
        "Toby", "Amora", "Cacau", "Snow", "Sandy", "Frajola", "Zelda", "Bolt", "Apolo", "Kiara",
        "Blue", "Pretinha", "Estrela", "Tufão", "Dory", "Kiko", "Jujuba", "Zeus", "Tita", "Costelinha",
        "Lelé", "Fred", "Sushi", "Nemo", "Lolita", "Pérola", "Chiquinha", "Sol", "Marley", "Raika",
        "Artemis", "Preto", "Branquinho", "Tron", "Skye", "Cristal", "Ozzy", "Sirius", "Raposa", "Panqueca",
        "Batata", "Caramelo", "Toquinho", "Bisteca", "Fubá", "Malu", "Bambam", "Leléco", "Zeca", "Clarinha",
        "Tina", "Maya", "Romeu", "Julieta", "Xuxu", "Naná", "Xuxa", "Fafá", "Nino", "Teca",
        "Biscoito", "Pudim", "Feijão", "Melão", "Tâmara", "Pantera", "Café", "Churros", "Rabanete", "Picles"
    ]

    for nome in nomes:
        NomePet.objects.get_or_create(nome=nome)

    print(f"{len(nomes)} nomes adicionados (ou já existentes)")

    nomes = []

    for nome in nomes:
        NomePet.objects.get_or_create(nome=nome)
    
    print(f"{len(nomes)} nomes adicionados (ou já existentes)")


    
