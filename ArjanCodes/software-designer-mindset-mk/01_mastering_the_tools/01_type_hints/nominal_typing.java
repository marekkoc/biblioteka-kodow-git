class Car {
    void drive() {
        System.out.println("Car is driving");
    }
}

class Truck {
    void drive() {
        System.out.println("Truck is driving");
    }
}

public class NominalTypingExample {
    public static void driveCar(Car car) {
        car.drive();
    }

    public static void main(String[] args) {
        Car car = new Car();
        Truck truck = new Truck();
        
        driveCar(car); // This works fine.
        // driveCar(truck); // This will result in a compile-time error.
    }
}
