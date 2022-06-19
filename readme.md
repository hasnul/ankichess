## ankichess
Add-ons for Anki 2.1+ to support learning chess using Anki.  
There is only one add-on at the moment, namely **replace_fen_with_svg**.
The addon depends on the following non-standard packages:
- `chess` : bundled with this addon.  


No unit testing has been done.  
A handful of runs have been done using Anki desktop on Ubuntu 20.04.


### replace_fen_with_svg

Replaces a Forsyth–Edwards Notation (FEN) of a chess position
with an SVG. The FEN string starts with `fen::` and ends with newline 
or `<br>`.

There are a few options to configure the svg output.
These options are documented [here.](config.md)

### Installation

Create a folder `ankichess` in the Anki addons folder and
copy the contents of this folder there.
Symbolic linking from the Anki addons folder to another
location does not work at time of writing (Anki v2.1.53).
