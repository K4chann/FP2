public class SteppedCounterCloneable extends SteppedCounter implements Cloneable {
    SteppedCounterCloneable (int step) {
        super(step);
    }
    
    @Override
    public SteppedCounterCloneable clone() throws CloneNotSupportedException {
        return (SteppedCounterCloneable) super.clone();
    }
}
