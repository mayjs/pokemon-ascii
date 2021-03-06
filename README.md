# pokemon-ascii

Watch the pokemon ascii being born!

![img/generation.gif](img/generation.gif)

This is a module for generating ascii art for any of the 721 pokemon, across 7 generations, in the Pokedex. The package includes functions for generating "gravatars" (pokemon associated with an identifier like an email address), and functions for searching and exploring the database. The library includes a [version of the database](pokemon/database/db.json) generated with [scripts/make_db.py](scripts/make_db.py) that can be updated by re-running the script. The choice of ascii art is to produce pokemon images or avatars that are suited for command line tools.

      usage: pokemon [-h] [--avatar AVATAR] [--pokemon POKEMON] [--message MESSAGE] [--catch]

      generate pokemon ascii art and avatars

      optional arguments:
        -h, --help         show this help message and exit
        --avatar AVATAR    generate a pokemon avatar for some unique id.
        --pokemon POKEMON  generate ascii for a particular pokemon (by name)
        --message MESSAGE  add a custom message to your ascii!
        --catch            catch a random pokemon!

      usage: pokemon [-h] [--avatar AVATAR] [--pokemon POKEMON] [--message MESSAGE] [--catch]


## Installation

You can install directly from pip:

      pip install pokemon


or for the development version, clone the repo and install manually:

      git clone https://github.com/vsoch/pokemon-ascii
      cd pokemon-ascii
      sudo python setup.py sdist
      sudo python setup.py install


## Produce an avatar

An "avatar" is an image that is consistently associated with some unique ID. In our case, this is an ascii avatar. For example,

![img/avatar.png](img/avatar.png)

To do this, I take the hash of a string, and then use modulus to get the remainder of that hash divided by the number of pokemon in the database. This means that, given that the database doesn't change, and given that the pokemon have unique IDs in the range of 1 to 721, you should always get the same image for some unique id (like an email).


      pokemon --avatar vsoch

      @@@@@@@@@@@@@*,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@,:::::::::,@@@:,S+@@@@@@@#:::::::,:@@@@@@@@@@@@@@@@
      @@@@@@@@:::::::::****@@**..@@@@@:::::::::::::S@@@@@@@@@@@@@@
      @@@@@@@::::***********#..%.S@@#::::::::::*****S@@@@@@@@@:?@@
      @@@@@@@*****?%%%%?***....SSSS#*****************#@@@@@@@@,::@
      @@@@@@@%***S%%%%%.#*S.SSSSSS?.****?%%%%%#*******@@@@@#:::::.
      @@@@@@@@****%%%%#...#SSSS#%%%?***?%%%%%%%******%@@@@%::::***
      @@@@@@@@@+****SSSSSS?SSS.%...%#SS#%....%.******@@@@@?*******
      @@@@@@@@@@@@#SSSSSSS#S#..%...%%.....%.%.******@@@@@@@#**.**@
      @@@@@@@@@@@..SSSSS..?#.%..%.......%.%.******#@@@@@@@@@@S%,@@
      @@@@@@@@@@#%........................%****%,@@@@@@@@@@@?%?@@@
      @@@@@@@@@@.#*@@@%.................%%%......SSS.SSS%@#%%?@@@@
      @@@@@@@@@%+*@@?,.%....%%.,@,@@,*%.%%%..%%%%.%....%...?#@@@@@
      @@@@@@@@@:*.@#+?,%%%%%.%,@??#@@@**......%........%...%%*@@@@
      @@@@@@@@@@.*.@##@...%%.+@##@?,@@****.....%...%....?...%%@@@@
      @@@@@@@@@@@.**+**#++SS***,*#@@@*****%%.%.......%%........@@@
      @@@@@@@@@@@@************************..........%%.%%...%%*@@@
      @@@@@@@@@@@@@@,?**?+***************.%........#....%%%%%%@@@@
      @@@@@@@@@@@@@@@@@%#*+....*******..%%..%%.....%%%%%%%%%%@@@@@
      @@@@@@@@@@@@@@+%%%%%%??#%?%%%???.%%%%%...%%%.**.**#%%%@@@@@@
      @@S#****.?......%%%%%%?%@@@@@:#........%?#*****.#***#@@@@@@@
      @***%.*S****S**.%%%%%%@@@@@@@S....%%..%@@+*+..%**+%#.@@@@@@@
      @%%..*..*%%+++++%%%%@@@@@@@...%.%%.%.%@@@,+#%%%%++++@@@@@@@@
      @:+++#%?++++++++%%@@.**%**.****#..%%%,@@@@@S+.?++++@@@@@@@@@
      @@@++?%%%?+++++#@@@**.********S**%%%@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@%++++?@@@@@@S%%*#%.**%%**..+%@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@@++++++++.S++++#@@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@@@++%%%%?+++++@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@@@@*+#%%%+++%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

      vsoch


