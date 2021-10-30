#### bugs

- [x] won't parse fen if there are empty spaces at the start
- [x] second position on card not displayed; duplicates earlier position

#### features

- [ ] set board size per card
- [x] single tag; make it simpler to type e.g. fen:[fen string here]. "Tags" are 'fen::' and '.'
- [ ] Also show board image during browsing? Can this be done?
- [ ] add test functions!

#### more options

- quiet
- enabled
- timer
- auto grade

#### simple tags

fen::[fen string]::[optional attributes].
[fen string] := valid fen string
[optional attributes] := attribute-value pair; ... 

#### v2: xml markup
<?xml version="1.0">
<fen size=400 flip="auto" mover="true" script="future" style="css">
    <record>fen string here</record>
    <caption>Mate in two</caption>
    <solution>1. Nc7# </solution>
    <tags>fork deflection</tags>
    <rating>5</rating>  ??
    <elo>2000</elo>
</fen>

see https://docs.python.org/3/library/markup.html

Attributes
- size=400
- flip=auto
- mover=true
- script=future
- style=css
- time=30
- good=10 
- auto=true
- sides=true # show white/black lines on white/black sides of the board

Attributes override general options

#### interactivity

- be able to move pieces
- display moves in standard notation
- no backsies!
- check solution on move seq end?
- autoplay opponents move
- time limit
- show countdown
- auto next
- auto grading
- modes:
  - rush
  - casual

#### ops

- shuffle
- randomize (swap) color of problem
- combine by tag
- filter by "failure" rate
- filter by tag

#### stats

- time 
- stats per tag

#### import/export helpers

convert pgn to csv for bulk import
convert pgn to deck?

