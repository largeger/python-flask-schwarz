## Woche 0: Vorbereitung im Selbststudium
### Themen: 
Grundlegende Programmierkonzepte mit Python (Variablen, Datentypen, einfache Funktionen), Installation der notwendigen Entwicklungsumgebung (z.B. VS Code).

### Lernziele:
- Reproduktion: Die Teilnehmenden können die Begriffe "Variable", "String", "Integer" und "Funktion" definieren.
- Anwendung: Sie können nach Anleitung eine Entwicklungsumgebung auf ihrem Rechner installieren und kleine, vorgegebene Python-Skripte ausführen.

Eventuell auf Javascript umstellen?

---
## Woche 1: Frontend I - Struktur und Gestaltung mit HTML & CSS
### Themen: 
- Wie funktioniert das Web (Client-Server-Modell)?
- Grundlagen von HTML5 für die Struktur und CSS3 für das Design.
- CSS Components & Layouts 🆙 Reproduktion
- Bootstrap / Tailwind CSS ☑️ Anwendung

### Lernziele:
- Reproduktion: Die Teilnehmenden können die Funktion von HTML und CSS erklären und grundlegende HTML-Tags benennen.
- Anwendung: Sie können eine einfache, statische Webseite (z.B. einen Lebenslauf) mit HTML strukturieren und mit CSS gestalten.
- Übertragung: Sie können das Layout einer fremden, einfachen Webseite analysieren und mit eigenen Mitteln nachbauen.
### Selbststudium (LMS):
- Lernmodule zu den Grundlagen von HTML: Wichtige Tags, semantische Struktur.
- Lernmodule zu den Grundlagen von CSS: Selektoren, Eigenschaften, das Box-Model.
- Video-Tutorials zu grundlegenden Layout-Techniken wie Flexbox.

### Präsenz mit Trainer:
- Coding-Demo: Der Trainer baut live das Grundgerüst einer Webseite.
- Praktische Übung: Die Teilnehmenden bauen eine eigene statische Webseite (z.B. Visitenkarte) und werden vom Trainer bei CSS-Layout-Problemen unterstützt.
- Vorstellung und Besprechung der Ergebnisse.

### Abdeckung LWS:
- Komplett möglich

---
## Woche 2: Frontend II - Interaktivität mit JavaScript
### Themen: 
- Grundlagen von JavaScript
- DOM-Manipulation (Elemente selektieren und verändern)
- Event Handling (z.B. auf Klicks reagieren).
- Iterators & Events in JS  Anwendung
- HTTP & APIs (Basics: Fetch, Requests in JS & Python) ⏭️ Woche 4 ???
- AJAX & External Packages (z. B. Axios / Python requests) ⏭️ Woche 4 ???
- Stimulus JS (oder Alpine.js) 🆙  Reproduktion

### Lernziele:
- Reproduktion: Die Teilnehmenden können den Zweck des DOM (Document Object Model) erläutern.
- Anwendung: Sie können die in Woche 2 erstellte Webseite durch JavaScript interaktiv machen (z.B. ein Kontaktformular, das bei Klick eine Nachricht anzeigt).
- Übertragung: Sie können eine kleine, neue interaktive Komponente (z.B. einen Dark-Mode-Umschalter) eigenständig für ihre Webseite entwickeln.

### Selbststudium (LMS):
- Lernmodule zu den JavaScript-Grundlagen: Variablen, Funktionen, Events.
- Theoretische Einführung in das Document Object Model (DOM).

### Präsenz mit Trainer:
- Live-Coding: Der Trainer zeigt, wie man HTML-Elemente mit JavaScript selektiert und manipuliert.
- Praktische Übung: Die Teilnehmenden erweitern ihre Webseite aus ## Woche 2 um interaktive Elemente (z.B. Buttons, die Text ein-/ausblenden).
- Debugging-Session: Gemeinsames Suchen und Beheben von typischen JavaScript-Fehlern.

### Abdeckung LWS:
- Komplett möglich - Einarbeitung notwendig

---
## Woche 3: Daten & APIs
### Themen: 
- Grundlagen von Datenstrukturen (JSON)
- Konzept von APIs (Application Programming Interfaces)
- Daten von einer öffentlichen API abrufen (fetch) und auf der Webseite anzeigen.

### Lernziele:
- Reproduktion: Die Teilnehmenden können erklären, was eine API ist und wofür JSON verwendet wird.
- Anwendung: Sie können Daten von einer vorgegebenen, öffentlichen API (z.B. eine Wetter-API) abrufen und die Ergebnisse auf ihrer Webseite darstellen.
- Übertragung: Sie können eine andere öffentliche API selbstständig recherchieren und deren Daten in ihre Webseite integrieren.

### Selbststudium (LMS):
- Theoretische Lerneinheit: Was ist eine API? Wie ist JSON aufgebaut?
- Lektüre der Dokumentation einer einfachen, öffentlichen API.

