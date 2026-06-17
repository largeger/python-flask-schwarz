# Projekt-Aufgabe: SkillTest – Das sichere Quiz-System mit Flask

## 1. Szenario und Zielsetzung
Wissen spielerisch abfragen! Sie sollen ein modulares Quiz-System ("SkillTest") entwickeln. Der Schwerpunkt liegt auf der **Strukturierung großer Anwendungen** durch Blueprints, der sicheren **Verarbeitung von Formulardaten (POST)** und der Nutzung von **Sessions**, um den Spielstand über mehrere Seiten hinweg zu speichern.

Das System soll verschiedene Themenbereiche (z.B. Python, Web, Allgemeinwissen) unterstützen, den Nutzer durch eine Serie von Fragen führen und am Ende eine detaillierte Auswertung präsentieren.

---

## 2. Projektarchitektur & Struktur
Das Projekt muss zwingend Blueprints nutzen, um Logikbereiche zu trennen:

```text
skilltest_app/
│
├── main.py                # App-Factory & Registrierung
├── blueprints/
│   ├── auth.py            # Login & Session-Start
│   ├── quiz.py            # Fragen-Logik & Formular-Handling
│   └── results.py         # Auswertung & Highscore
│
├── data/
│   └── questions.json     # (Optional) Fragen-Datenquelle
│
├── static/
│   └── css/
│       └── style.css      # Modernes UI-Design
│
└── templates/
    ├── layout.html        # Basis-Layout
    ├── auth/              # Templates für Login
    ├── quiz/              # Templates für Fragen
    └── results/           # Templates für die Auswertung
```

---

## 3. Detaillierte Anforderungen

### Teil A: Struktur & Blueprints
1. **App Factory:** Erstellen Sie die Flask-App in einer `create_app()` Funktion.
2. **Modularisierung:** Implementieren Sie mindestens drei Blueprints (`auth`, `quiz`, `results`). Nutzen Sie `url_prefix` für eine saubere URL-Struktur (z.B. `/quiz/start`, `/quiz/frage/1`).

### Teil B: Formular-Verarbeitung & Validierung
1. **Dynamische Formulare:** Jede Frage wird über ein POST-Formular beantwortet.
2. **Sicherheit:** Validieren Sie im Backend, ob eine Antwort ausgewählt wurde. Geben Sie Feedback über **Flash-Messages**, wenn Eingaben fehlen.
3. **Antwort-Check:** Vergleichen Sie die gesendeten Daten mit der korrekten Lösung in Ihrer Datenquelle (Liste oder JSON).

### Teil C: State Management mit Sessions
Da HTTP zustandslos ist, müssen wir uns merken, wie viele Punkte der User hat:
1. **Session-Start:** Beim Start des Quiz wird der Score in `session['score'] = 0` initialisiert.
2. **Score-Update:** Bei jeder richtigen Antwort wird der Score in der Session erhöht.
3. **Session-Sicherheit:** Setzen Sie einen starken `SECRET_KEY` in der Konfiguration.

### Teil D: Auswertung & UX
1. **Feedback-Schleife:** Zeigen Sie nach jeder Antwort kurz an, ob sie richtig oder falsch war (Flash-Messages mit Kategorien `success` oder `danger`).
2. **Finale:** Berechnen Sie am Ende das Ergebnis in Prozent und zeigen Sie eine motivierende Nachricht basierend auf der Leistung an.
3. **Styling:** Nutzen Sie CSS-Transitions, um den Übergang zwischen Fragen angenehm zu gestalten.

---

## 4. Bonus-Herausforderung (Optional)
- **Timer:** Implementieren Sie einen Timer (via JavaScript), der die Zeit pro Frage begrenzt.
- **Datenbank-Anbindung:** Speichern Sie abgeschlossene Quiz-Runden in einer Datenbank (`SQLAlchemy`), um eine globale Highscore-Liste zu führen.
- **WTForms:** Nutzen Sie die Library `Flask-WTF` für eine noch professionellere Formular-Handhabung und CSRF-Schutz.

---

## 5. Neue Python-Konzepte
Für dieses Projekt vertiefen Sie:
- **`flask.session`**: Speichern von Daten über mehrere Requests hinweg.
- **`flask.Blueprint`**: Fortgeschrittene Modularisierung.
- **Nested Templates**: Organisation von HTML-Dateien in Unterordnern.

---

## 6. Bewertungskriterien
- **Struktur:** Sind die Blueprints logisch getrennt und sauber registriert?
- **User Flow:** Funktioniert das Quiz ohne Sackgassen? Wird der Score korrekt mitgezählt?
- **Validierung:** Werden leere Antworten abgefangen?
- **Code-Qualität:** Ist der Code lesbar und folgt den Flask-Konventionen?

---

**Viel Erfolg beim Bau von SkillTest! 🧠💡**
