//MINESWEEPER VERSION 1.1
//TO DO LIST
import java.util.*;
class Main {
  public static void main(String[] args) {
    //Welcoming message for them to read while it is being set up
    System.out.println("Welcome to minesweeper!, If you want to read the instructions enter 2!");
    System.out.println("If you already know how to play, input your favorite integer of choice,\nwhich hopefully isn't 2, and we can get right in to it.");
    // Ask the user to enter the number of rows and columns
    Scanner console = new Scanner(System.in);
    Random rand = new Random();
    int q = console.nextInt();
    if (q==2){
      System.out.println("The game is minesweeper, the goal is to place flags on the spots where all the bombs are\nGet your thinking cap on! because this is where you need some logic!\nThe spaces that say a number indicate how many bombs are adjacent to that\nspot on the board,and the Xs are uncleared spots, so be careful of those!\nyou only have 25 flags and there are 25 mines, so be sure to not waste any flags!, or also blow up a mine, yeah it would be worse if you blew up a mine");
      System.out.println("input literally integer to proceed");
      int b = console.nextInt();
      if (b==999999999){
        q=q+1;
      }
    }
    int numRows = 10;
    int numCols = 10;
    // Create an array of integers of the specified size
    int[][] field = new int[numCols][numRows];
    // setting every space clear of bomb
    for (int x = 0; x <= numCols - 1; x++) {
      for (int y = 0; y <= numRows - 1; y++) {
        field[x][y] = -2;
      }
    }
    // placing bombs
    int numBombs = 25;
    int bombcounter = 1;
    while (bombcounter <= numBombs) {
      int xcoord = rand.nextInt(10);
      int ycoord = rand.nextInt(10);
      if (field[xcoord][ycoord] != -1) {
        field[xcoord][ycoord] = -1;
        bombcounter++;
      }
    }
    // finding value for all the field
    for (int x = 0; x <= numCols - 1; x++) {
      for (int y = 0; y <= numRows - 1; y++) {
        if (field[x][y] == -2) {
          field[x][y] = valueFind(y, x, field);
        }
      }
    }
    // clearing all values adjacent to 0
    for (int x = 0; x <= numCols - 1; x++) {
      for (int y = 0; y <= numRows - 1; y++) {
        if (field[x][y] == 0) {
          zeroClear(field, x, y);
        }
      }
    }
    boolean stillPlaying = true;
    // guessing loop
    while (stillPlaying == true) {
      fieldPrint(numCols, numRows, field);
      System.out.println("Input 1 if you want to place a flag");
      System.out.println("Input 2 if you want to clear a spot");
      int flagOrSpot = console.nextInt();
      if (flagOrSpot==1||flagOrSpot==2){
        System.out.println("Choose the column");
        int columnCoord = console.nextInt() - 1;
        System.out.println("Choose the row");
        int rowCoord = console.nextInt() - 1;
        if (rowCoord <= 9 & rowCoord >= 0 & columnCoord <= 9 & columnCoord >= 0) {
          if (flagOrSpot == 1) {
            if (field[rowCoord][columnCoord] != -1) {
              System.out.println("You placed a flag where there wasn't a bomb, you lose!");
              stillPlaying = false;
            } else {
              field[rowCoord][columnCoord] = -2;
              numBombs--;
              System.out.println("Only " + numBombs + " bombs to go!");
            }
          } else if (flagOrSpot == 2) {
            if (field[rowCoord][columnCoord] == -1) {
              System.out.println("You tried to clear a spot where a bomb was, you lost!");
              explosionPrint();
              stillPlaying = false;
            }
            field[rowCoord][columnCoord] = field[rowCoord][columnCoord] + 10;
          }
        } else {
          System.out.println("wow, you can't even place that in the board correctly, you lose!");
          stillPlaying=false;
        }
        if (winCheck(field) == true) {
          System.out.println("You cleared all of the bombs! Congrats!");
          winPrint();
          stillPlaying = false;
        }
      } else {
        System.out.println("\nplease pick 1 or 2, seriously, it isn't that hard!");
      }
    }
  }

  public static void fieldPrint(int numCols, int numRows, int[][] field) {
    int x = 1;
    System.out.println("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n   | 1 2 3 4 5 6 7 8 9 10");
    for (int i = 0; i <= numCols - 1; i++) {
      if (x == 10) {
        System.out.print("10 | ");
      } else {
        System.out.print(x + "  | ");
      }
      for (int a = 0; a <= numRows - 1; a++) {
        int product = field[i][a];
        if (product == -1) {
          //bomb
          System.out.print("X ");
        } else if (product == -2) {
          //flag
          System.out.print("> ");
        } else if (product == 0) {
          System.out.print("0 ");
        } else if (product < 10) {
          //unrevealed blank
          System.out.print("X ");
        } else {
          //revealed blank
          System.out.print(product - 10 + " ");
        }
      }
      x++;
      System.out.println();
    }
  System.out.println();
  }
//looks for all of the bombs
  public static int valueFind(int ColNum, int RowNum, int[][] field) {
    int x = 0;
    for (int i = 0; i <= field.length - 1; i++) {
      for (int j = 0; j <= field[i].length - 1; j++) {
        if (RowNum - 1 == i || RowNum + 1 == i || RowNum == i) {
          if (ColNum - 1 == j || ColNum + 1 == j || ColNum == j) {
            if (ColNum == j && RowNum == i) {
            } else if (field[i][j] == -1) {
              x++;
            }
          }
        }
      }
    }    return x;
  }

  public static boolean winCheck(int field[][]) {
    boolean winCheck = true;
    for (int[] n : field) {
      for (int i : n) {
        if (i == -1) {
          winCheck = false;
        }
      }
    }
    return winCheck;
  }
//clears all of the zeros and all things adjacent to zero
  public static int[][] zeroClear(int field[][], int RowNum, int ColNum) {
    for (int i = 0; i <= field.length - 1; i++) {
      for (int j = 0; j <= field[i].length - 1; j++) {
        if (RowNum - 1 == i || RowNum + 1 == i || RowNum == i) {
          if (ColNum - 1 == j || ColNum + 1 == j || ColNum == j) {
            if (ColNum == j && RowNum == i) {
            }
            if (field[i][j] != 0 & field[i][j] <= 10) {
              field[i][j] = field[i][j] + 10;
            }
          }
        }
      }
    }
    return field;
  }
  //Here and on are just end of game printing stuff
  public static void flagWaste(){
    System.out.print("You wasted a flag on a spot where there wasn't a bomb! YOU LOSE!");
  }
  public static void explosionPrint() {
    System.out.println(        "          _ ._  _ , _ ._\n        (_ ' ( `  )_  .__)\n      ( (  (    )   `)  ) _)\n     (__ (_   (_ . _) _) ,__)\n         `~~`\\ ' . /`~~`\n              ;   ;\n              /   \\\n_____________/_ __ \\_____________\nYou cleared a spot where there was a bomb!");
  }
  public static void winPrint(){
    System.out.println("\n             ___________\n            '._==_==_=_.'\n            .-\\:      /-.");
    System.out.println("       | (|:.     |) |\n            '-|:.     |-'\n              \\::.    /\n               '::. .'\n                 ) (\n               _.' '._\n              `\"\"\"\"\"\"\"`");
  }
}
