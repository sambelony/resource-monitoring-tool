# ENG:

**Task:**

Write a program that will launch a process and collect the following statistics about it at a specified time interval:

- CPU load (in percent);

- Memory consumption: Working Set and Private Bytes (for Windows systems) or Resident Set Size and Virtual Memory Size (for Linux systems);

- Number of open handles (for Windows systems) or file descriptors (for Linux systems).

Collection of statistics should be executed all the time the process is running. The path to the file to be run and the statistics collection interval must be specified by the user. The collected statistics must be saved to disk. The presentation of the data should further allow the use of these statistics for automated graphing of resource consumption.

**Instructions:**
Get instructions from the terminal (must be in the folder with the `.py` file):
`python rmonitoring.py --help `

1. Argument `--process` - the name of the process with the extension, or the full path to the file.
2. Argument `--interval` - statistics collection interval, in seconds.
3. Argument `--graph` - is responsible for creating graphs, whether it is necessary to save (Y or N) graphs built according to the data from the created `.csv` file.

**Program launch example:**
`python rmonitoring.py --process notepad.exe --interval 1 --graph y` - to run the notepad.exe process, data collection interval is 1 second, graphs will be built and saved in `.png` format to the directory with the `rmonitoring file .py`.

**Important:**
The program will require additional libraries that are specified in `requirements.txt`.
To install required libraries: `pip install -r requirements.txt`

# RUS:

**Задача:**

Написать программу, которая будет запускать процесс и с указанным интервалом времени собирать о нём следующую статистику:

- Загрузка CPU (в процентах);

- Потребление памяти: Working Set и Private Bytes (для Windows-систем) или Resident Set Size и Virtual Memory Size (для Linux-систем);

- Количество открытых хендлов (для Windows-систем) или файловых дескрипторов (для Linux-систем).

Сбор статистики должен осуществляться всё время работы запущенного процесса. Путь к файлу, который необходимо запустить, и интервал сбора статистики должны указываться пользователем. Собранную статистику необходимо сохранить на диске. Представление данных должно в дальнейшем позволять использовать эту статистику для автоматизированного построения графиков потребления ресурсов.

**Инструкции:**
Получить инструкции из терминала (необходимо находиться в папке с файлом `.py`):
`python rmonitoring.py --help  `

1. Аргумент `--process` - название процесса с расширением, либо полный путь до файла.
2. Аргумент `--interval` - интервал сбора статистики, указывается в секундах.
3. Аргумент `--graph` - отвечает за создание графиков, необходимо ли сохранять (Y or N) построенные по данным из созданного `.csv` файла графики.

**Пример запуска программы:**
`python rmonitoring.py --process notepad.exe --interval 1 --graph y` - для запуска процесса notepad.exe, интервал сбора 1 секунда, графики будут построены и сохранены в формате `.png` в дерикторию с файлом `rmonitoring.py`.

**Важно:**
Для работы программы потребуются дополнительные библиотеки, которые указаны `requirements.txt`.
Чтобы установить необходимые библиотеки: `pip install -r requirements.txt`

