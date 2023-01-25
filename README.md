### Projekt_PaMiW
# Projekt semestralny z przedmiotu "Programowanie aplikacji mobilnych i webowych".
***
Aplikacja została napisana przy użyciu języka Python, a frameworkiem był Flask. Dodatkowo aplikacja została zapakowana do Docker'a. 
W ramach projektu została napisana aplikacja webowa spełniająca poniższe wymagania:
* realizacja części serwerowa (dane "na sztywno" w pamięci);
* integracja z bazą danych (może być SQLite w pliku);
* usługa sieciowa oraz aplikacja internetowa, która z nią rozmawia (może to być REST API lub RPC API);
* zintegrowanie autoryzacji z Google/GitHub/Auth0 poprzez protokół OAuth 2.0; ew. Powiadomienia do klienta z serwera (Server-Sent Events, WebSockets);
***
# Sposób uruchomienia aplikacji
W celu uruchomienia aplikacji należy utworzyć obraz Dockera oraz uruchomić go. W tym celu należy skorzystać z poniższych poleceń:

**sudo docker build --tag pamiw_prezentacja .**

**sudo docker run -it -p 5000:5000 pamiw_prezentacja**