You can also use the functions on command line:

      from pokemon.skills import get_avatar
 
      # Just get the string!
      avatar = get_avatar("vsoch",print_screen=False)
      print avatar

      # Remove the name at the bottom, print to screen (default)
      avatar = get_avatar("vsoch",include_name=False)


## Randomly select a Pokemon

You might want to just randomly get a pokemon! Do this with the `--catch` command line argument!

      pokemon --catch

      @%,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      .????.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      .???????S@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      :?????????#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      *?????????????*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @???????#?????###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,*.??#
      @?????,##,S???#####@@@@@@@@@@@@@@@@@@@@@@@@@@S##????????????
      @?????*,,,,,,########@@@@@@@@@@@@@@@@@:###????????????????#@
      @##????,,,,,,,,,#####@@@@@@@@@@@@@.######?????#?:#????????@@
      @####?#,,,,,,,,,,,##@@@@@@@@@@@@@@#######*,,,,,*##+?????+@@@
      @######,,,,,,,,,,,S@@@@@@@@@@@@@@#.,,,,,,,,,,,,,,:?####@@@@@
      @######,,,,,,,,,,%@@,S.S.,@@@@@@@,,,,,,,,,,,,,,,######@@@@@@
      @@#####,,,,,,,,.,,,,,,,,,,,,,,,*#,,,,,,,,,,,,,.#####:@@@@@@@
      @@@@@@@@@@.#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,######@@@@@@@@@
      @@@@@@@@@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,+######@@@@@@@@@@
      @@@@@@@@%,,,,,++:,,,,,,,,,,,,,,,,,,,,,@@:.######:@@@@@@@@@@@
      @@@@@@@:,,,:##@@@#,,,,,,,,,,,,?@S#,,,,,,@@@@@@@@@@@@@@@@@@@@
      @@@@@@@?,,,#######,,,,,,,,,,,#.@:##,,,:?@@@@@@@@@@@@@@@@@@@@
      @@@@@@@.,,S,??%?*,,,,,,,,,,,,####?%+,::%@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@?..*+,,,,,,*,,,,,,,,,,,+#S,::::*@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@%..*,,,,,,,,,,,,,,,,,,,:.*...%@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@.**::*::::::,,:::::::+.....@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@.@@@@?:**:::*::::::::::*...@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@?,,,,,,,,,:,##S::::**:::S#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@.,,,,,,:S#?##?########:#****#,@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@,%:*%,??#,,,,:*S##**:..****:,.*@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@+,,,,,,,,,,,,,,,,,,*...*:,.,@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@+,,,,,,,,,,,,,,,,,,?@@@@@*#?@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@*,,,,,,,,,,,,,,,,,,.@#########?@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@.*:,,,,,,,,,,,,,,:.##%,?#####????:@@@@@@@@@@@@@
      @@@@@@@@@@@@@@?.....*******....S@@@@@@:##?????@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@S.+..********...#%@@@@@@@@@##,@@@@@@@@@@@@@@@@
      @@@@@@@@@@@#*,,,,*.#@@@@@@@..*:,,*S@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@+@,%,,,#@@@@@@@@@@,S,,,%,,:@@@@@@@@@@@@@@@@@@@@@@@

      Pichu

