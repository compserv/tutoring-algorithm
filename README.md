# CS270 Project -- HKN Office Hour Scheduler

HKN holds weekly office hours that are rescheduled each semester as new
officers and committee members roll in.

## Building

Build this project with Gradle:

```sh
gradle build
```

If you don't have Gradle installed, the bundled `gradlew` wrapper script will
download a copy of Gradle and run as normal (`gradlew.bat` on Windows):

```sh
gradlew build
```

The output `Scheduler.jar` will be located in `build/libs`.

## Running

Gradle 4.9+:
```
gradle run --args='data.json'
```

Gradle older than 4.9:

```
gradle run -Pdata="['data.json']"
```

## Notes (Updated Sep 05, 2023)
For @bri25yu, I had to install Java Development Kit (JDK) via https://www.oracle.com/java/technologies/downloads/ and download the most recent version of gradle from https://gradle.org/install/ (I chose manual installation). For Sp23, I also had to run the updated post processing script on the output. 

Running with the new rooms requires additional input/output mapping. 

1. Download the scheduler params from https://hkn.eecs.berkeley.edu/admin/tutor/params_for_scheduler?which=officer into a file in this directory named `base_params.json`
2. Run `python process_input.py`
3. Use the output `scheduler_input.json` file as input to the scheduler (see the Java instructions above)
4. Rename the scheduler output file to `output.json`
5. Rename the scheduler input file to `input.json` (or make a copy of it with that name)
6. Run `python process_output.py` - may not be necessary depending on how many tutors are available. Can also try uploading `output.json` to hkn.mu.
7. Upload `processed_output.json` to https://hkn.eecs.berkeley.edu/admin/tutor
