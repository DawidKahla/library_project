Aplikacja webowa pozwalająca prowadzić ewidencje biblioteki domowej.

W celu zapewnienia poprawnego działania aplikacji należy upewnić się, że na urządzeniu zainstalowane są wersje odpowiednich modułów, zgodnie z plikiem requirements.txt, co można zrobić przy pomocy polecenia: "pip install -r requirements.txt" Natępnie należy utworzyć lokalną bazę danych zgodną z ostatnią migracją poleceniem: "flask db upgrade".

Aplikację można uruchomić poprzez uruchomienie pliku start.bat i wpisanie "http://127.0.0.1:5000/books/" lub "http://127.0.0.1:5000/hires" w adres dowolnej przeglądarki internetowej.