# goit-algo-hw-04

## Порівняння Алгоритмів Сортування в Python

Цей проект досліджує ефективність трьох різних алгоритмів сортування: сортування злиттям, сортування вставками та Timsort (вбудований алгоритм сортування Python).
Ми виміряли час виконання кожного алгоритму на різних наборах даних, щоб емпірично порівняти їх продуктивність.

### Methodology
- Реалізовано алгоритми сортування злиттям і сортування вставками.
- Використано вбудовану функцію sorted() Python, яка застосовує алгоритм Timsort.
- Проведено вимірювання часу виконання кожного алгоритму на маленьких (100 елементів), середніх (1000 елементів) і великих (10000 елементів) наборах випадкових даних.
- Для вимірювань використано модуль timeit.

### Results
- Сортування вставками показало найнижчу продуктивність на великих наборах даних, що відповідає його теоретичній складності O(n2).
- Сортування злиттям було ефективніше, ніж сортування вставками, завдяки складності O(n log n), але все ще було повільніше за вбудоване сортування.
- Timsort продемонстрував найкращі результати на всіх типах наборів даних, що підтверджує його ефективність та адаптивність.

### Висновки

Експеримент підтвердив, що вибір алгоритму сортування має значний вплив на продуктивність програми, особливо при роботі з великими обсягами даних.
Результати підкреслюють переваги використання оптимізованих та адаптивних алгоритмів, таких як Timsort, для ефективної обробки даних.