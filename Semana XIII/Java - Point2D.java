import java.util.Arrays;

public class Point2D {
	private double x, y;
    
    public Point2D(double x, double y) {
        this.x = x;
        this.y = y;
    }
    
    public double[] coordinates() {
        return new double[]{x, y};
    }
    
    @Override
    public boolean equals(Object other) {
        if (this == other) return true;
        if (this.getClass() != getClass() || other == null) return false;
        Point2D obj = (Point2D) other;
        return Arrays.equals(this.coordinates(), obj.coordinates());
    }
    
    @Override
    public String toString() {
        return String.format("(%f, %f)", x, y);
    }
}
