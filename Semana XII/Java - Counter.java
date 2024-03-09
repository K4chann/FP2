public class Counter {
    private int counter;
    
    public Counter() {
        this.counter = 0;
    }
    
    public void step() {
        this.counter++;
    }
    
    public int getValue() {
        return counter;
    }
    
    public void reset() {
        counter = 0;
    }
}
