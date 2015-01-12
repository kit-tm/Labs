Material zum SDN-Laborversuch und dem dazugehörigen Übungsblatt. 

Im Ordner pox befindet sich eine unmodifizierte Version des POX-Controllers 
(https://github.com/noxrepo/pox, aktualisiert am 12. Januar 2015, Commit 
bab636bc89584b3bb2baaa5bc766be82fb81d1b2). Die für das Übungsblatt (und den Versuch) 
verwendeten Dateien finden Sie im Unterordner ext. Der Ordner pox/ext muss auf den
Ordner ext zeigen (z.B. via ln -s)

~~~~~~~~~~~~~~~~~~~~~~~~~~
WICHTIG: Wenn Sie NICHT in der von uns vorbereiteten virtuellen Maschine arbeiten und
trotzdem die im Übungsblatt referenzierten Aliase verwenden wollen, 
müssen sie den Pfad ganz oben in der Datei ext/sdn_aliases.sh an ihr System anpassen!
Außerdem müssen Sie diese Datei in ihrer ~/.bashrc einbinden.
~~~~~~~~~~~~~~~~~~~~~~~~~~

Danach stehen Ihnen dann die folgenden Befehle in der Shell zur Verfügung, mit denen sich der POX-Controller
und die Mininet-Testumgebung aufrufen lässt. Die dabei geladenen (zusätzlich zu den von POX bereitgestellten) 
Module befinden sich alle im Ordner (pox/ext).

	controller 		- startet Controller für den Lab-Versuch, zeigt auf pox/ext/aufgabe0.py
	controller1 	- startet den Controller für Aufgabe 1 aus dem Übungsblatt (pox/ext/aufgabe1.py)
	controller2 	- wie oben, zeigt auf pox/ext/aufgabe2.py
	controller2.2 	- wie controller2, nur das zusätzlich die Standardlogausgaben unterdrückt werden

Im Lab und für Aufgabe 1 (silent arp) verwenden wir Szenario 1, für Aufgabe 2
(multi switch) verwenden wir Szenario 2. Auch hierfür gibt es passende Aliase:

	mininet 	- startet Mininet Szenario 1 (Lab und Aufgabe 1)
	mininet1 	- wie mininet
	mininet2 	- startet Mininet Szenario 2 (nur Aufgabe 2)
	 
	 
	 
