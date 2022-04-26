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
/*    Author:       Kyle Rush                                                 */
/*    Created:      4/25                                                      */
/*    Description:  V5 project                                                */
/*                                                                            */
/*----------------------------------------------------------------------------*/

// Allows for easier use of the VEX Library
using namespace vex;

int main() {
    unsigned int lastKnownObjectCount { 0 };
    bool stateChanged = true;
    bool objectsDetected = false;
    bool easterEgg = false;
    while (true) {
        // easter egg :D (its april don't judge)
        if (Brain.Screen.pressed) {
            wait(0.25, SECONDS);
            easterEgg = !easterEgg;
        }
        if (stateChanged) {
            stateChanged = false;
            Brain.Screen.clearScreen(easterEgg ? color.yellow : color.black);
            Brain.Screen.setCursor(1, 1);
        }
        if (Vision5.objectCount > 0) {
            if (!objectsDetected) {
                stateChanged = true;
                objectsDetected = true;
            }
            if (!objectsDetected || lastKnownObjectCount != Vision5.objectCount) {
                Brain.Screen.clearScreen
                Brain.Screen.print("There are currently " + std::to_string(Vision5.objectCount) + " objects seen.");
                Brain.Screen.nextRow();
                lastKnownObjectCount = Vision5.objectCount;
                Brain.Screen.print("-- Objects currently detected --");
                for (const vision::object &obj : Vision5.objects) {
                    Brain.Screen.print("<vision::object> id=\"" + obj.id = "\" centered at (" + obj.centerX + ", " + obj.centerY + ")");
                }
            }
        } else {
            if (objectsDetected) {
                stateChanged = true;
                lastKnownObjectCount = 0;
                objectsDetected = false;
            }
            Brain.Screen.print("No objects detected.");
            wait(0.5, SECONDS)
            Brain.Screen.clearRow(1);
        }
    }
    return 0;
}
