interface Container {
  addItem(item: string): void;
  getItem(index: number): string;
}

// This class does not correctly implement the Container interface
class Bag {
  addItem(item: string): void { // Method name does not match
    // Implementation not relevant for this example
  }
}

// This will cause a TypeScript compile-time error when we try to use Bag as a Container
function fillContainer(container: Container) {
  container.addItem("Apple"); // Error: Property 'addItem' does not exist on type 'Container'
}

const myBag = new Bag();
fillContainer(myBag); // TypeScript will flag this as an error
