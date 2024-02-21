## Aufgaben  6

### 1. Welche Zeichen sind in einem DNS-Namen erlaubt?

- Buchstaben von a bis z
- Zahlen von 0 bis 9
- Bindestriche (-)
- Punkt (.)


### 2. Was sind internationalisierte Domain-Namen (IDN: internationalized domain names)?

Internationale Domainnamen (IDN) ermöglichen die Verwendung von Zeichen aus verschiedenen Schriftsystemen, nicht nur aus dem ASCII-Zeichensatz. Dadurch können Domains in verschiedenen Sprachen und Schriftsystemen registriert und genutzt werden, was die Internetnutzung für Menschen weltweit erleichtert und fördert.


### 3. Was ist ein Punycode? Beschreiben Sie das Encoding-Verfahren textuell.

Punycode ist ein Encoding-Verfahren, das verwendet wird, um internationale Domainnamen (IDNs) in ASCII-Zeichen umzuwandeln, die für das Domain Name System (DNS) zulässig sind. Dies ist wichtig, da das DNS ursprünglich nur ASCII-Zeichen akzeptierte. Das Punycode-Verfahren basiert auf ASCII-Zeichen und verwendet eine spezielle Kodierung, um Zeichen aus nicht-ASCII-Schriftsystemen, wie beispielsweise kyrillische, arabische oder chinesische Schriftzeichen, in ASCII-Zeichen zu kodieren. Hier ist eine grobe Beschreibung des Verfahrens:

1. Zerlegung: Der nicht-ASCII-String wird in einzelne Zeichen zerlegt.

2. Normalisierung: Die Zeichen werden normalisiert, um verschiedene Schreibweisen zu vereinheitlichen.

3. Kodierung: Jedes normalisierte Zeichen wird in eine Zahlenfolge umgewandelt, die nur aus ASCII-Zeichen besteht. Dies geschieht mithilfe eines Algorithmus, der die Unicode-Codepunkte in ASCII-Zeichen konvertiert.

4. Konkatenierung: Die kodierten Zeichen werden zu einem einzigen String zusammengefügt, der den Punycode darstellt.

5. Hinzufügen des Präfix: Der Punycode-String wird mit dem Präfix "xn--" versehen, um anzuzeigen, dass er in Punycode kodiert ist.

#### 4. Was passiert wenn Sie in einem Browser eine IDN-URL eingeben. Beschreiben Sie den Ablauf.

Wenn Sie eine IDN-URL (internationalisierte Domainnamen) in einem Browser eingeben, durchläuft der Browser einen Prozess, um die IDN-URL in eine für das Domain Name System (DNS) verständliche Form zu übersetzen. Hier ist der Ablauf:

1. Eingabe der IDN-URL: Sie geben die IDN-URL in die Adressleiste des Browsers ein und drücken Enter.

2. Punycode-Konvertierung: Der Browser erkennt, dass es sich um eine IDN-URL handelt, die nicht aus reinen ASCII-Zeichen besteht. Er wandelt dann die nicht-ASCII-Zeichen mithilfe des Punycode-Verfahrens in ASCII-Zeichen um. Dieser Schritt wird als Punycode-Konvertierung bezeichnet.

3. Übermittlung an den DNS-Resolver: Der Browser sendet die umgewandelte ASCII-Version der URL an den DNS-Resolver des Betriebssystems.

4. DNS-Auflösung: Der DNS-Resolver löst die URL in die entsprechende IP-Adresse auf, indem er die DNS-Anfragen an die zuständigen DNS-Server sendet.

5. Abruf der Webseite: Nachdem die IP-Adresse der Webseite ermittelt wurde, sendet der Browser eine Anfrage an den Webserver, um den Inhalt der Webseite abzurufen.

6. Anzeige der Webseite: Der Browser empfängt die Daten von der Webseite und rendert sie anschließend im Browserfenster, sodass Sie die Webseite betrachten können.


#### 5. IDNs können verwendet werden, um sogenannte Homografische Phishing Attacks durchzuführen. Erklären Sie das Verfahren

Homografische Phishing-Angriffe nutzen die Ähnlichkeit von Zeichen aus verschiedenen Alphabetsätzen, um gefälschte URLs zu erstellen, die dem Original ähnlich sehen.


#### 6. Wie können Sie diese Art von Phishing verhindern?

1. Überprüfen Sie sorgfältig die URL.
2. Verwenden Sie Lesezeichen für Websites.
3. Halten Sie Ihre Sicherheitssoftware aktuell.
4. Sensibilisieren Sie Benutzer und bieten Sie Schulungen an.
5. Aktivieren Sie Phishing-Filter in E-Mails und Browsern.
6. Verwenden Sie Punycode-Anzeigen für IDNs in Ihrem Browser, falls verfügbar.