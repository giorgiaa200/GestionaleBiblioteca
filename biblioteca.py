class Autore:
    def __init__(self, nome, nazionalita):
        self.nome = nome
        self.nazionalita = nazionalita

# --- ISTANZE AUTORI ---
calvino = Autore("Italo Calvino", "Italiana")
orwell = Autore("George Orwell", "Britannica")
pirandello = Autore("Luigi Pirandello", "Italiana")


# ===== CLASSE LIBRO =====
class Libro:
    def __init__(self, titolo, isbn, autore):
        self.titolo = titolo
        self.isbn = isbn
        self.autore = autore
        self.disponibile = True

# --- ISTANZE LIBRI ---
libro1 = Libro("Il barone rampante", "001", calvino)
libro2 = Libro("1984", "002", orwell)
libro3 = Libro("La fattoria degli animali", "003", orwell)
libro4 = Libro("Sei personaggi in cerca d'autore", "004", pirandello)


# ===== CLASSE UTENTE =====
class Utente:
    MAX_PRESTITI = 3

    def __init__(self, nome, numero_tessera):
        self.nome = nome
        self.numero_tessera = numero_tessera
        self.prestiti_attivi = []

# --- ISTANZE UTENTI ---
mario = Utente("Mario Rossi", 100)
luigi = Utente("Luigi Bianchi", 200)


# ===== CLASSE PRESTITO =====
class Prestito:
    def __init__(self, libro, utente):
        self.libro = libro
        self.utente = utente
        self.data_prestito = "29/01/2026"
        self.data_restituzione = None

# --- ISTANZE PRESTITI (inizialmente vuote, saranno create dal metodo della biblioteca)
prestiti = []


# ===== CLASSE BIBLIOTECA =====
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
        libro = next((l for l in self.libri if l.isbn == isbn), None)
        utente = next((u for u in self.utenti if u.numero_tessera == numero_tessera), None)

        if libro is None:
            print("Libro non trovato")
            return
        if utente is None:
            print("Utente non trovato")
            return
        if not libro.disponibile:
            print("Libro già in prestito")
            return
        if len(utente.prestiti_attivi) >= Utente.MAX_PRESTITI:
            print("Utente ha raggiunto il limite di prestiti")
            return

        libro.disponibile = False
        prestito = Prestito(libro, utente)
        self.prestiti.append(prestito)
        utente.prestiti_attivi.append(prestito)
        print(f"Prestito registrato: {libro.titolo} a {utente.nome}")

    # restituisci libro
    def restituisci_libro(self, isbn):
        prestito = next((p for p in self.prestiti if p.libro.isbn == isbn and p.data_restituzione is None), None)
        if prestito is None:
            print("Prestito non trovato")
            return
        prestito.data_restituzione = "29/01/2026"
        prestito.libro.disponibile = True
        prestito.utente.prestiti_attivi.remove(prestito)
        print(f"Libro restituito: {prestito.libro.titolo} da {prestito.utente.nome}")

    # cerca libri per titolo o autore
    def cerca_libri(self, testo):
        return [l for l in self.libri if testo.lower() in l.titolo.lower() or testo.lower() in l.autore.nome.lower()]

    # libri disponibili
    def libri_disponibili(self):
        return [l for l in self.libri if l.disponibile]

    # storico prestiti utente
    def storico_prestiti_utente(self, numero_tessera):
        return [p for p in self.prestiti if p.utente.numero_tessera == numero_tessera]

# --- ISTANZA BIBLIOTECA ---
biblioteca = Biblioteca()
biblioteca.aggiungi_libro(libro1)
biblioteca.aggiungi_libro(libro2)
biblioteca.aggiungi_libro(libro3)
biblioteca.aggiungi_libro(libro4)
biblioteca.iscrivi_utente(mario)
biblioteca.iscrivi_utente(luigi)

# --- DEMO PRESTITI ---
biblioteca.presta_libro("001", 100)  # Mario prende libro1
biblioteca.presta_libro("002", 100)  # Mario prende libro2
biblioteca.presta_libro("003", 200)  # Luigi prende libro3

# --- LIBRI DISPONIBILI ---
print("Libri disponibili:")
for libro in biblioteca.libri_disponibili():
    print(f"{libro.titolo} - Autore: {libro.autore.nome}")

# --- RICERCA LIBRI ---
print("Cerca libri con 'Orwell':")
for libro in biblioteca.cerca_libri("Orwell"):
    print(f"{libro.titolo} - Autore: {libro.autore.nome}")



# --- STORICO PRESTITI ---
print("\nStorico prestiti Mario Rossi:")
for prestito in biblioteca.storico_prestiti_utente(100):
    stato = "Restituito" if prestito.data_restituzione else "In prestito"
    print(f"{prestito.libro.titolo} - {stato} - Prestito: {prestito.data_prestito} - Restituzione: {prestito.data_restituzione}")


# --- STORICO PRESTITI ---
print("\nStorico prestiti Luigi Bianchi:")
for prestito in biblioteca.storico_prestiti_utente(200):
    stato = "Restituito" if prestito.data_restituzione else "In prestito"
    print(f"{prestito.libro.titolo} - {stato} - Prestito: {prestito.data_prestito} - Restituzione: {prestito.data_restituzione}")





