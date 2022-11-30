package com.ssafy.myframework.controller;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.ssafy.myframework.data.BoardManager;
import com.ssafy.myframework.model.Board;

public class BoardController{

    private BoardManager manager;
    
    public BoardController() {
        manager = BoardManager.getInstance();
	}
	
	public void service(HttpServletRequest request, HttpServletResponse response)
			throws Exception {

		String act = request.getParameter("act");
		if (act == null) act = "list";
		switch (act) {
		case "list":
			list(request, response);
			break;
		case "write-form":
		    writeForm(request, response);
			break;
		case "write":
		    write(request, response);
			break;

		}
	}

	public void writeForm(HttpServletRequest request, HttpServletResponse response)
            throws Exception {
        request.getRequestDispatcher("/board/write-form.jsp").forward(request, response);
    }

    public void list(HttpServletRequest request, HttpServletResponse response) throws Exception {
        request.setAttribute("list", manager.selectBoard());
        request.getRequestDispatcher("/board/list.jsp").forward(request, response);
    }

    public void write(HttpServletRequest request, HttpServletResponse response) throws Exception {
        Board board = new Board();
        board.setTitle(request.getParameter("title"));
        board.setWriter(request.getParameter("writer"));
        manager.insertBoard(board);
        response.sendRedirect("board?act=list");
    }
    
}
