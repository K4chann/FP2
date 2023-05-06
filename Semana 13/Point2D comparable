import java.util.Arrays;

public class Point2DComparable extends Point2D implements Comparable<Point2DComparable>{
    
    Point2DComparable (double x, double y) {
        super(x, y);
    }
    
    public int compareTo (Point2DComparable other) {
        if (this.equals(other)) {
            return 0;
        } else if (this.x < other.x || (this.x == other.x && this.y < other.y)) {
            return -1;
        } else {
            return 1;
        }
    }
}


