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

## Notes
For @bri25yu, I had to install Java Development Kit (JDK) via https://www.oracle.com/java/technologies/downloads/ and download the most recent version of gradle from https://gradle.org/install/ (I chose manual installation). For Sp23, I also had to run the updated post processing script on the output. 