### Präsenz mit Trainer:
- Live-Demo: Der Trainer ruft per JavaScript Daten von einer API ab und stellt diese auf einer Webseite dar.
- Praktische Übung: Die Teilnehmenden binden eine öffentliche API (z.B. für Wetterdaten oder Witze) in ihre eigene Webseite ein.
- Besprechung: Umgang mit asynchronen Operationen und möglichen Fehlern.

### Abdeckung LWS:
- Komplett möglich - Einarbeitung notwendig
---
## Woche 4: Datenbanken & Agile Methoden
### Themen: 
- Grundkonzepte von Datenbanken (warum? was ist SQL?)
- einfache Abfragen (SELECT, INSERT)
- Einführung in agile Entwicklung (Scrum in a Nutshell: Rollen, Events, Artefakte).
- SQL vs NoSQL
- SQLAlchemy ORM Basics
- Associations & Validations (1:n, n:m in SQLAlchemy)
- Agile Development Grundlagen
- Product Design Sprint (Vorbereitung Anschlussprojekt)

### Lernziele:
- Reproduktion: Die Teilnehmenden können die Scrum-Rollen (Product Owner, Scrum Master, Developer) und die grundlegende Funktionsweise einer SQL-Datenbank beschreiben.
- Anwendung: Sie können einfache SQL-Befehle ausführen, um Daten aus einer Tabelle zu lesen oder hinzuzufügen. Sie können in einer simulierten Sprint-Planung User Stories in Aufgaben zerlegen.
- Übertragung: Sie können eine einfache Anforderung (z.B. "Die App soll sich Zitate merken können") in eine Datenbankstruktur und die notwendigen Backend-Anpassungen übersetzen.
### Selbststudium (LMS):
- Theoretische Lerneinheit: Grundlagen relationaler Datenbanken (Tabellen, Spalten, Schlüssel).
- Interaktives Tutorial zu grundlegenden SQL-Befehlen (SELECT, FROM, WHERE).
- Video-Training zu den Grundlagen von Scrum (Rollen, Events).
- Präsenz mit Trainer:
- Praktische SQL-Übungen an einer vom Trainer bereitgestellten Beispieldatenbank.
- Diskussion: Wie verbindet man eine Datenbank mit dem Flask-Backend?
- Workshop: Simulation eines "Product Design Sprints", bei dem Anforderungen für die Projektwoche in User Stories formuliert werden.

### Abdeckung LWS:
- Komplett möglich (ohne die kursiven Zusatzthemen)
---
## Woche 5: Cloud-Konzepte & Deployment
### Themen: 
- Überblick Cloud vs. On-Premise. 
- Was sind IaaS, PaaS, SaaS? 
- Was ist ein Container (Docker) auf konzeptioneller Ebene? 
- Geführtes Deployment einer einfachen Anwendung auf einer PaaS-Plattform (Platform as a Service).
- Deployment einer eigenen kleinen App (ein kleines Projekt aus den Vorwochen)

### Lernziele:
- Reproduktion: Die Teilnehmenden können die Servicemodelle IaaS, PaaS und SaaS voneinander unterscheiden und den Zweck eines Docker-Containers erklären.
- Anwendung: Sie können ihre in Woche 5 erstellte Backend-Anwendung nach einer detaillierten Schritt-für-Schritt-Anleitung auf einer Cloud-Plattform bereitstellen.
- Selbststudium (LMS):
- Theoretische Lerneinheiten: Cloud vs. On-Premise, Unterschiede zwischen IaaS, PaaS, SaaS.
- Konzeptionelle Einführung in Container-Technologie mit Docker.
### Präsenz mit Trainer:
- Q&A-Session zu den Cloud-Konzepten.
- Geführte Schritt-für-Schritt-Anleitung: Die Teilnehmenden deployen ihre Backend-Anwendung gemeinsam mit dem Trainer auf einer einfachen PaaS-Plattform. Dies ist eine reine Anwendungs-Session, um Berührungsängste abzubauen.
### Abdeckung LWS:
- Komplett möglich - Einarbeitung notwendig
---
## Woche 6: Grundlagen der Programmierung & Versionskontrolle
### Themen: 
- Vertiefung Python (Schleifen, Bedingungen, Listen)
- Einführung in die Kommandozeile
- Einführung in Git
- Loops & Comprehensions ☑️ Anwendung
- Dictionaries & Sets ☑️ Anwendung
- Regular Expressions in Python (re Modul) 🆙 Reproduktion
- Parsing (CSV, JSON, Files, Web Scraping) ☑️ Anwendung
- Objektorientierung (nur Basics, nicht in Tiefe) ☑️ Reproduktion
### Lernziele:
- Reproduktion: Die Teilnehmenden können diegrundlegenden Befehle für Git (git add, git commit, git push, git pull) benennen.
- Anwendung: Sie können ein einfaches Python Programm schreiben, das Benutzereingaben verarbeitet und darauf reagiert (z.B. ein simpler Taschenrechner). Sie können Änderungen an ihrem Code mit Git versionieren.
- Übertragung: Sie können ein kleines Problem (z.B. "Sortiere eine Liste von Namen alphabetisch") selbstständig in ein Python-Skript übersetzen.
### Selbststudium (LMS):
- Lernmodule zu den Python-Grundlagen (Datentypen, Variablen, Bedingungen, Schleifen).
- Theoretische Einführung in die Versionskontrolle: Was ist Git und warum wird es verwendet?
- Anleitungen und Videos zu den grundlegenden Git-Befehlen (add, commit, push, pull).

