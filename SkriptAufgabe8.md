# Aufgaben 8 Skript 4

#### Was versteht man unter der BEM-Konvention?  Erstellen Sie die folgenden Beispiele mit BEM:

Die BEM (Block Element Modifier) ist eine Namenskonvention für CSS-Klassen in der Webentwicklung, die darauf abzielt, den Code besser lesbar, wartbar und skalierbar zu machen. Sie besteht aus drei Teilen: dem Block, dem Element und dem Modifier. Ein Block stellt ein eigenständiges Modul oder eine Komponente dar, ein Element ist ein Bestandteil dieses Blocks und ein Modifier modifiziert das Aussehen oder Verhalten eines Blocks oder Elements.


##### a. Section-Element in Main-Element soll rote Schrift erhalten.

HTML: 

```
<div class="main">
    <section class="main__section">Inhalt der Section</section>
</div>
```

CSS:
```
.main {
    
}
.main__section {
    color: red; 
}
```

##### b. Button mit <span>-Element und großer Schrift


HTML: 

```
<button class="button">
    <span class="button__text">Button-Text</span>
</button>

```

CSS:
```
.button {
   
}

.button__text {
    font-size: 20px; 
}
```

####  Erklären Sie die folgenden CSS-Selektoren h1[title], spa [hello="Cleveland"][goodbye="Columbus"], a[href^="http"]

Die folgenden CSS-Selektoren haben unterschiedliche Verwendungszwecke und wählen bestimmte Elemente auf einer Webseite aus:

Die folgenden CSS-Selektoren haben unterschiedliche Verwendungszwecke und wählen bestimmte Elemente auf einer Webseite aus:
1. h1[title]: Dieser Selektor wählt alle \<h1>-Elemente aus, die ein title-Attribut haben. Zum Beispiel wird \<h1 title="Überschrift"> ausgewählt, aber \<h1> ohne das title-Attribut wird nicht ausgewählt.

2. span[hello="Cleveland"][goodbye="Columbus"]: Dieser Selektor wählt alle <span>-Elemente aus, die sowohl das Attribut hello mit dem Wert "Cleveland" als auch das Attribut goodbye mit dem Wert "Columbus" haben. Es wählt also <span hello="Cleveland" goodbye="Columbus">, aber nicht <span hello="Cleveland"> oder <span goodbye="Columbus">.

3. a[href^="http"]: Dieser Selektor wählt alle \<a>-Elemente aus, deren href-Attribut mit "http" beginnt. Das bedeutet, dass alle Hyperlinks, die auf externe URLs verweisen und mit "http" starten, ausgewählt werden. Zum Beispiel wird \<a href="http://example.com"> ausgewählt, aber \<a href="https://example.com"> oder \<a href="ftp://example.com"> werden nicht ausgewählt.


#### Erstellen Sie ein Hintergrundimage für eine einfache Webseite mit einem linearen Farbverlauf von hellem Grau (rgb(190,190,190)) zu hellem Blau (rgb(195,215,250)). Der Farbgradient soll von links
nach verlaufen.

CSS: 
```
body {
    background-image: linear-gradient(to right, rgb(190, 190, 190), rgb(195, 215, 250));
}
```


#### Erstellen Sie einen Button der beim Hovern ("schweben über") mit ihrem Mauszeiger einen Tooltip (Kurzinformationen über Funktion des Buttons) anzeigt. Der Tooltip verschwindet nach 4s.

HTML: 
```
<button id="myButton">Button</button>
<div class="tooltip" id="myTooltip">Tooltip-Text</div>
```

CSS:
```
.tooltip {
    display: none;
    position: absolute;
    background-color: #555;
    color: #fff;
    padding: 5px;
    border-radius: 6px;
}

#myButton:hover + #myTooltip {
    display: block;
}
```

JavaSkript:
```
document.getElementById("myButton").addEventListener("mouseover", function() {
    document.getElementById("myTooltip").style.display = "block";
    setTimeout(function() {
        document.getElementById("myTooltip").style.display = "none";
    }, 4000); // 4 Sekunden
});
```

#### Erstellen Sie für eine Webseite ein sogenanntes Holy-Gray-Layout ("heiliger Gral") mit Hilfe einer Grid-Box. Die Webseite besitze einen \<header>, einen \<footer>, eine \<nav>-, eine \<aside>-Bar sowie einen \<article>.


HTML:
```
<div class="grid-container">
    <header>Header</header>
    <nav>Navigation</nav>
    <aside>Aside</aside>
    <article>Article</article>
    <footer>Footer</footer>
</div>
```

CSS:
```
.grid-container {
    display: grid;
    grid-template-columns: 1fr 3fr 1fr;
    grid-template-rows: auto;
    grid-template-areas: 
        "header header header"
        "nav article aside"
        "footer footer footer";
    min-height: 100vh;
}

header {
    grid-area: header;
    background-color: lightgray;
    padding: 10px;
}

nav {
    grid-area: nav;
    background-color: lightgray;
    padding: 10px;
}

aside {
    grid-area: aside;
    background-color: lightgray;
    padding: 10px;
}

article {
    grid-area: article;
    background-color: white;
    padding: 10px;
}

footer {
    grid-area: footer;
    background-color: lightgray;
    padding: 10px;
}
```

