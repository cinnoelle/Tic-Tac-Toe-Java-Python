import java.util.Scanner;
public class TicTacToe {
    private static final int SIZE = 3;
    private char[][] board = new char[SIZE][SIZE];
    private char currentPlayer;
    // Constructor: initializes the board and sets the first player
    public TicTacToe() {
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                board[i][j] = '-';
            }
        }
        currentPlayer = 'X'; // Player 1 starts
    }

    // Display the current state of the board
    public void displayBoard() {
        for (int i = 0; i<SIZE; i++) {
        	for (int j = 0; j < SIZE; j++) {
        		System.out.print(board[i][j] + " ");
        	}
        	System.out.println();
        }
    }

    // Place a move on the board
    public boolean makeMove(int row, int col) {
        if (row < 0 || row >= SIZE || col < 0 || col >= SIZE) {
        	System.out.println("Invalid position. Try again.");
        	return false;
        }
        
        if (board[row][col] != '-') {
        	System.out.println("That spot is taken. Try again.");
        	return false;
        }
        board[row][col] = currentPlayer;
        return true;
    }

    // Check if the current player has won
    public boolean checkWinner() {
        for (int i = 0; i < SIZE; i++) {
        	if (board[i][0] == currentPlayer && board[i][1] == currentPlayer && board[i][2] == currentPlayer) {
        		return true;
        	}
        }
        
        for (int i = 0; i < SIZE; i++) {
        	if (board[0][i] == currentPlayer && board[1][i] == currentPlayer && board[2][i] == currentPlayer) {
        		return true;
        	}
        }
        
        
        if (board[0][0] == currentPlayer && board[1][1] == currentPlayer && board[2][2] == currentPlayer) {
        	return true;
        	
        }
        
        if (board[0][2] == currentPlayer && board[1][1] == currentPlayer && board[2][0] == currentPlayer) {
        	return true;
        }
        
        return false;
        
       
        
        
        
    }

    // Check if the board is completely filled (draw condition)
    public boolean isBoardFull() {
        for (int i = 0; i < SIZE; i++) {
        	for (int j = 0; j<SIZE; j++) {
        		if (board[i][j] == '-') {
        			return false;
        		}
        	}
        }
        return true;
    }

    // Switch the current player
    public void switchPlayer() {
        currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        TicTacToe game = new TicTacToe();

        boolean gameWon = false;
        System.out.println("Welcome to Tic-Tac-Toe!");
        game.displayBoard();
        

        // Main game loop
        while (!gameWon && !game.isBoardFull()) {
            System.out.print("Player " + (game.currentPlayer == 'X' ? "1 (X) " : "2 (O)") + ", enter your move (row and column): ");
            
            if (!scanner.hasNextInt()) {
            	System.out.println("Invalid input. Try again.");
            	scanner.next();
            	continue;	
            }
            int row = scanner.nextInt();
            
            if (!scanner.hasNextInt()) {
            System.out.println("Invalid input. Try again.");
            scanner.next();
            continue;
            }
            
            int col = scanner.nextInt();
            
            boolean moveMade = game.makeMove(row, col);
            
            
            if(moveMade) {
            	game.displayBoard();
            	gameWon = game.checkWinner();
            	
            	if (gameWon) {
            		System.out.println("Player " + (game.currentPlayer == 'X' ? "1 (X)" : "2 (O)") + " wins!");
            	}
            	else { 
            		game.switchPlayer();
            	}
            }
            
          if (!gameWon && game.isBoardFull()) {
        	  System.out.println("It's a draw!");
          }
            
        }
        
        
        
        scanner.close();
    }
}
