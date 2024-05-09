import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.TreeMap;
import java.util.Scanner;
import java.io.File;
import java.util.Map;
import java.io.BufferedReader;
import java.io.FileReader;

public class sample_assignment07 {
    public static TreeMap<String, ArrayList<String[]>> list = new TreeMap<>();
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);

        // folder path
        String folderName = scn.next();
        String folderPath = "./" + folderName;
        scn.close();
        
        // read every files in the folder
        File folder = new File(folderPath);
        File[] files = folder.listFiles();
        
        // check every files
        if(files != null) {
            for(File file : files) {
                if(file.isFile() && file.getName().endsWith(".txt")) {
                    System.out.println("Reading file: " + file.getName());
                    readTXTFile(file, file.getName());
                }
            }
        }
        else System.out.println("Folder is empty or does not exist.");

        // create the board
        ArrayList<String[]> board = new ArrayList<>();
        for(int i = 0; i < 8; i++) {
            String[] row = new String[8];
            for(int j = 0; j < 8; j++) row[j] = "0";
            board.add(row);
        }
        int count = 0;
        for(Map.Entry<String, ArrayList<String[]>> map : list.entrySet()) {
            String color = map.getKey();
            boolean res = false;
            for(int i = 0; i < 8 && res == false; i++) {
                for(int j = 0; j < 8 && res == false; j++) {
                    res = placePiece(board, list.get(color), i, j, color);
                    if(res) count++;
                }
            }
        }
        writeBoardToFile(board, folderName + "_112XXXXXX.txt", count);
        // new ShowResult(board);
    }

    public static void writeBoardToFile(ArrayList<String[]> board, String filename, int count) {
        /*
         * @param board: the board for puzzles to put in
         * @param filename: the output file name
         * @param count: the number of puzzles you used
         */
        try{
            FileWriter writer = new FileWriter(filename);
            writer.write("We use " + count + " pieces of puzzles.\n");
            for(String[] row : board) {
                for(String cell : row) {
                    writer.write(cell + " ");
                }
                writer.write("\n");
            }
            writer.close();
            System.out.println("Written Success: " + filename);
        }
        catch(Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public static boolean placePiece(ArrayList<String[]> board, ArrayList<String[]> piece, int row, int col, String color) {
        /*
         * @param board: the board for puzzles to put in
         * @param pieces: the puzzle piece
         * @param row: the row where the puzzle piece place in
         * @param col: the column where the puzzle piece place in
         * @param color: the puzzle piece color name
         */
        int rows = board.size();
        int cols = board.get(0).length;
        int pieceRows = piece.size();
        int pieceCols = piece.get(0).length;

        // check oversize
        if(row < 0 || row + pieceRows > rows || col < 0 || col + pieceCols > cols) {
            return false;
        }

        // check overlapping
        for(int i = 0; i < pieceRows; i++) {
            for(int j = 0; j < pieceCols; j++) {
                if(!piece.get(i)[j].equals("0") && !board.get(row + i)[col + j].equals("0")) {
                    return false;
                }
            }
        }
        
        for(int i = 0; i < piece.size(); i++) {
            for(int j = 0; j < piece.get(i).length; j++) {
                if(piece.get(i)[j].equals(color)) {
                    board.get(row + i)[col + j] = color;
                }
            }
        }
        return true;
    }
    
    private static void readTXTFile(File file, String fileName) {
        /*
         * @param file: the txt file
         * @param fileName: the name of the txt file
         */
        try(BufferedReader reader = new BufferedReader(new FileReader(file))) {
            String line;
            ArrayList<String[]> arr = new ArrayList<>();
            while((line = reader.readLine()) != null) {
                String[] words = line.split(" ");
                arr.add(words);
            }
            fileName = fileName.replace(".txt", "");
            list.put(fileName, arr);
        }
        catch(Exception e) {
            System.err.println(e.getMessage());
        }
    }
}
