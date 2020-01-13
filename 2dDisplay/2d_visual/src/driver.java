
import java.awt.Color;
import java.awt.geom.Point2D;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

class Point {
	double x;
	double y;

	public Point(double d, double e) {
		super();
		this.x = d;
		this.y = e;
	}
}

class Rectangle {

	private final Point topLeft;
	private final Point bottomRight;

	public Rectangle(Point topLeft, Point bottomRight) {
		this.topLeft = topLeft;
		this.bottomRight = bottomRight;
	}

	/**
	 * Java method to check if two rectangle are intersecting to each other.
	 * 
	 * @param other
	 * @return true if two rectangle overlap with each other
	 */
	public boolean isOverLapping(Rectangle other) {

		if (this.topLeft.x > other.bottomRight.x // R1 is right to R2
				|| this.bottomRight.x < other.topLeft.x // R1 is left to R2
				|| this.topLeft.y < other.bottomRight.y // R1 is above R2
				|| this.bottomRight.y > other.topLeft.y) { // R1 is below R1
			return false;
		}
		return true;
	}

	@Override
	public String toString() {
		return (this.topLeft + "    " + this.bottomRight);
	}

}

public class driver {

	@SuppressWarnings("deprecation")
	public static void main(String[] args) throws InterruptedException, FileNotFoundException {

		// compile python sim;
		int InterSize = 200;
		int InterSquare = 20;
		

		Draw map = new Draw();
		map.setCanvasSize(800, 800);
		map.setXscale(-InterSize, InterSize);
		map.setYscale(-InterSize, InterSize);
	//	map.enableDoubleBuffering();
		

		// variables
		int vin;
		int lane;
		double w;
		double l;
		int numberOfCars = 600;
		Point2D pos = new Point2D.Double();
		ArrayList<Rectangle> cars = new ArrayList<Rectangle>();
		
		
		//display
		boolean clear = true;
		Color grey = new Color(170, 170, 170);
		

		// Location of file to read
		File file = new File("/home/maxwell/Documents/Git/Intersection_2d_simulation/Algorithm/carData.csv");

		// big data
		String[] thisLines;
		String thisLine = null;

		// read in data
		double[] tempData = new double[numberOfCars];
		ArrayList<double[]> data = new ArrayList<double[]>();
		Scanner scanner = new Scanner(file);
		while (scanner.hasNextLine()) { // iterte through row
			
			thisLine = scanner.nextLine();
			
			//thisLine = scanner.nextLine();
			thisLines = thisLine.split(",");
			tempData = new double[numberOfCars];
			// convert into double
			for (int i = 0; i < thisLines.length; i++) {
				try{
					tempData[i] = Double.parseDouble(thisLines[i]);
				}catch (Exception e) {
					// TODO: handle exception
				}
			}
			data.add(tempData);
		}
		scanner.close();

		
		for (int j = 4; j < data.size() - 4; j = j + 10) {

			//type 'p' to end display
			if (map.isKeyPressed(80)) {
				clear = false;
			}
			
			//draw background
			map.clear(new Color(40,120,40));
			
			//draw road
			map.setPenColor(grey);
			map.filledRectangle(0, 0, InterSquare, InterSize);
			map.filledRectangle(0, 0, InterSize, InterSquare);
			
			//draw yellow lanes
			map.setPenColor(Color.YELLOW);
			for (int i = -InterSize; i <= InterSize ; i = i + (InterSize/10)) {
				map.filledRectangle(i, 0, 5, 2);
				map.filledRectangle(0, i, 2, 5);
			}
			
			//draw middle inter
			map.setPenColor(Color.black);
			map.setPenRadius(0.0025);
			map.square(-InterSquare / 2, -InterSquare / 2, InterSquare / 2);
			map.square(InterSquare / 2, -InterSquare / 2, InterSquare / 2);
			map.square(InterSquare / 2, InterSquare / 2, InterSquare / 2);
			map.square(-InterSquare / 2, InterSquare / 2, InterSquare / 2);
			
			
			
			
			

			for (int i = 0; i < numberOfCars; i++) {

				vin = (int) data.get(0)[i];
				lane = (int) data.get(1)[i];
				l = data.get(2)[i];
				w = data.get(3)[i];

				pos.setLocation(data.get(j)[i], data.get(j + 1)[i]);
				// System.out.println(pos.toString());

				if ((pos.getX() != 0.0 && pos.getY() != 0.0) && (Math.abs(pos.getX()) < (InterSize + (InterSquare/2))) && (Math.abs(pos.getY()) < (InterSize + (InterSquare/2)))) {
					map.setPenColor((vin * 15) % 256, (vin * 7) % 256, (vin * 99) % 256);
					//map.setPenColor(Color.BLUE);
					if (lane == 2 || lane == 4) {
						double temp = w;
						w = l;
						l = temp;

					}
					map.filledRectangle(pos.getX(), pos.getY(), w, l);

					// add a car
					Point l1 = new Point(pos.getX() - w, pos.getY() + l);
					Point r1 = new Point(pos.getX() + w, pos.getY() - l);

					Rectangle tempCar = new Rectangle(l1, r1);
					cars.add(tempCar);
				}

			}
			
			map.show(1);
			
			
			//hold 'o' to pause, will start when let go
			while(map.isKeyPressed(79)) {}
			
			
			
			//if 'p' clicked do not clear
			if(!clear) {
				break;
			}else {
				map.clear();
			}

			// check if any rectangle colided
			//for (int k = 0; k < cars.size(); k++) {
			//	for (int k2 = 0; k2 < cars.size(); k2++) {
			//		if ((cars.get(k).isOverLapping(cars.get(k2))) && (k2 != k)) {
			//			System.out.println(k + " -- " + k2);
			//		} else {
			///			//System.out.println("good");
			//		}
			//	}
			//}
			cars.clear();

		}
		System.out.print("done");
	

	}
}