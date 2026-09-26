#!/usr/bin/env python3
"""Create the Russian quick-start / defense guide (requires reportlab)."""
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image, KeepTogether
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT
import csv
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/DAA_Assignment1_Guide_RU.pdf'
FONTDIR=Path('/usr/share/fonts/truetype/dejavu')
pdfmetrics.registerFont(TTFont('DV',str(FONTDIR/'DejaVuSans.ttf')))
pdfmetrics.registerFont(TTFont('DVB',str(FONTDIR/'DejaVuSans-Bold.ttf')))
pdfmetrics.registerFont(TTFont('DVM',str(FONTDIR/'DejaVuSansMono.ttf')))
pdfmetrics.registerFontFamily('DV',normal='DV',bold='DVB',italic='DV',boldItalic='DVB')
NAVY=colors.HexColor('#17324D'); TEAL=colors.HexColor('#087E8B'); PALE=colors.HexColor('#EDF4F8')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyRU',fontName='DV',fontSize=10,leading=15,spaceAfter=9,textColor=NAVY))
styles.add(ParagraphStyle(name='TitleRU',fontName='DVB',fontSize=27,leading=33,spaceAfter=16,textColor=NAVY))
styles.add(ParagraphStyle(name='HeadingRU',fontName='DVB',fontSize=18,leading=24,spaceAfter=14,textColor=NAVY))
styles.add(ParagraphStyle(name='SubRU',fontName='DVB',fontSize=11,leading=16,spaceBefore=8,spaceAfter=7,textColor=TEAL))
styles.add(ParagraphStyle(name='CodeRU',fontName='DVM',fontSize=8,leading=12,backColor=PALE,borderPadding=9,spaceBefore=5,spaceAfter=14))
styles.add(ParagraphStyle(name='SmallRU',fontName='DV',fontSize=8.6,leading=12,spaceAfter=7,textColor=NAVY))
story=[]
def p(s,style='BodyRU'): story.append(Paragraph(s,styles[style]))
def h(s): p(s,'HeadingRU')
def sub(s): p(s,'SubRU')
def code(s): p(escape(s).replace('\n','<br/>'),'CodeRU')
def gap(n=6): story.append(Spacer(1,n))
def page(): story.append(PageBreak())
def table(rows,widths):
 t=Table([[Paragraph(str(x),styles['SmallRU']) for x in row] for row in rows],colWidths=widths,hAlign='LEFT')
 t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),PALE),('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,0),1,TEAL),('LINEBELOW',(0,1),(-1,-1),.35,colors.HexColor('#D7E2EC')),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
 story.append(t);gap(10)

p('DAA / ASSIGNMENT 1','SubRU')
p('Запуск, сдача<br/>и защита проекта','TitleRU')
p('Практическое руководство к проекту<br/><b>Divide-and-Conquer Algorithm Analysis</b>')
gap(7)
p('В комплекте: четыре алгоритма на Java, 24 692 успешные проверки, 672 строки измерений, четыре графика, README на английском и последовательная история Git.')
sub('1. Открой правильную папку')
p('Полностью распакуй ZIP. Открой папку <b>assignment1-divide-and-conquer</b>: внутри должны находиться pom.xml, README.md, src, tests, docs и results. Команды ниже выполняются из этой папки.')
sub('2. Проверь Java')
code('java -version')
p('Нужен <b>JDK 17 или новее</b>. JDK включает компилятор; одного старого JRE недостаточно. В IntelliJ IDEA можно открыть pom.xml и выбрать JDK 17.')
sub('3. Запусти на Windows')
code('powershell -ExecutionPolicy Bypass -File scripts/run.ps1 demo\npowershell -ExecutionPolicy Bypass -File scripts/run.ps1 test')
p('Первая команда показывает работу алгоритмов. Вторая должна закончиться строкой:')
code('ALL TESTS PASSED: 24692 checks')
p('На Linux, macOS или в Git Bash используй <b>bash scripts/run.sh demo</b> и <b>bash scripts/run.sh test</b>. Прямой Java/Bash-запуск проверен; Maven и PowerShell в среде измерений отсутствовали.','SmallRU')

page();h('Как сдать через GitHub')
p('По условию сдаётся <b>ссылка на репозиторий</b>. Сам архив или PDF не заменяет эту ссылку. Публикация в твоём аккаунте пока не выполнена.')
sub('1. Создай пустой репозиторий')
p('На GitHub создай assignment1-divide-and-conquer. Не добавляй новый README, лицензию или .gitignore при создании: локальный проект уже содержит нужные файлы. Выбери видимость, при которой преподаватель получит доступ.')
sub('2. Перенеси проект вместе с историей')
p('Нужен установленный Git. Замени YOUR_USERNAME своим логином и выполни команды из папки проекта:')
code('git status\ngit log --oneline --reverse\ngit remote add origin https://github.com/YOUR_USERNAME/assignment1-divide-and-conquer.git\ngit push -u origin main\ngit push origin v1.0')
p('При запросе авторизации войди через браузер или настроенный менеджер учётных данных. Не требуется передавать пароль в переписку.')
sub('3. Проверь страницу перед отправкой')
p('На GitHub должны открываться исходники, тесты, README, графики и CSV. Проверь список коммитов. Затем отправь в LMS адрес страницы репозитория.')
sub('Если история не распозналась')
p('Сначала проверь рабочую папку и полноту распаковки. В архиве есть резервный <b>assignment1-history.bundle</b>. Из папки с этим файлом можно восстановить репозиторий:')
code('git clone assignment1-history.bundle assignment1-restored')
p('Дальнейшие команды подключения origin и отправки приведены в docs/SUBMISSION_RU.md. Загрузка через Upload files не переносит существующую историю Git.','SmallRU')
p('Коммиты отражают реальные этапы подготовки в текущей сессии; даты и авторство не изменялись. Для своих дальнейших изменений используй собственные имя и почту Git.','SmallRU')

page();h('Четыре алгоритма: основная идея')
sub('MergeSort')
p('Делим массив пополам, сортируем половины и сливаем их. На каждом уровне суммарная работа линейная, уровней порядка log n. Один вспомогательный массив переиспользуется. Части длиной не больше 24 обрабатываются сортировкой вставками.')
p('<b>Что показать:</b> создание auxiliary один раз, условие INSERTION_CUTOFF и цикл линейного слияния в MergeSorter.java.')
sub('QuickSort')
p('Случайный pivot делит массив на области меньше, равно и больше него. Равная область уже готова. Для меньшей части выполняется рекурсивный вызов, большая обрабатывается циклом. Повторы не создают цепочку бесполезных разбиений.')
p('<b>Главная мысль:</b> стек O(log n) даже при плохих pivot, но худшее время остаётся O(n²). Маленький стек и небольшое число операций - разные свойства.')
sub('Deterministic Select')
p('Ищем элемент ранга k, не сортируя весь массив. Сортируем группы по пять, собираем их медианы и находим медиану медиан. После разбиения продолжаем только в части с нужным k. Индексация начинается с нуля.')
p('<b>Пример:</b> для [9, 1, 7, 3, 5] и k=2 ответ 5. В экспериментах используется k=n/2 - верхний центральный элемент при чётной длине.')
sub('Closest Pair')
p('Сортируем точки по x, решаем левую и правую половины. Проверяем полосу около границы, где может лежать более близкая пересекающая пара. Точки в полосе идут по y; достаточно не более семи следующих соседей.')
p('<b>Ключевая деталь:</b> порядок по y поддерживается слиянием. Сортировка полосы заново на каждом уровне дала бы O(n log² n).')

page();h('Сложность и её объяснение')
table([['Алгоритм','Время','Доп. память'],['MergeSort','Θ(n log n)','O(n)'],['QuickSort','Ожидаемое Θ(n log n),<br/>худшее Θ(n²)','O(log n)'],['Select','Худшее Θ(n)','O(log n)'],['Closest Pair','Θ(n log n)','O(n)']],[130,225,145])
sub('Master Theorem: MergeSort и Closest Pair')
code('T(n) = 2T(n/2) + Theta(n)\na = 2, b = 2, log_b(a) = 1')
p('Нерекурсивная работа совпадает по порядку с n в степени log_b(a). Это второй случай Master Theorem: результат Θ(n log n). Для Closest Pair первоначальная сортировка по x тоже укладывается в O(n log n).')
sub('Почему Select имеет линейную гарантию')
p('Примерно половина медиан групп находится по каждую сторону pivot. Каждая подходящая полная группа даёт три значения с нужной стороны. Поэтому можно отбросить около 3n/10 значений, с постоянной поправкой из-за округления.')
code('T(n) <= T(n/5) + T(7n/10) + O(n)\n1/5 + 7/10 = 0.9 < 1')
p('Обычная Master Theorem напрямую не применяется: подзадачи разных размеров. В объяснении Akra-Bazzi показатель p удовлетворяет (1/5)^p + (7/10)^p = 1. Он лежит между 0 и 1; линейная работа вне рекурсии даёт итог O(n). Полный вывод приведён в README.')
sub('Почему QuickSort может оставаться квадратичным')
p('При постоянно крайних pivot остаётся задача размера n-1: T(n)=T(n-1)+Θ(n). Сумма n+(n-1)+... даёт Θ(n²). Цикл для большой части экономит стек, но не убирает эту работу.')

page();h('Вопросы на защите')
for q,a in [
('Как проверялась правильность?','Сортировки и Select сравниваются с Arrays.sort. Closest Pair сравнивается с полным перебором для небольших наборов, включая n=2000. Большой набор проверяется также на известном расстоянии.'),
('Зачем System.nanoTime()?','Для измерения прошедшего времени: берём разницу значений до и после алгоритма. Генерация входа и эталонная проверка не входят в этот интервал.'),
('Почему есть прогрев JVM?','Виртуальная машина компилирует часто используемые участки во время работы. Без прогрева первые запуски могут быть несопоставимы с последующими.'),
('Почему семь повторов и медиана?','Один запуск может замедлиться из-за GC или других процессов. Медиана уменьшает влияние единичного выброса; исходные семь результатов сохранены в CSV.'),
('Что означает seed?','Он фиксирует последовательность псевдослучайных чисел. Данные и pivot воспроизводятся; время может отличаться.'),
('Что происходит с пустым входом?','Сортировки завершаются без действий. Select отклоняет недопустимый k. Closest Pair сообщает об отсутствии пары.'),
('Что с повторяющимися значениями?','QuickSort и Select используют отдельную область равных pivot. Совпадающие точки разрешены: их расстояние равно нулю.'),
('Что можно улучшить дальше?','Добавить отдельные процессы JVM для измерений, подобрать cutoff экспериментально и сравнить версии со счётчиками и без них. Это планы, а не выполненные части.')]:
 p('<b>'+q+'</b><br/>'+a)
p('Подробные ответы и короткое вступление на английском находятся в <b>docs/DEFENSE_RU.md</b>. Перед защитой обязательно проследи хотя бы один пример вручную для каждого алгоритма.','SmallRU')

page();h('Результаты и финальная проверка')
p('Для случайного входа из 300 000 элементов/точек в сохранённой среде получены следующие медианы семи запусков:')
summary={(r['algorithm'],r['input_type'],int(r['n'])):r for r in csv.DictReader((ROOT/'results/summary.csv').open())}
rows=[['Алгоритм','Время, мс','Макс. глубина']]
for a in ['MergeSort','QuickSort','Select','ClosestPair']:
 r=summary[a,'RANDOM',300000];rows.append([a,f"{float(r['median_ms']):.3f}",r['max_depth']])
table(rows,[185,155,160])
p('На 2000 случайных точек: быстрый поиск около 0,702 мс, полный перебор около 35,550 мс. Наблюдаемое ускорение - примерно 50,7 раза. Это результат конкретного запуска, а не обещание такой скорости на любом компьютере.')
sub('Что уже покрыто по критериям')
table([['Раздел','Вес','Где смотреть'],['Алгоритмы','40%','src/daa'],['Реализация и эксперименты','20%','Experiment.java, results'],['Тестирование','10%','AlgorithmTests.java, tests.txt'],['README и изображения','15%','README.md, docs'],['Структура и история Git','15%','Локальная история готова;<br/>нужна публикация на GitHub']],[195,55,250])
sub('Перед сдачей')
p('1. Запусти demo и test на своём компьютере.<br/>2. Сделай собственные скриншоты терминала, если преподавателю нужны именно снимки экрана. В комплекте - изображения реального сохранённого вывода.<br/>3. Перечитай Reflection и поправь его под свой реальный опыт.<br/>4. Проверь графики и доступ к репозиторию.<br/>5. Отправь ссылку GitHub в LMS.')
p('Оценку выставляет преподаватель. Этот комплект закрывает техническую подготовку; итог зависит также от публикации, требований курса и того, насколько уверенно ты объяснишь решение.','SmallRU')

def footer(c,doc):
 c.setStrokeColor(colors.HexColor('#D7E2EC'));c.line(47,46,548,46)
 c.setFont('DV',8);c.setFillColor(colors.HexColor('#657D92'))
 c.drawString(47,31,'DAA Assignment 1  |  Руководство к проекту')
 c.drawRightString(548,31,str(doc.page))

doc=SimpleDocTemplate(str(OUT),pagesize=(595.28,841.89),leftMargin=47,rightMargin=47,topMargin=44,bottomMargin=61,title='DAA Assignment 1 - Запуск, сдача и защита',author='Project preparation')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(OUT)
