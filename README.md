##Тестовое задание

####Стек: 
* Python >3.7, behave, selenium, sqlite3.

####Исходные данные:
 
* stocks (файл sqlite)
    
####Описание задачи:

Вам необходимо написать тестовый сценарий, который собирает информацию (название, цена)
на [сайте](https://ru.investing.com/) о российских акциях, цена которых изменилась
на определенный % в большую сторону. Цена для расчета % роста цен, хранится в базе данных stocks
(данные по акциям находятся по следующему пути Котировки->Акции->Россия).
При переходе к  списку акций проверять отсутствие / присутствие заголовка Россия – акции.
После сбора информации сценарий должен выгрузить собранные данные в файл report.json

####Важное замечание:

Запрещается использовать прямые ссылки на необходимые страницы,
использовать только итерации по web-сайту. 

Описание остальных частей смотри тут:
    
    https://gitlab.com/KhayFix/behave_selenium
    
Все что требуется для работы теста запустить файл:

    test_1.feature