You can equivalently use the `--message` argument to add a custom message to your catch!

      pokemon --catch --message You got me!

      @@@@@@@@@*.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@...+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@++++@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      :..+,@@+.+++%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @..++++S++++++.?...@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@:S.S+SSS.S%++.+++@@@@@@@@@@+.%.@@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@:SSSSSSSSSS,@@@@@@@,:,:.SS+.....+.@@@@@@@@@@@@@@@@@@@@@@
      @@@@,:%SS++SS.,.%,:,S,,,,+..%.........S.@@@@@@@@@@@@@@@@@@@@
      @@@@@,:*...:,,+,.,,,,,,,*%%%++++..+++SSS+@@@@@@@@@@@@@@@@@@@
      @@@@@@,,.....%:,,,:.:.,:.%%.SSSS++SS+%+S%,+@@@@@@@@@@@@@@@@@
      @@@@@@@*.....S...***+,,,%..%++,?SSS.%.%%%:,.,@@@@@@@@@@@@@@@
      @@@@@@@@,+**........,,,,....++S@,+%..#..%,,S..@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@*..:,,,,,%..%++S%%.%%.S%%,,*+.+@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@S,,,,,,,,,%%%..SS..%?%%%,,,S+...@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@S.:::::::::%.%%S...%%%%:::*.....**@@@@@@@@@@
      @@@@@@@@@@@@@@@@.%%..:::::::S%%.?%%%%%:::....**,S,,:@@@@@@@@
      @@@@@@@@@@@@@@:::*%%%%?..*:::,.%%%%.,:*.%@@.*:,,,:,,S@....@@
      @@@@@@@@@@@@@:,:,::*.?%%%%%%?+*%%?.?%%%%%+@@,,,,,,,.++%++@@@
      @@@@@@@@@@@@@@*,,,,,**...*%%%%%%%%%%?++++++.@,,,,,SS+SS++@@@
      @@@@@@@@@@@@@,,.,S,,,,:....***%%?%++++++++++.@.,,+SSSSS.S+@@
      @@@@@@@@@@@@,,SSSS..:.%,:*..?%%??%%++++++.+S+@@@.S..%S.%.S++
      @@@@@@@@@@@,,S.....S::*.@@@%%%%@?%%#+++++%%%?S@@@@@.%.,@@...
      @@@@@@@@@@@:,,?.%%%::::@@@...%.@?.%.++++.+%%%%.@@@@..++@@@@@
      @@@@@@@@@@S,.%%.:,,,,,S@@@@@.?@@+SS,S..........@@@@@,@@@@@@@
      @@@@@@@@@@@+S...++.,,:@@@@@@@@@@@@@@@%....SSS+SS@@@@@@@@@@@@

      You got me!

You can also catch pokemon in your python applications. If you are going to be generating many, it is recommended to load the database once and provide it to the function, otherwise it will be loaded each time.

      from pokemon.master import catch_em_all, get_pokemon

      pokemons = catch_em_all()
      catch = get_pokemon(pokemons=pokemons)

The catch is a dictionary, with keys as the pokemon ID, and the value being another dictionary with various meta data (height, weight, japanese, link, ascii, etc).


## Updating the database

The database was generated by running the script make_db.py, and you can update it by running it yourself, if at some point in the future new pokemon are added to the index.

      git clone https://github.com/vsoch/pokemon-ascii
      cd pokemon-ascii
      cd scripts
      python make_db.py

The file pokemons.json will be saved under [pokemon/databases](pokemon/databases). Next, install as usual (hopefully you aren't using system python and don't need sudo... clearly I've made some bad life choices here :P

      sudo python setup.py sdist
      sudo python setup.py install


## Issues and updates

Would you like different or updated functionality? Please ping me by adding an [issue](https://github.com/vsoch/pokemon-ascii)! I did this for fun, might sneak it into a few command line applications, and it's pretty simple so far! I hope you have fun with it! :D
