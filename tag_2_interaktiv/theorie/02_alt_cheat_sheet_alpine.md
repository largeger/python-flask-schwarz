# 🍦 Alternative Tag 2: Progressive Enhancement mit Alpine.js

## 📖 Theorie-Impuls: Der "Sprinkles" Ansatz
Anstatt das komplette Frontend mit einem schweren Framework (wie React) neu zu bauen, nutzen wir Jinja2 für die Struktur und "bestreuen" (sprinkle) es mit kleinen, interaktiven JavaScript-Komponenten. **Alpine.js** ist dafür perfekt, da es direkt im HTML geschrieben wird.

---

## 🛠️ Alpine.js + Flask Cheat Sheet

### 1. Einbindung (CDN)
In dein `layout.html` im `<head>`:
```html
<script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>
```

### 2. Grundkonzepte
- `x-data`: Definiert einen Bereich mit eigenen Daten.
- `x-show`: Zeigt/Versteckt Elemente.
- `x-on` (oder `@`): Reagiert auf Events (Klick, Tastendruck).
- `x-text`: Ändert den Text eines Elements dynamisch.

### 3. Beispiel: Ein interaktives Dropdown
```html
<div x-data="{ open: false }">
    <button @click="open = !open">Menü umschalten</button>
 
    <div x-show="open" @click.outside="open = false">
        <ul>
            <li>Profil</li>
            <li>Einstellungen</li>
        </ul>
    </div>
</div>
```

### 4. Flask + Alpine.js (Datenübergabe) ⚠️
Nutze Jinja2, um den Startzustand zu setzen. **WICHTIG:** Nutze einfache Anführungszeichen (`'`) für das Attribut, da JSON doppelte Anführungszeichen nutzt!
```html
<div x-data='{ items: {{ my_list | tojson }} }'>
    ...
</div>
```

### 5. Funktionen in x-data
Für komplexere Logik definieren wir Funktionen direkt im `x-data` Objekt. Rufe sie im HTML am besten immer mit Klammern `()` auf:
```html
<div x-data='{ 
    items: [], 
    newItem: "",
    addItem() {
        if(this.newItem) {
            this.items.push(this.newItem);
            this.newItem = "";
        }
    } 
}'>
    <input x-model="newItem" @keydown.enter="addItem()">
    <button @click="addItem()">Add</button>
</div>
```

---

## 🎯 Lernziele für heute
- [ ] Alpine.js in ein Flask-Projekt einbinden
- [ ] Interaktive Komponenten ohne Seiten-Refresh bauen
- [ ] Den Unterschied zwischen Server-Side (Jinja) und Client-Side (Alpine) verstehen
- [ ] Dynamische Filter oder Suchfelder im Frontend umsetzen
