package com.ssafy.myframework.controller;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.ssafy.myframework.data.BoardManager;
import com.ssafy.myframework.model.Board;

@WebServlet("/board")
public class BoardController extends HttpServlet {

	private static final long serialVersionUID = 1L;
	
    private BoardManager manager;
    
    public BoardController() {
        manager = BoardManager.getInstance();
	}
	
	@Override
	protected void service(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		if (request.getMethod().equals("POST")) {
			request.setCharacterEncoding("UTF-8");
		}

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
            throws ServletException, IOException {
        request.getRequestDispatcher("/board/write-form.jsp").forward(request, response);
    }

    public void list(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.setAttribute("list", manager.selectBoard());
        request.getRequestDispatcher("/board/list.jsp").forward(request, response);
    }

    public void write(HttpServletRequest request, HttpServletResponse response) throws IOException {
        Board board = new Board();
        board.setTitle(request.getParameter("title"));
        board.setWriter(request.getParameter("writer"));
        manager.insertBoard(board);
        response.sendRedirect("board?act=list");
    }
    
}
