### ankichess
Add-ons for Anki 2.1+ to support learning chess using Anki.  
There is only one add-on at the moment, namely **replace_fen_with_svg**.
The addon depends on the following non-standard packages:
- `chess` 
The `chess` package is bundled with this addon.  


No unit testing has been done.  
A handful of runs have been done using Anki desktop on Ubuntu 20.04.


#### replace_fen_with_svg

Replaces a Forsyth–Edwards Notation (FEN) of a chess position
with an SVG. The FEN string must be enclosed by a FEN tag pair.  
The opening FEN tag is `[fen]` ;the closing FEN tag is `[/fen]`.


There are a few options to configure the svg output.
These options are documented [here.](config.md)
