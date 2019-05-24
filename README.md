# ![NC2DT Logo](logo.png)

**NC2DT** is a osu! tool that allows one to convert their beatmaps' audio so that they, when
used with the **Nightcore (NC)** mod, sound the **same** as the **Double Time (DT)** mod.

## Usage

1. Download the latest release, from the [Releases](https://github.com/ekisu/NC2DT/releases) page.
2. Extract and run the `NC2DT.exe` executable.
3. Type into the search bar the name of the beatmap you want to create a NC2DT audio, and
double-click it in the results listing.
4. Click the _Create Converted Audio_ button to create the converted audio.
5. Switch between the normal and NC2DT versions of the audio using the _Switch to Original/NC2DT Audio_ button.

**Note:** If you also want to get rid of the nightcore beats, download [these silent effects](https://github.com/ekisu/NC2DT/releases/download/v0.1/silent-nightcore.zip) (found originally [here](https://osu.ppy.sh/community/forums/topics/617312)) and put them into your skin folder.

## Development

### Building (Windows)

You'll need Python 3.7 installed, and added to your `PATH`. Additionally, you'll need to download [sox](https://sourceforge.net/projects/sox/) and [soundstretch](https://www.surina.net/soundtouch/download.html). Place them on `src/main/resources/windows`, with sox inside a folder named `sox`.

1. Create a virtualenv: `python -m venv venv`, and activate it with `venv/Scripts/activate.bat` (for cmd) or `activate.ps1` (for PowerShell).
2. Inside the virtualenv, install the dependencies: `pip install -r requirements.txt`
3. Run the program with fbs: `fbs run`.
4. (Optional) Package the program for redistribution with `fbs freeze`. The binaries will be placed under `target/`.
