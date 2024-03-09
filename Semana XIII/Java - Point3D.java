import java.util.Arrays;

public class Point3D extends Point2D {
    private double z;

    public Point3D (double x, double y, double z) {
        super(x, y);
        this.z = z;
    }

    public double getZ() {
        return z;
    }

    @Override
    public boolean equals(Object other) {
        if (this == other) return true;
        if (other.getClass() != getClass() || other == null) return false;
        Point3D obj = (Point3D) other;
        return super.equals(new Point2D(this.x, this.y)) && this.z == obj.z;
    }

    @Override
    public String toString() {
        return super.toString() + ", z: " + this.z;
    }
    
    @Override
    public double[] coordinates () {
        double[] result = Arrays.copyOf(super.coordinates(), 3);
        result[2] = this.z;
        return result;
    }
}
