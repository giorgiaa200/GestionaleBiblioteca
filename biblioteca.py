#  CLASSE AUTORE 
class Autore:
    def __init__(self, nome, nazionalita):
        self.nome = nome
        self.nazionalita = nazionalita

#  ISTANZE AUTORI 
calvino = Autore("Italo Calvino", "Italiana")
orwell = Autore("George Orwell", "Britannica")
pirandello = Autore("Luigi Pirandello", "Italiana")


#  CLASSE LIBRO 
class Libro:
    def __init__(self, titolo, isbn, autore):
        self.titolo = titolo
        self.isbn = isbn
        self.autore = autore
        self.disponibile = True

# ISTANZE LIBRI 
libro1 = Libro("Il barone rampante", "001", calvino)
libro2 = Libro("Una boccata d'aria", "002", orwell)
libro3 = Libro("La fattoria degli animali", "003", orwell)
libro4 = Libro("Sei personaggi in cerca d'autore", "004", pirandello)



# CLASSE UTENTE 
class Utente:
    MAX_PRESTITI = 3

    def __init__(self, nome, numero_tessera):
        self.nome = nome
        self.numero_tessera = numero_tessera
        self.prestiti_attivi = []

# ISTANZE UTENTI 
mario = Utente("Mario Rossi", 100)
luigi = Utente("Luigi Bianchi", 200)


#  CLASSE PRESTITO 
class Prestito:
    def __init__(self, libro, utente):
        self.libro = libro
        self.utente = utente
        self.data_prestito = "29/01/2026"
        self.data_restituzione = None


#  CLASSE BIBLIOTECA 
class Biblioteca:
    def __init__(self):
        self.libri = []
        self.utenti = []
        self.prestiti = []

    # aggiungi libro al catalogo
    def aggiungi_libro(self, libro):
        self.libri.append(libro)

    # iscrivi utente

    def iscrivi_utente(self, utente):
        self.utenti.append(utente)

    # presta libro
    def presta_libro(self, isbn, numero_tessera):
        libro_trovato = None
        for libro in self.libri:
            if libro.isbn == isbn:
                libro_trovato = libro
                break
        if libro_trovato is None:
            print("Libro non trovato")
            return

        utente_trovato = None
        for utente in self.utenti:
            if utente.numero_tessera == numero_tessera:
                utente_trovato = utente
                break
        if utente_trovato is None:
            print("Utente non trovato")
            return

        if libro_trovato.disponibile == False:
            print("Libro già in prestito")
            return

        if len(utente_trovato.prestiti_attivi) >= Utente.MAX_PRESTITI:
            print("Utente ha già 3 libri in prestito")
            return

        libro_trovato.disponibile = False
        prestito = Prestito(libro_trovato, utente_trovato)
        self.prestiti.append(prestito)
        utente_trovato.prestiti_attivi.append(prestito)
        print("Prestito registrato:", libro_trovato.titolo, "a", utente_trovato.nome)

    # restituisci libro
    def restituisci_libro(self, isbn):
        prestito_trovato = None
        for prestito in self.prestiti:
            if prestito.libro.isbn == isbn and prestito.data_restituzione is None:
                prestito_trovato = prestito
                break
        if prestito_trovato is None:
            print("Prestito non trovato")
            return

        prestito_trovato.data_restituzione = "30/01/2026"
        prestito_trovato.libro.disponibile = True
        prestito_trovato.utente.prestiti_attivi.remove(prestito_trovato)
        print("Libro restituito:", prestito_trovato.libro.titolo, "da", prestito_trovato.utente.nome)

    # cerca libri
    def cerca_libri(self, testo):
        risultati = []
        for libro in self.libri:
            if testo.lower() in libro.titolo.lower() or testo.lower() in libro.autore.nome.lower():
                risultati.append(libro)
        return risultati

    # libri disponibili
    def libri_disponibili(self):
        disponibili = []
        for libro in self.libri:
            if libro.disponibile:
                disponibili.append(libro)
        return disponibili

    # storico prestiti utente
    def storico_prestiti_utente(self, numero_tessera):
        storico = []
        for prestito in self.prestiti:
            if prestito.utente.numero_tessera == numero_tessera:
                storico.append(prestito)
        return storico


# ISTANZA BIBLIOTECA 
biblioteca = Biblioteca()
biblioteca.aggiungi_libro(libro1)
biblioteca.aggiungi_libro(libro2)
biblioteca.aggiungi_libro(libro3)


biblioteca.aggiungi_libro(libro4)
biblioteca.iscrivi_utente(mario)
biblioteca.iscrivi_utente(luigi)

# DEMO PRESTITI 
biblioteca.presta_libro("001", 100)  # Mario prende libro1
biblioteca.presta_libro("002", 100)  # Mario prende libro2
biblioteca.presta_libro("003", 200)  # Luigi prende libro3

# LIBRI DISPONIBILI 
print("\nLibri disponibili:")
for libro in biblioteca.libri_disponibili():
    print(f"{libro.titolo} - Autore: {libro.autore.nome}")

# RICERCA LIBRI 
print("\nCerca libri con 'Orwell':")
for libro in biblioteca.cerca_libri("Orwell"):
    print(f"{libro.titolo} - Autore: {libro.autore.nome}")

#  STORICO PRESTITI MARIO 
print("\nStorico prestiti Mario Rossi:")
for prestito in biblioteca.storico_prestiti_utente(100):
    stato = "Restituito" if prestito.data_restituzione else "In prestito"
    print(f"{prestito.libro.titolo} - {stato} - Prestito: {prestito.data_prestito} - Restituzione: {prestito.data_restituzione}")

#  STORICO PRESTITI LUIGI 
print("\nStorico prestiti Luigi Bianchi:")
for prestito in biblioteca.storico_prestiti_utente(200):
    stato = "Restituito" if prestito.data_restituzione else "In prestito"
    print(f"{prestito.libro.titolo} - {stato} - Prestito: {prestito.data_prestito} - Restituzione: {prestito.data_restituzione}")

    