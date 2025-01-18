# RAG-pipeline for analyzing Tarot books

## Prerequisites

Create .env file in the root of the project and add the keys for YaGPT API:

```
YANDEX_FOLDER_ID=
YANDEX_API_KEY=
```
Tutorial on how to get these keys: [Habr](https://habr.com/ru/articles/780008/)

## Run

```
python main.py
```

## Comments

This pipeline is designed to work with books in both PDF and TXT formats. However, my experiments with PDF files weren't very successful (probably because of the complexity of the formatting). 

Also, I used [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) for embeddings and retrieval initially. This model was not very successful in semantic search due to the specifics of the textbooks' structure and large paragraphs of text. Then I switched to `Yandex GPT` and it worked much better.

`Yandex GPT` is a great model for language modelling in Russian, so example questions are in Russian. However, an original text is in English and random questions are better to be asked in English. To be honest, I am surprised that the retrieval model works well with Russian questions ;)


## Examples of work


<font color="red">**Question:**</font> Как связаны Арканы Солнца и Луны?

<font color="green">**Response:**</font> В этом тексте описывается, как Арканы Солнца и Луны связаны с этапами познания себя. После встречи со страхами (Аркан Луна) человек переходит к новому этапу духовного развития и творческой реализации, словно видит свет мира после тьмы (Аркан Солнце).

Также указано, что после столкновения с «тёмной ночью души» под светом Луны появляется обновлённая энергия и начинается путь к свету, который приводит к Аркану Солнце.

--------------------------------------------------------------------------------

<font color="red">**Question:**</font> Какой эзотерический смысл у Аркана Королевы?

<font color="green">**Response:**</font> У аркана Королевы Мечей есть несколько значений, которые зависят от положения карты в раскладе и её аспектов.

**Если карта в прямом положении**, она означает, что личность обладает мудростью, дальновидностью, проницательностью, способностью видеть общую картину ситуации и находить истину. Также этот аркан может говорить о женщине или мужчине, который твёрдо стоит на своём пути в жизни. В качестве «вашей» карты Королева Мечей предлагает быть решительным и стойким. 

**Перевёрнутая карта** может указывать на нечестность или неверность со стороны близкого человека. Как личность, перевёрнутая Королева имеет навязчивые наклонности, борется за внимание и хочет всегда поступать по-своему. Она истощает окружающих, поэтому лучше не способствовать её прихотям. Такая личность может находить оправдания плохому поведению или несправедливому нападению на себя. Одной из причин инверсии Королевы может быть сильный стресс — она не осознаёт, насколько необоснованными стали её требования.


Чакры Королевы: сердечная, третий глаз и солнечное сплетение, символизирующие любовь, интуицию и мудрость. Это аркан с умственными способностями, который позволяет анализировать психологический аспект ситуаций. Королева Мечей символизирует тип человека, стремящегося к независимости и не склонного к эмоциональной или финансовой поддержке партнёров.  

--------------------------------------------------------------------------------

<font color="red">**Question:**</font> Какой аркан отвечает за неожиданные перемены?

<font color="green">**Response:**</font> В представленном тексте есть фрагмент про аркан «Маг», который, помимо прочего, означает новое начало в карьере. Также упоминается аркан «Дурак», символизирующий перемены и новое начинание.

Поэтому можно сказать, что у карт Таро с названием «Маг» или «Дурак» (или «Шут») есть значение, связанное с неожиданными переменами.

