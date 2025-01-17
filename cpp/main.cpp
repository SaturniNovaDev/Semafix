// main.py rewritten in C++ 
#include <iostream>
#include <thread> // for delays
#include <chrono> // for second management
#include <iomanip>

class Lane {
public:
    int carsAmount;
    int waitTime;
    int laneNumber;
    bool greenLight;
    
    Lane(int carsAmount, int waitTime, int laneNumber)
    : carsAmount(carsAmount), waitTime(waitTime), laneNumber(laneNumber), greenLight(false) {}
};

void givePriority(Lane lane, int timeFor){
    // Gives priority to a specific lane for a specific time in seconds

    lane.greenLight = true;
    std::cout << "Lane number " << lane.laneNumber << " has priority for " << timeFor << "seconds\n";

    std::cout << "before time" << std::endl;
    std::this_thread::sleep_for(std::chrono::seconds(timeFor));
    std::cout << "after time" << std::endl;
    lane.greenLight = false;
    lane.carsAmount = 0;
    std::cout << "Lane number " << lane.laneNumber << " has finished its priority time.\n";
}

void controlTraffic(Lane lane1, Lane lane2, int timeFor){
    // Header
    std::cout << std::left << std::setw(15) << "Lane" << " | " 
    << std::setw(20) <<  "Cars amount" << " | " 
    << std::setw(20) <<  "Wait time (s)" << " | \n";

    while (lane1.carsAmount > 0 || lane2.carsAmount > 0)
    {
        // Printing lane status
        std::cout << std::left << std::setw(15) << lane1.laneNumber << " | " 
            << std::setw(20) << lane1.carsAmount << " | " 
            << std::setw(20) << lane1.waitTime << " | \n";

        std::cout << std::left << std::setw(15) << lane2.laneNumber << " | " 
            << std::setw(20) << lane2.carsAmount << " | " 
            << std::setw(20) << lane2.waitTime << " | \n";

        if (lane1.waitTime > lane2.waitTime)
        {
            givePriority(lane1, timeFor);
            lane2.waitTime += timeFor;
            lane1.carsAmount = std::rand() % 16; // generate number between 0 and 15;
            lane1.waitTime = (std::rand() & 35) + 1; // generate number between 1 and 35;
        }
        else if (lane1.waitTime < lane2.waitTime)
        {
            givePriority(lane2, timeFor);
            lane1.waitTime += timeFor;
            lane2.carsAmount = std::rand() % 16; // generate number between 0 and 15;
            lane2.waitTime = (std::rand() & 35) + 1; // generate number between 1 and 35;
        }
    }
    std::cout << "Both lanes are empty. Exiting the traffic control system\n";
    std::this_thread::sleep_for(std::chrono::milliseconds(2500));
    std::cout << "Traffic control system has been terminated" << std::endl;
}

// Main class, with some testing
int main(){
    Lane laneA = Lane(12,15,1);
    Lane laneB = Lane(4,35,2);
    controlTraffic(laneA, laneB, 15);
    return 0;
}