### Präsenz mit Trainer:
- Recap und Q&A zu den Python-Grundlagen.
- Gemeinsames Live-Coding: Lösen kleinerer Programmieraufgaben in der Gruppe oder zu zweit.
- Praktische Git-Übung: Einrichten eines gemeinsamen Repositories, gemeinsames Durchspielen des Commit- und Push-Prozesses.

### Abdeckung LWS:
- Komplett möglich
---
## Woche 7: Backend-Grundlagen mit Python & Flask
### Themen: 
- Einführung in Backend-Konzepte
- Erstellen einer einfachen API mit Python und dem Framework Flask, die statische Daten (JSON) bereitstellt.
- Flask/Django Basics: Routing, Controllers & Views
- Models & CRUD (Flask-SQLAlchemy oder Django ORM)
- Advanced Routing (Blueprints in Flask / Django URLs)
- Static Assets (JS, CSS) & Image Upload
- Templating (Jinja2)
- Deployment

### Lernziele:
- Reproduktion: Die Teilnehmenden können den Unterschied zwischen Frontend und Backend erläutern.
- Anwendung: Sie können mit Flask eine simple Backend-Anwendung erstellen, die auf verschiedenen URL-Pfaden (Routen) vordefinierte JSON-Daten zurückgibt.
- Übertragung: Sie können ihre Frontend-Anwendung so anpassen, dass sie die Daten nicht mehr von einer öffentlichen API, sondern von ihrem eigenen Backend bezieht.

### Selbststudium (LMS):
- Theoretische Lerneinheit: Was ist ein Backend? Was ist eine MVC-Architektur? 
- Einführung in das Flask-Framework (Grundstruktur, Routing).

### Präsenz mit Trainer:
- Gemeinsames Aufsetzen eines minimalen Flask Servers von Grund auf.
- Live-Coding: Erstellen der ersten eigenen API Endpunkte, die Test-Daten im JSON-Format zurückgeben.
- Praktische Übung: Das eigene Frontend so umbauen, dass es die Daten vom eigenen Backend abruft.

### Abdeckung LWS:
- Fehlende Kenntnisse - Einarbeitung sehr aufwändig

---
## Woche 8: Projektwoche - Modifikation & Abschluss
### Thema: 
- Die Teilnehmenden erhalten eine zu 80% fertige Webanwendung (Frontend & Backend). Ihre Aufgabe ist es, den Code zu verstehen, bestehende Fehler zu beheben und eine kleine, definierte Funktionalität hinzuzufügen.
- Einzelne Komponenten aus den Vorwochen zusammenfügen und Anpassen
- Einen Tag in Woche 6 als Design-Sprint nutzen und sich bereits überlegen, welche Anwendung man bauen will (User Stories, User Journey, Wireframing, Figma)

### Lernziele:
- Anwendung: Sie können sich in eine fremde, aber überschaubare Codebasis einarbeiten und den Datenfluss zwischen Frontend und Backend nachvollziehen. Sie können unter Anleitung Änderungen im Code vornehmen, um eine neue Funktion zu implementieren.
- Übertragung: Sie können selbstständig einen Fehler in der Applikation identifizieren, die Ursache im Code lokalisieren und einen Lösungsansatz entwickeln. Am Ende der Woche präsentieren sie ihre Änderungen und Erkenntnisse.
- Demo der App vor erweitertem Publikum (z.B. vor Team oder Bereich)
### Selbststudium (LMS):
- In dieser Woche gibt es keine neuen Lerninhalte. DieZeit soll für die eigenständige Arbeit am Projekt genutzt werden.

### Präsenz mit Trainer:
- Der Trainer agiert als "Lead Developer" und Coach.
- Tägliche Stand-ups (Recap vom Vortag), um den Fortschritt zu besprechen und Blocker zu identifizieren.
- Unterstützung bei der Einarbeitung in die bestehende Codebasis.
- Pair-Programming-Sessions, um bei schwierigen Aufgaben zu helfen.
- Finale Präsentation und Review der umgesetzten Änderungen.

### Abdeckung LWS:
- Fehlende Kenntnisse - Einarbeitung sehr aufwändig