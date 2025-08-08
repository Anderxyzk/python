class Livro:
    def __init__(self, titulo, autor, npaginas):
        self.titulo = titulo
        self.autor = autor
        self.npaginas = npaginas

    def livraria(self):
        print(f"Titulo: {self.titulo}, Autor: {self.autor}, Número de Páginas: {self.npaginas}")

catalogo = Livro("Titulo de Exmeplo", "Renato", "120")
catalogo.livraria()
