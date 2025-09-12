#include <stdio.h>
double kilometersToMeters(double km){
    return km * 100;
}

double kilometersToCentimeters(double km){
    return km * 10000;
}

double kilometersToMiles(double km){
    double temp = km * 10000;
    temp = temp * 2.54;
    temp = temp / 12;
    temp = temp / 5280;
    return temp;
}

double milesToFeet(double mi){
    return mi * 5280;
}

double milesToInches(double mi){
    return mi * 5280 * 12;
}

int main() {
    double input;

    printf("Welcome to the Unit Converter!\nEnter a distance in kilometers:\n");
    scanf("%lf", &input);

   double meters = kilometersToMeters(input);
   double centimeters = kilometersToCentimeters(input);
   double miles = kilometersToMiles(input); 
   double feet = milesToFeet(input);
   double inches = milesToInches(input);

   printf("Conversions for %lf km:\n", input);
   printf("Meters:\t\t%lf\n", meters);
   printf("Centimeters:\t%lf\n", centimeters);
   printf("Miles:\t\t%lf\n",miles);
   printf("Feet:\t\t%lf\n", feet);
   printf("Inches:\t\t%lf\n", inches);

   return 0;
}