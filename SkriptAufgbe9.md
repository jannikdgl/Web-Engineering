# Skript Aufgabe 9

####  Viele Browser stellen eine sogenannte Console zur Verfügung. Was versteht man unter dem Begriff REPL? Erläutern Sie dieses an einem konkreten JavaScript-Beispiel.

REPL steht für "Read-Eval-Print Loop" und bezieht sich auf eine interaktive Programmierumgebung, die es ermöglicht, Code schrittweise einzugeben, auszuführen, das Ergebnis zu evaluieren und dann erneut Code einzugeben. Dies geschieht in einer Endlosschleife (Loop), die eine schnelle Iteration und Überprüfung des Codes ermöglicht.

Beispiel: 

```
// Eingabe in der Konsole
> 2 + 3
// Ausgabe in der Konsole
5
```
In diesem Beispiel wird die Addition von 2 und 3 in der Konsole eingegeben. Das System bewertet den Ausdruck sofort und gibt das Ergebnis, 5, zurück.

#### Erstellen Sie ein JavaScript, dass die Primzahlen der folgenden 13-stelligen Dezimalzahl 7008514751431 bestimmt und die Zeit zur Berechnung dieses Faktorisierungsproblemes misst. Erhöhen Sie die Anzahl der Dezimalstellen und vergleichen Sie die Rechenzeiten. Führen Sie das Script in der Console ihres Browsers aus.

Code: 

```
function findPrimeFactors(number) {
    const factors = [];
    let divisor = 2;

    while (number > 2) {
        if (number % divisor === 0) {
            factors.push(divisor);
            number = number / divisor;
        } else {
            divisor++;
        }
    }
    return factors;
}

const start = performance.now(); // Startzeit messen
const number = 7008514751431;
const primeFactors = findPrimeFactors(number);
const end = performance.now(); // Endzeit messen
const timeTaken = end - start; // Zeitdauer berechnen

console.log('Primfaktoren:', primeFactors);
console.log('Zeit zur Berechnung:', timeTaken, 'Millisekunden');

```

#### Das Verschlüsselungsverfahren RSA verwendet 3072 Bits für das Faktorisierungsproblem. Wieviel Stellen besitzt die zugehörige Dezimalzahl?

926 Stellen

#### Erstellen Sie nun eine HTML-Seite mit einem \<body> ohne Inhalt. Ergänzen Sie den \<body> per JavaScript mit einem Button (Text: "Finde meine Geokoordinaten", Farbe: "orange", keine Umrandung,id="btn1") , der per Mausklick ihre Geokoordinaten bestimmt und diese im Textfeld des <body> ausgibt.

Code: 

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Geokoordinaten finden</title>
</head>
<body>

<script>
    function getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition);
        } else { 
            alert("Geolocation wird von Ihrem Browser nicht unterstützt.");
        }
    }

    function showPosition(position) {
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;
        const locationInfo = `Latitude: ${latitude}, Longitude: ${longitude}`;

        document.body.innerHTML += `<p>${locationInfo}</p>`;
    }
</script>

<button id="btn1" style="background-color: orange; border: none; padding: 10px 20px; color: white;" onclick="getLocation()">Finde meine Geokoordinaten</button>

</body>
</html>

```