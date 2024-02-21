# Aufgabe 5

#### 1. ZIP ist ein sogenanntes Container-Format. Erklären Sie den Begriff und den Aufbau einer ZIP-Datei.

ZIP ist ein weit verbreitetes Dateiformat, das als Container für die Komprimierung und Archivierung von Dateien und Verzeichnissen verwendet wird. Es ermöglicht das Zusammenfassen mehrerer Dateien und Verzeichnisse in einer einzelnen Datei, wodurch sie platzsparender gespeichert und einfacher übertragen werden können. Der Begriff "ZIP" steht für Reisverschluss (englisch: "Zipper").

1. Dateiverzeichnis (Central Directory): Am Ende der ZIP-Datei befindet sich ein Verzeichnis, das Metadaten über die enthaltenen Dateien und Verzeichnisse enthält. Dieses Verzeichnis ermöglicht es, schnell auf bestimmte Dateien zuzugreifen, ohne die gesamte ZIP-Datei durchsuchen zu müssen. Es enthält Einträge für jede Datei oder jedes Verzeichnis, einschließlich ihrer Namen, Größen, Kompressionsmethoden und Positionen innerhalb der ZIP-Datei.

2. Dateien und Verzeichnisse: Vor dem Dateiverzeichnis befinden sich die eigentlichen Daten, die komprimierten Dateien und Verzeichnisse. Diese Daten sind normalerweise komprimiert, um Speicherplatz zu sparen. Jede Datei und jedes Verzeichnis wird als Eintrag in der ZIP-Datei gespeichert, einschließlich ihrer Metadaten wie Dateinamen, Größe und Kompressionsmethode.
3. End of Central Directory Record: Dieser Bereich am Ende der ZIP-Datei enthält Metadaten über das gesamte ZIP-Archiv, wie die Anzahl der Dateien, die Größe des zentralen Verzeichnisses und andere relevante Informationen. Es dient dazu, das Ende des ZIP-Archivs zu markieren und wichtige Informationen über die Struktur des Archivs bereitzustellen.

Insgesamt ermöglicht der Aufbau einer ZIP-Datei die effiziente Komprimierung und Archivierung von Dateien und Verzeichnissen, wodurch sie in einem einzigen Paket gebündelt und leicht übertragen oder gespeichert werden können.

#### 2. Was versteht man unter dem Mime Media Type von Daten? Wie lautet dieser für ZIP-Dateien?

Der MIME Media Type (auch MIME-Typ genannt) ist ein Standard, der verwendet wird, um den Inhalt und das Format von Daten in einem Internetumfeld zu kennzeichnen. MIME steht für "Multipurpose Internet Mail Extensions" und wurde ursprünglich entwickelt, um verschiedene Dateitypen in E-Mail-Nachrichten zu kennzeichnen. Heute wird der MIME-Typ in einer Vielzahl von Anwendungen und Protokollen verwendet, um den Typ von Daten anzugeben, der über das Internet übertragen wird.

Für ZIP-Dateien lautet der MIME Media Type: "application/zip"

Dieser MIME-Typ gibt an, dass die Datei eine ZIP-Datei ist und normalerweise komprimierte Daten oder Verzeichnisse enthält. Beim Übertragen von ZIP-Dateien über das Internet oder beim Arbeiten mit Webanwendungen wird dieser MIME-Typ verwendet, um die Art der Datei zu identifizieren und entsprechend zu verarbeiten.


#### 3. Was verbirgt sich hinter dem Namen Ecma International (Ecma)?

Ecma International ist eine Organisation, die Standards für Technologien wie Programmiersprachen und Dateiformate entwickelt. Bekannte Standards sind ECMAScript (JavaScript), Office Open XML und die C# Language Specification. Die Organisation fördert offene und interoperable Technologien.

Office Open XML Dokumente werden im Ecma-376 Standard definiert. Office Open XML
Dokumente werden in sogenannte Packages abgespeichert. Welches Format verwendet ein
Package und aus welchen Bestandteilen besteht dieses?

