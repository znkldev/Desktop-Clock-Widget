# Desktop Clock Widget
 This project contains a basic clock widget created using Tkinter. This widget can be configured to start up when the system boots in Windows operating systems.

[![license](https://img.shields.io/github/license/QL-Win/QuickLook.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)
[![Github All Releases](https://img.shields.io/github/downloads/znkldev/Desktop-Clock-Widget/total.svg)](https://github.com/znkldev/Desktop-Clock-Widget/releases)
[![GitHub release](https://img.shields.io/github/release/znkldev/Desktop-Clock-Widget.svg)](https://github.com/znkldev/Desktop-Clock-Widget/releases/latest)

## Hotkeys and Buttons
- `Win`+`H` Show/Hide the widget window
> (Win + H shortcut conflicts with Windows applications in some cases.)
- `Win`+`T` Show/Hide the widget window 
- `Alt`+`M` Change the clock mode
- `Alt`+`0` Reset chronometer
- `Alt`+`1` Start chronometer


## Code how to Use

1. Download or clone the project to your computer.
2. Open a terminal or command prompt and run the following command to install the required libraries:

## Required Libraries
- `tkinter`
- `pywin32`
- `keyboard`
- `ctypes`
  

How to install:

```sh
pip install -r requirements.txt
```
The requirements.txt file contains a directory. That directory needs to be transferred to the command line.
```sh
# Example: If your 'requirements.txt' file is located at 'C:\users\pc\downloads\Desktop-Clock-Widget\'
cd C:\users\pc\downloads\Desktop-Clock-Widget
pip install -r requirements.txt
```

3. Move the `.exe` file from the project folder to the startup folder or create a shortcut.


>[!important] 
>**Fonts download link:** 
>
>https://fonts.google.com/specimen/Montserrat
>
>https://fontmeme.com/fonts/ds-digital-font/

## Startup Configuration

1. Right-click in the project folder to create a shortcut for the `.exe` file. (Or you can move the `exe` file directly.)
2. Press `Win + R`, type `shell:startup`, and press Enter. This opens the Windows startup folder.
3. Right-click in the startup folder and select "Paste shortcut" to add the shortcut.

## Screen Capture
It will look like this;

Clock:


![Screenshot of the Clock Widget](https://res.cloudinary.com/dqrjy97s9/image/upload/v1708883867/lhrxixc6iqc4xnlxjcxb.png)

Chronometer:

![Screenshot of the Clock Widget](https://res.cloudinary.com/dqrjy97s9/image/upload/v1708884647/hi3lte7tnxz1fupszcdh.png)

>[!Warning]
>Montserrat and DS-DIGITAL font has been used for the clock. If this font is not installed on your computer, it may be displayed in a different font.

# Download
[Download Latest Release](https://github.com/znkldev/Desktop-Clock-Widget/releases)
 


## License

![GPL-v3](https://www.gnu.org/graphics/gplv3-127x51.png)

This project is licensed under the [GPL-3.0](https://opensource.org/licenses/GPL-3.0) License. For more information, see the [LICENSE file](LICENSE-GPL).

If you want to make any modification on these source codes while keeping new codes not protected by GPL-3.0, please contact me for a sublicense instead.

**Develooped by ZNKL© 07/12/2023**
