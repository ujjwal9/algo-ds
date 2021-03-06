public class Spot { 
    Piece piece; 
    int x; 
    int y;
}

public abstract class Piece { 
    boolean killed = false; 
    boolean white = false; 
}

public class King extends Piece { 
    private boolean castlingDone = false; 
    public King(boolean white) { 
        super(white); 
    }  
  
    @Override
    public boolean canMove(Board board, Spot start, Spot end) 
    { 
        if (end.getPiece().isWhite() == this.isWhite()) { 
            return false; 
        } 
  
        int x = Math.abs(start.getX() - end.getX()); 
        int y = Math.abs(start.getY() - end.getY()); 
        if (x + y == 1) { 
            // check if this move will not result in the king 
            // being attacked if so return true 
            return true; 
        } 
  
        return this.isValidCastling(board, start, end); 
}

//Similarly we can design for  Queen, Pawns, Rooks, Bishops etc.
public class Board { 
    Spot[][] boxes; 
  
    public Board() 
    { 
        this.resetBoard(); 
    } 
  
    public Spot getBox(int x, int y) 
    { 
  
        if (x < 0 || x > 7 || y < 0 || y > 7) { 
            throw new Exception("Index out of bound"); 
        } 
  
        return boxes[x][y]; 
    } 
  
    public void resetBoard() 
    { 
        // initialize white pieces 
        boxes[0][0] = new Spot(0, 0, new Rook(true)); 
        boxes[0][1] = new Spot(0, 1, new Knight(true)); 
        boxes[0][2] = new Spot(0, 2, new Bishop(true)); 
        //... 
        boxes[1][0] = new Spot(1, 0, new Pawn(true)); 
        boxes[1][1] = new Spot(1, 1, new Pawn(true)); 
        //... 
  
        // initialize black pieces 
        boxes[7][0] = new Spot(7, 0, new Rook(false)); 
        boxes[7][1] = new Spot(7, 1, new Knight(false)); 
        boxes[7][2] = new Spot(7, 2, new Bishop(false)); 
        //... 
        boxes[6][0] = new Spot(6, 0, new Pawn(false)); 
        boxes[6][1] = new Spot(6, 1, new Pawn(false)); 
        //... 
  
        // initialize remaining boxes without any piece 
        for (int i = 2; i < 6; i++) { 
            for (int j = 0; j < 8; j++) { 
                boxes[i][j] = new Spot(i, j, null); 
            } 
        } 
    } 
} 

public abstract class Player { 
    public boolean whiteSide; 
    public boolean humanPlayer; 
} 
  
public class HumanPlayer extends Player { 
} 
  
public class ComputerPlayer extends Player {  
}

public class Move { 
    private Player player; 
    private Spot start; 
    private Spot end; 
    private Piece pieceMoved; 
    private Piece pieceKilled; 
  
    public Move(Player player, Spot start, Spot end) 
    { 
        this.player = player; 
        this.start = start; 
        this.end = end; 
        this.pieceMoved = start.getPiece(); 
    } 
}

public enum GameStatus { 
    ACTIVE, 
    BLACK_WIN, 
    WHITE_WIN, 
    FORFEIT, 
    STALEMATE, 
    RESIGNATION 
}

public class Game { 
    private Player[] players; 
    private Board board; 
    private Player currentTurn; 
    private GameStatus status; 
    private List<Move> movesPlayed; 
  
    private void initialize(Player p1, Player p2) 
    { 
        players[0] = p1; 
        players[1] = p2; 
  
        board.resetBoard(); 
  
        if (p1.isWhiteSide()) { 
            this.currentTurn = p1; 
        } 
        else { 
            this.currentTurn = p2; 
        } 
  
        movesPlayed.clear(); 
    } 
  
    public boolean isEnd() 
    { 
        return this.getStatus() != GameStatus.ACTIVE; 
    } 
  
    public boolean playerMove(Player player, int startX,  
                                int startY, int endX, int endY) 
    { 
        Spot startBox = board.getBox(startX, startY); 
        Spot endBox = board.getBox(startY, endY); 
        Move move = new Move(player, startBox, endBox); 
        return this.makeMove(move, player); 
    } 
  
    private boolean makeMove(Move move, Player player) 
    { 
        Piece sourcePiece = move.getStart().getPiece(); 
        if (sourcePiece == null) { 
            return false; 
        } 
  
        // valid player 
        if (player != currentTurn) { 
            return false; 
        } 
  
        if (sourcePiece.isWhite() != player.isWhiteSide()) { 
            return false; 
        } 
  
        // valid move? 
        if (!sourcePiece.canMove(board, move.getStart(),  
                                            move.getEnd())) { 
            return false; 
        } 
  
        // kill? 
        Piece destPiece = move.getStart().getPiece(); 
        if (destPiece != null) { 
            destPiece.setKilled(true); 
            move.setPieceKilled(destPiece); 
        } 
  
        // castling? 
        if (sourcePiece != null && sourcePiece instanceof King 
            && sourcePiece.isCastlingMove()) { 
            move.setCastlingMove(true); 
        } 
  
        // store the move 
        movesPlayed.add(move); 
  
        // move piece from the stat box to end box 
        move.getEnd().setPiece(move.getStart().getPiece()); 
        move.getStart.setPiece(null); 
  
        if (destPiece != null && destPiece instanceof King) { 
            if (player.isWhiteSide()) { 
                this.setStatus(GameStatus.WHITE_WIN); 
            } 
            else { 
                this.setStatus(GameStatus.BLACK_WIN); 
            } 
        } 
  
        // set the current turn to the other player 
        if (this.currentTurn == players[0]) { 
            this.currentTurn = players[1]; 
        } 
        else { 
            this.currentTurn = players[0]; 
        } 
  
        return true; 
    } 
} 