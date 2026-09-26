# Как запустить и сдать Assignment 1

## Что уже готово

Четыре алгоритма на Java, автоматические тесты, 672 строки настоящих замеров, четыре графика, README на английском, изображения вывода и история Git. Все 24 692 проверки завершились успешно. Итоговая оценка зависит от преподавателя, требований к самостоятельной работе и защиты.

Сдавать по условию нужно **ссылку на репозиторий GitHub**, а не ZIP или PDF. Публикация в аккаунте пока не выполнена. Архив сохраняет историю подготовки: коммиты создавались последовательно при работе, без изменения дат и авторства.

## 1. Открой проект

Распакуй весь архив. Рабочая папка называется `assignment1-divide-and-conquer`; в ней находятся `pom.xml`, `README.md`, `src`, `tests`, `docs` и `results`.

Нужен JDK 17 или новее. Проверь в PowerShell:

```powershell
java -version
```

Открой терминал именно в папке проекта. Через Проводник можно открыть папку, нажать на строку пути, написать `powershell` и нажать Enter.

## 2. Запусти демонстрацию и тесты

```powershell
powershell -ExecutionPolicy Bypass -File scripts/run.ps1 demo
powershell -ExecutionPolicy Bypass -File scripts/run.ps1 test
```

Вторая команда должна закончиться строкой:

```text
ALL TESTS PASSED: 24692 checks
```

Для Linux/macOS или Git Bash:

```bash
bash scripts/run.sh demo
bash scripts/run.sh test
```

В IntelliJ IDEA можно открыть `pom.xml` как проект, выбрать JDK 17 и запустить `daa.Main`; затем запустить `daa.AlgorithmTests` из папки `tests`. У тестов есть обычный метод `main`, JUnit не требуется. Тесты также подключены к фазе Maven `test`.

## 3. Разберись с результатами

`results/results.csv` содержит исходные измерения. `results/summary.csv` - медианы, квартили, минимумы, максимумы и счётчики. `docs/EXPERIMENT_TABLES.md` показывает все таблицы. Графики уже вставлены в README.

Чтобы получить измерения на своём ноутбуке:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/run.ps1 experiment
```

Запуск заменит `results.csv` и `environment.txt`. Для согласованного отчёта после него нужно заново построить графики и обновить числовые таблицы и выводы в README: автоматически меняются только CSV, графики и `docs/EXPERIMENT_TABLES.md`, основной README не переписывается.

Для перегенерации изображений вывода сначала сохрани соответствующие логи:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/run.ps1 demo | Tee-Object -FilePath results/demo.txt
powershell -ExecutionPolicy Bypass -File scripts/run.ps1 test | Tee-Object -FilePath results/tests.txt
powershell -ExecutionPolicy Bypass -File scripts/run.ps1 experiment | Tee-Object -FilePath results/experiment.txt
python -m pip install -r scripts/requirements.txt
python scripts/make_report_assets.py
```

Изображения в `docs/screenshots` воспроизводят реальный сохранённый вывод. Для буквальных скриншотов экрана запусти программу и тесты на своём компьютере, нажми Win+Shift+S и замени соответствующие PNG. Следи, чтобы были видны команды и итоговая строка тестов.

## 4. Опубликуй репозиторий с историей

Установи Git, если команда `git --version` не работает. На GitHub создай **пустой** репозиторий `assignment1-divide-and-conquer`: не добавляй при создании README, лицензию или `.gitignore`, они уже есть локально. Выбери доступность согласно требованиям преподавателя.

В папке распакованного проекта выполни:

```bash
git status
git log --oneline --reverse
git remote add origin https://github.com/YOUR_USERNAME/assignment1-divide-and-conquer.git
git push -u origin main
git push origin v1.0
```

Замени `YOUR_USERNAME` на свой логин GitHub. При запросе авторизации пройди вход через браузер/настроенный менеджер учётных данных. Обычный пароль аккаунта для Git HTTPS не используется.

Если `git status` сообщает, что это не репозиторий, проверь, что открыта правильная папка и архив извлечён полностью. Внешний файл `assignment1-history.bundle` содержит резервную копию истории. Из папки, где он лежит, можно восстановить проект в новую папку:

```bash
git clone assignment1-history.bundle assignment1-restored
cd assignment1-restored
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/assignment1-divide-and-conquer.git
git push -u origin main
git push origin v1.0
```

Не загружай только исходники через «Upload files», если хочешь сохранить историю: это создаст новые коммиты загрузки вместо переноса существующих. Не нужно повторно выполнять `git init` или изменять авторство прошлых коммитов.

Для **своих будущих изменений** настрой имя и почту Git и добавляй осмысленные коммиты:

```bash
git config user.name "Ваше имя"
git config user.email "Ваша почта GitHub"
git add README.md docs
git commit -m "docs: add my reflection and local screenshots"
git push
```

Выполняй последние команды после реальных изменений, а не для создания пустой истории.

## 5. Перед отправкой преподавателю

1. Открой страницу GitHub: должны отображаться папки, README, таблицы и все изображения.
2. Убедись, что преподаватель имеет доступ к репозиторию.
3. Перечитай Reflection и отредактируй его под то, что ты действительно поняла и с чем работала.
4. Просмотри `docs/DEFENSE_RU.md`, особенно различие между временем работы и глубиной рекурсии.
5. Отправь в LMS ссылку вида `https://github.com/твой-логин/assignment1-divide-and-conquer`.

Официальные инструкции: [загрузка локального проекта](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github), [учётные данные Git](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git).