#### 4. Office Open XML Dokumente werden im Ecma-376 Standard definiert. Office Open XML Dokumente werden in sogenannte Packages abgespeichert. Welches Format verwendet ein Package und aus welchen Bestandteilen besteht dieses?

Office Open XML-Dokumente werden im Ecma-376-Standard definiert. Diese Dokumente werden in sogenannte Packages im ZIP-Format abgespeichert. Ein Package besteht aus einer Sammlung von XML-basierten Dateien, darunter Hauptdokumente, Zusatzinformationen, Bilder und andere Ressourcen, die für das Dokument benötigt werden.

#### 5. Beschreiben Sie den Unterschied zwischen wohlgeformten und gültigen XML-Dokumenten.

Ein wohlgeformtes XML-Dokument muss bestimmte strukturelle Regeln einhalten, einschließlich:

1. Korrektes Tag-Pairing: Jedes Öffnungstag muss ein entsprechendes Schließtag haben, und die Tags müssen ordnungsgemäß verschachtelt sein.

2. Einhaltung der Groß- und Kleinschreibung: XML ist case-sensitive, daher müssen Tags und Attribute konsistent verwendet werden.

3. Korrekte Attributsyntax: Attribute müssen innerhalb von Tags korrekt formatiert sein, d. h. mit einem Attributnamen, einem Gleichheitszeichen und einem Wert, der in Anführungszeichen eingeschlossen ist.

4. Verwendung von Escapings: Bestimmte Zeichen wie "<" und ">" müssen entweder in CDATA-Abschnitten oder durch Escapezeichen wie "<" und ">" dargestellt werden.

Ein gültiges XML-Dokument ist ein wohlgeformtes Dokument, das zusätzlich zu den oben genannten strukturellen Regeln auch alle Regeln einer definierten XML-Sprachspezifikation einhält. Diese Regeln können DTDs (Document Type Definitions), XML-Schemas oder andere Schema-Spezifikationen sein. Gültige XML-Dokumente müssen sich an die Struktur und die zulässigen Inhalte halten, die in der verwendeten Spezifikation definiert sind.

#### 6. Was ist eine XML-Bombe? Geben Sie ein Beispiel für eine XML-Bombe an.

Eine XML-Bombe ist ein XML-Dokument, das dazu entworfen ist, eine XML-Parser-Implementierung zu überlasten oder zum Absturz zu bringen. Sie besteht aus einer sehr großen XML-Struktur, die eine große Menge an Speicher und Rechenleistung erfordert, um verarbeitet zu werden.

Bombe: 

```
<!DOCTYPE bomb [
<!ENTITY a "xxxxxxxxxx">
<!ENTITY b "&a;&a;&a;&a;&a;&a;&a;&a;&a;&a;">
<!ENTITY c "&b;&b;&b;&b;&b;&b;&b;&b;&b;&b;">
<!ENTITY d "&c;&c;&c;&c;&c;&c;&c;&c;&c;&c;">
<!ENTITY e "&d;&d;&d;&d;&d;&d;&d;&d;&d;&d;">
<!ENTITY f "&e;&e;&e;&e;&e;&e;&e;&e;&e;&e;">
<!ENTITY g "&f;&f;&f;&f;&f;&f;&f;&f;&f;&f;">
<!ENTITY h "&g;&g;&g;&g;&g;&g;&g;&g;&g;&g;">
<!ENTITY i "&h;&h;&h;&h;&h;&h;&h;&h;&h;&h;">
]>
<bomb>&i;</bomb>

```


#### 7. Was ist ein XML External Entity Attack? Geben Sie ein Beispiel dafür an.


Eine XML External Entity (XXE)-Attacke ist eine Art von Angriff, bei dem ein Angreifer einen XML-Parser dazu verleitet, externe Inhalte zu laden und zu verarbeiten, die sich außerhalb des beabsichtigten Anwendungsbereichs befinden. Dies kann dazu führen, dass vertrauliche Daten offengelegt werden oder dass der Angriff als Teil einer größeren Sicherheitslücke auf einem System ausgeführt wird.

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE data [
<!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<data>
&xxe;
</data>

```