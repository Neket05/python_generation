# Как работают юнит тесты?

В Python есть стандартная библиотека для юнит тестирования, но более удачной является библиотека pytest. 
Для ее установки удобнее всего создать новую среду conda (установка conda на ubuntu:
https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html)


```bash
# создать новую среду с именем tests
conda create -yn tests
# активировать среду с имененем tests
conda activate tests
# установить в ней dependencies
pip3 install -r requirements.txt
```

После этого необходимо перейти в папку, где живут тесты и выполнить команду pytest. Тесты будут найдены и распознаны автоматически, главное, чтобы классы, методы и функции имели в названии слово Test / test.

```bash
# перейти в папку с тестами
cd 2_week
# запустить тесты
pytest
```