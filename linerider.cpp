#pragma region VEXcode Generated Robot Configuration
// Make sure all required headers are included.
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include <string.h>


#include "vex.h"

using namespace vex;

// Brain should be defined by default
brain Brain;


// START V5 MACROS
#define waitUntil(condition)                                                   \
  do {                                                                         \
    wait(5, msec);                                                             \
  } while (!(condition))

#define repeat(iterations)                                                     \
  for (int iterator = 0; iterator < iterations; iterator++)
// END V5 MACROS


// Robot configuration code.
/*vex-vision-config:begin*/
vision Vision5 = vision (PORT5, 66);
/*vex-vision-config:end*/


#pragma endregion VEXcode Generated Robot Configuration

/*----------------------------------------------------------------------------*/
/*                                                                            */
/*    Module:       linerider.cpp                                             */
/*    Author:       Kyle Rush                                                 */
/*    Created:      4/26                                                      */
/*    Description:  Line Rider                                                */
/*                                                                            */
/*----------------------------------------------------------------------------*/

// Allows for easier use of the VEX Library
using namespace vex;

void drive() {
  drivetrain.drive(directionType::fwd);
}

void stop() {
  drivetrain.stop(brakeType::brake);
}

int main() {
  //hog rider
  event::event stepuptodriveitsrapidreact = new event::event(drive);
  event::event stopdriving = new event::event(stop);
  bool hasStarted = false;
  while (true) {
    if (Vision5.objectCount == 0) {
      Brain.Screen.clearScreen();
      Brain.Screen.print(hasStarted ? "Robot has run off path" : "No objects detected");
      if hasStarted {
        break;
      } else {
        wait(1, SECONDS);
        continue;
      }
    }
    if (!hasStarted) { hasStarted = true; }
    Brain.Screen.nextRow();
    if (Vision5.largestObject.angle > 0) {
      stopdriving.broadcast();
      Brain.Screen.print("turn left");
    } else if (Vision5.largestObject.angle < 0) {
      stopdriving.broadcast();
      Brain.Screen.print("turn right");
    } else {
      stepuptodriveitsrapidreact.broadcast();
      Brain.Screen.print("go straight");
    }
  }
  return 0;
}
