# Henlo world

test 0.2 here

## Testing sections

Here I'm testing something

### Did it work?

The title above should be indented in the right-side bar

#### Yes, it did

## Features

- Create new project
    - Main parameters
    - Metadata
- Generate new data for existing project
    - Folder structure
    - Metadata
- Introduce errors in the data
- How to store data: DBs (SQLite, PostgreSQL), files (parquet, csv, txt)
- How to use it: Visualisation, monitoring, dashboards, reports

---

Whatever system I come up with it needs to respect some constaints:

 - The driving force of a sale is the willingness of a potential customer to **change** (use two examples: company using agroptima, me buying a new carbon bike although I already have one). This means that the utility of what our fake company offers surpasses its cost. Cost is not only monetary. Utility is also composed of different parts [^2].
 - The system needs to represent this process of change. It should not be "seen" in the generated data, but should be held somewhere to be used when respecting established trends (explain established trends)
 - This means that the generated data, when analysed at any given point in time, should reflect a realistic scenario that represents some state of change.

 ---

 - This system, therefore will be based on 3 pilars: trends, state, and interaction.
    1. High-level and low-level trends will be established, respected, and modified.
    2. State values will represent preferences and moments in time, in terms of decision-making for all users. Point-based system, threshold value <-- These through time are trends.
    3. There will be an action, interaction (game-theory?), and reaction to fake company initiatives and user initatives.

The project will be defined if it serves consumers, businesses, or both. After it is created, this can be modified (upscaling to only businesses or offering cheaper consumer options from only B2B).


## Code test

```python
for i in range(10):
    print(i)
```

## Footnote test & emoji! :smile:

This text[^1] is interesting.

## Roadmap

* [x] this task is done
* [ ] this one isn't.

## Maths

I can do some maths $a + b < c$ inline.

$$ a + c^2 < b^7 $$


First Header | Second Header | Third Header
:----------- |:-------------:| -----------:
Left         | Center        | Right
Left         | Center        | Right


[^1]: See more in [here](https://www.google.com){:target="_blank"}

[^2]: Link to Pigneur something book, value design proposition thing.