#include <stdio.h>
double kilometersToMeters(double km){
    return km * 1000;    // km --> m
}

double kilometersToCentimeters(double km){
    return km * 100000;    // km --> cm
}

double kilometersToMiles(double km){
    return km * 100000 / 2.54 / 12 / 5280;    // km --> cm --> in --> ft --> mi
}

double milesToFeet(double mi){
    return mi * 5280;    // mi --> ft
}

double milesToInches(double mi){
    return mi * 5280 * 12;    // mi --> ft --> in
}

int main() {
    double input;

    printf("Welcome to the Unit Converter!\nEnter a distance in kilometers:\n");
    scanf("%lf", &input);

    // check for negative distance (protect against bad input breaking the code or giving wrong/irrelevant answers)
    if(input < 0){
        printf("You entered a negative number!\n");
        return 0;
    }
    
   double meters = kilometersToMeters(input);
   double centimeters = kilometersToCentimeters(input);
   double miles = kilometersToMiles(input); 
   double feet = milesToFeet(miles);
   double inches = milesToInches(miles);

    // print all conversions
   printf("Conversions for %lf km:\nMeters:\t\t%lf\nCentimeters:\t%lf\nMiles:\t\t%lf\nFeet:\t\t%lf\nInches:\t\t%lf\n", input, meters, centimeters, miles, feet, inches);

   return 0;
}
