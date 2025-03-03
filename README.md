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

Modified by Artem:

Running with the new rooms requires additional input/output mapping. 

1. Download the scheduler params from https://hkn.eecs.berkeley.edu/admin/tutor/params_for_scheduler?which=officer into a file in this directory named `base_params.json`
2. Inside `process_input.py` modify start and end hours(these are tutoring hours, they must not include prodev hours) inside of python file as well as people doing review sessions and execs. To add people just do `execs = ["First Last", ...]` where First and Last name are from hkn.mu website, also do this for other variables, leaving them empty is fine.
3. Run `python process_input.py`.
4. Use the output `scheduler_input.json` file as input to the scheduler (see the Java instructions above)
5. Rename the scheduler output file to `output.json`
6. Run `python change_output_ids.py`
7. Upload `upload_ready_output.json` to https://hkn.eecs.berkeley.edu/admin/tutor

There is also a `process_output.py` file which might be useful, but I havent used it.

For tutoring/debug purposes `print_number_available_assignments.py` can be helpful. It prints total number of hours available for assignment.
 Run this after running `process_input.py`. You can manually calculate number of hours needed for slots and see how many extra you need/have.
