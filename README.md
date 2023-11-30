[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/kCrKdl4V)
# ExplorationActivity2

## 1. Which package/library did you select

The sample program additionally demonstrates the use of Colorama library as well as BCrypt. 

## 2. What is the package/library?
### What purpose does it serve?
Colorama adds the ability to simply add colour to terminal text by allowing for the modification of the text colour itself, the background colour, and the style of the text (DIM, NORMAL, BRIGHT) 
### How do you use it?
First, install the library by running the following command: ``pip install colorama``      
Then import the necessary resources from the library. The example below shows importing Style, Fore, Back.  
```from colorama import Fore, Style, Back```  
When printing strings or receiving input, add "Style.BIGHT", "Fore.BLUE", and or "Back.BLACK" to modify the following string's appearance. each Style, Fore, and Back allow for .RESET to reset their values to the default. The application of these modifiers remains until it is reset or changed so if output is desired for only a certain section of text it must be reset to the desired colour again.  When used on non-Windows devices, additional functionality such as blinking console text is available using attributes like so:  ``attrs=["blink"]``  The library can also be used on Windows devices to make ANSI escapes work properly by including ``from colorama import just_fix_windows_console  just_fix_windows_console()``. This functionality was not applicable for the purposes of this password guessing game. 
## 3. What are the functionalities of the package/library?
This package allows the programmer of a CLI application or interface to provide additional context to the user by providing coloured text output to the user. It lets the programmer decide what the background colour of the terminal will be, what the colour of the text itself will be, and the intensity or "style" of the text. 
## 4. When was it created?
Version 0.1 was available on April 19, 2010. 
## 5. Why did you select this package/library?
In absense of a graphical user interface many people are used to, making a command line interface provide more information without imagery is necessary to make a program more detailed and interactive. Allowing for numbers in my program to have varying shades of red, yellow, and green lets the user know whether their performance is poor or impressive. The ability to provide this in the context of simple colour lets the programmer take control over the style of the users terminal. Many terminal colours are adjusted by the user themselves allowing for the choice to be made by them instead of the programmer. Colorama overrides that logic by letting the programmer choose what the background colour of the program will look like. 
## 6. How did learning the package/library influence your learning of the language?
When using the library, I quickly deepened my understanding of printing syntax along with concatenation of strings. The modifiers act as a prefix to the printing of the strings, and needed to be formatted properly to function, with extra care being taken to not create a syntax error when adding colour to integers as a ``,`` was required instead of a ``,``. 
## 7. How was your overall experience with the package/library?
### When would you recommend this package/library to someone?
If anyone required adding colour to their CLI interface, this would definitely be my go to recommendation. 
### Would you continue using this package/library? Why or why not?
Yes of course I would continue to use this library because of its ease of use and compatibility across most platforms. Colorama can in theory also improve accessibility for a program by allowing for properly contrasted visuals or simply by highlighting imagery.  
