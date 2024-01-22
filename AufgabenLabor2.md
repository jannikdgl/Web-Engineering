# Aufgaben Labor 2


## Aufgabe 1.1
### 1. Recherchieren Sie zunächst im Internet nach dem Begriff XML Namespaces und erklären Sie den Einsatzzweck anhand eines konkreten Beispiels


XML Namespaces sind eine Möglichkeit, in XML-Dokumenten eindeutige Namenskonflikte zu vermeiden, wenn Elemente und Attribute aus verschiedenen Quellen stammen. Dies ist besonders wichtig, wenn verschiedene XML-Elemente oder Attribute denselben Namen haben könnten, aber unterschiedlichen Kontext oder Ursprung haben. XML Namespaces ermöglichen es, Elemente und Attribute zu gruppieren und zu kennzeichnen, um Kollisionen zu verhindern. Dies ist besonders relevant, wenn mehrere XML-basierte Sprachen oder Anwendungen in einem einzigen Dokument verwendet werden.

##### Beispiel:

```
<book>
  <author>
    <name>John Doe</name>
  </author>
  <publisher>
    <name>XYZ Publications</name>
  </publisher>
</book>


```

###### Mit Namespace

```
<book xmlns:author="http://example.com/authors"
      xmlns:publisher="http://example.com/publishers">
  <author:name>John Doe</author:name>
  <publisher:name>XYZ Publications</publisher:name>
</book>
```
Durch die Einführung von Namespaces mit den Präfixen "author" und "publisher" wird deutlich, welches "name"-Element zu welchem Namespace gehört. 