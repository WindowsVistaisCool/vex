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
vision::signature Vision5__REDD = vision::signature (1, 5877, 10923, 8400,-891, 299, -296,2.5, 0);
vision::signature Vision5__GREENN = vision::signature (2, -5709, -1309, -3510,-2379, -351, -1364,1, 0);
vision::signature Vision5__BLUEE = vision::signature (3, -3413, -1235, -2324,4515, 9557, 7036,1.1, 0);
vision Vision5 = vision (PORT5, 66, Vision5__REDD, Vision5__GREENN, Vision5__BLUEE);
/*vex-vision-config:end*/


#pragma endregion VEXcode Generated Robot Configuration

/*----------------------------------------------------------------------------*/
/*                                                                            */
/*    Module:       main.cpp                                                  */
/*    Author:       {author}                                                  */
/*    Created:      {date}                                                    */
/*    Description:  V5 project                                                */
/*                                                                            */
/*----------------------------------------------------------------------------*/

// Include the V5 Library
#include "vex.h"
  
// Allows for easier use of the VEX Library
using namespace vex;

int main() {
  while (true) {
    Brain.Screen.clearLine(1);
    Brain.Screen.setCursor(1, 1);
    bool foundRed = Vision5.takeSnapshot(Vision5__REDD);
    bool foundGreen = Vision5.takeSnapshot(Vision5__GREENN);
    bool foundBlue = Vision5.takeSnapshot(Vision5__BLUEE);
    bool anyObject { foundRed || foundGreen || foundBlue };
    if (anyObject) {
      if (foundRed) {
        Brain.Screen.print("JOE FOUND RED!!");
      } else if (foundGreen) {
        Brain.Screen.print("JOE FOUND GREEN!!");
      } else if (foundBlue) {
        Brain.Screen.print("JOE FOUND BLUE!!");
      }
    } else {
      Brain.Screen.print("No objcects :(");
    }
  }
}
