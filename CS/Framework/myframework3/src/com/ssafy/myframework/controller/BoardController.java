package com.ssafy.myframework.controller;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.web.servlet.mvc.Controller;

import com.ssafy.myframework.data.BoardManager;
import com.ssafy.myframework.model.Board;

public class BoardController implements Controller {

	private BoardManager manager;

	public BoardController() {
		manager = BoardManager.getInstance();
	}

	public String service(HttpServletRequest request, HttpServletResponse response) throws Exception {

		String viewName = null;

		String act = request.getParameter("act");
		if (act == null)
			act = "list";
		switch (act) {
		case "list":
			viewName = list(request, response);
			break;
		case "write-form":
			viewName = writeForm(request, response);
			break;
		case "write":
			viewName = write(request, response);
			break;
		}
		return viewName;
	}

	public String writeForm(HttpServletRequest request, HttpServletResponse response) throws Exception {
		return "/board/write-form.jsp";
	}

	public String list(HttpServletRequest request, HttpServletResponse response) throws Exception {
		request.setAttribute("list", manager.selectBoard());
		return "/board/list.jsp";
	}

	public String write(HttpServletRequest request, HttpServletResponse response) throws Exception {
		Board board = new Board();
		board.setTitle(request.getParameter("title"));
		board.setWriter(request.getParameter("writer"));
		manager.insertBoard(board);
		return "redirect:board?act=list";
	}
}
