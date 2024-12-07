interface Driveable {
    drive(): void;
}

function driveSomething(vehicle: { drive(): void }) {
    vehicle.drive();
}

const myCar: Driveable = {
    drive() {
        console.log("The car is driving.");
    }   
};

const myTruck = {
    drive() {
        console.log("This random vehicle is driving.");
    },
    fly() {
        console.log("This vehicle can also fly!");
    }
};

// Both calls are valid in TypeScript due to structural typing
driveSomething(myCar); // This works because 'myCar' matches the structure required by 'driveSomething'.
driveSomething(myTruck); // This also works even though 'randomVehicle' has an extra method 'fly'.
