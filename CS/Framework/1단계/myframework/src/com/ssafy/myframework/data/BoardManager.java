package com.ssafy.myframework.data;

import java.util.ArrayList;
import java.util.List;

import com.ssafy.myframework.model.Board;

public class BoardManager {
    private static int seq;
    private static List<Board> boards = new ArrayList<>();
    static {
        for (int i = 0; i < 10; i++) {
            Board board = new Board("ssafy 게시물" + i, "ssafy" + i, 0);
            board.setNo(++seq);
            boards.add(board);
        }
    }
    
    private static BoardManager instance = new BoardManager();
    
    public static BoardManager getInstance() {
        return instance;
    }
    
    public List<Board> selectBoard() {
        List<Board> boards = new ArrayList<>();
        boards.addAll(BoardManager.boards);
        return boards;
    }

    public void insertBoard(Board board) {
        board.setNo(++seq);
        boards.add(board);
    }
}
