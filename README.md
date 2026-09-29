# Лабораторная работа 1. Сбор параметров операционной системы

# Описание

Скрипт `lab1.py` определяет, в какой операционной системе он запущен,
собирает ключевые параметры текущей системы и сохраняет результат
в файл `result.json`.

Скрипт работает кроссплатформенно: на Windows, Linux.
Используются только стандартные модули Python — внешние зависимости не требуются.

## Используемые модули
'json', 'platform', 'sys', 'os' , 'getpass' - все стандартные

## Собираемые параметры

- `system` — полное имя системы (`platform.platform()`)
- `os_family` — семейство ОС: Windows / Linux (`platform.system()`)
- `release` — версия ОС (`platform.release()`)
- `version` —  внутренняя сборка ОС (`platform.version()`)
- `processor` — модель процессора (`platform.processor()`)
- `machine` — архитектура процессора, его "семейство"  (`platform.machine()`)
- `architecture_bits` — разрядность системы: 64bit / 32bit (`platform.architecture()`)
- `hostname` — имя компьютера в сети (`platform.node()`)
- `username` — имя пользователя, под которым запущен скрипт (`getpass.getuser()`)
- `python_version` — версия Python, которой запущен скрипт (`platform.python_version()`)
- `interpreter_path` —  полный путь к интерпретатору, которым запущен скрипт (`sys.executable`)
- `cpu_count` — число логических ядер процессора (`os.cpu_count()`)

## примеры работы программы
## на Windows:

<img width="1108" height="396" alt="image" src="https://github.com/user-attachments/assets/8ede7f0f-9cd4-4663-b55d-e082b783a82c" />

## на Linux:

<img width="763" height="315" alt="image" src="https://github.com/user-attachments/assets/6e3098d0-633a-4fc2-accb-0316e5c56b57" />
