# Опис
Репозиторій містить додаткові матеріали до статті.


## parcels_water_check.py
Програма завантажує данi з файлiв parcels_small.geojson та water˙geojson, якi мiстять полiгони
земельних дiлянок та водної поверхнi вiдповiдно, знаходить всi дiлянки, якi перетинаються з водними
об’єктами, та виводить результати.

Вхiднi данi:
* файл з геометрiєю дiлянок
* файл з геометрiєю водних об’єктiв

Вихiднi данi:
* Вивiд на екран перетинiв дiлянок з водними об’єктами
* (Опцiонально) Збереження результатiв у файл intersections.geojson

## parcels_index_check.py
Програма завантажує данi з файлу parcels.csv, конвертує геометрiю з текстового формату, завантажує данi з файлу index_db.gpkg, виконує просторове об’єднання для знаходження перетинiв
дiлянок, та перевiряє вiдповiднiсть полiв zona та kvart.

Вхiднi данi:
* файл з даними про дiлянки, включаючи геометрiю у текстовому форматi
* файл з геометрiєю для перевiрки перетинiв
Вихiднi данi:
* Вивiд на екран попереджень про невiдповiднiсть полiв zona та kvart
* Вивiд на екран перетинаючих дiлянок для перевiрки

