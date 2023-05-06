public class SteppedCounter extends Counter {
    private int paso, counter;
    
    public SteppedCounter (int paso) {
        super();
        this.paso = paso;
        this.counter = 0;
    }
    
    @Override
    public void step() {
        for (int i = 0; i < this.paso; i++) {
            super.step();
        }
        
        this.counter = super.getValue();
    }
}
