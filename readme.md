## Opis

Program do tekstu artykułu wstawia tagi html oraz tag na obraz wraz z przykładowym promptem


## Działanie

1. Program pobiera tekst artykułu z pliku article.txt
2. Wysyła za pomocą API tekst artykułu wraz z promptem
3. Program otrzymuje tekst z tagami html wraz z miejscem na obraz
4. Następnie wysyła ten tekst aby w miejsca na obrazy wstawić tag z obrazem
5. Program otrzymuje odpowiedź i zapisuje ją w plikut artykul.html


## Użycie

Jako zmienną środowiskową ustawiamy nasz klucz api z openai
Dwie możliwość:
1. Miejsce do edycji można znaleźć w /.idea/workspace.xml
W tym pliku wstawiamy poniższy kod w miejscu bezpośrednio pod "<env name="PYTHONUNBUFFERED" value="1"/>"
W miejsce * należy wpisać nasz klucz api:
<env name="OPENAI_API_KEY" value="*"/>
2. Bezpośrednio w edytorze IDE 


## Nota końcowa

Mam świadomość, że to repozytorium jest bardzo wybrakowane i z błędami. Zapomniałem, że trzeba to wstawić na githuba - robię to w ostaniej godzinie a nigdy nie korzystałem z wstawiania projektów do repozytorium. Jest to do nauczenia - nie będzie z tym problemu.

Więcej informacji w pliku Wybory.txt

