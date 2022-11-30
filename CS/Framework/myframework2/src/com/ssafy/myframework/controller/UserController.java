package com.ssafy.myframework.controller;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.ssafy.myframework.data.UserManager;
import com.ssafy.myframework.model.User;

public class UserController {

	private UserManager manager;

	public UserController() {
		manager = UserManager.getInstance();
	}

	public void service(HttpServletRequest request, HttpServletResponse response) throws Exception {

		String act = request.getParameter("act");
		if (act == null)
			act = "list";
		switch (act) {
		case "list":
			list(request, response);
			break;
		case "join-form":
			joinForm(request, response);
			break;
		case "join":
			join(request, response);
			break;

		}

	}

	public void joinForm(HttpServletRequest request, HttpServletResponse response) throws Exception {
		request.getRequestDispatcher("/user/join-form.jsp").forward(request, response);
	}

	public void join(HttpServletRequest request, HttpServletResponse response) throws Exception {
		User user = new User();
		user.setId(request.getParameter("id"));
		user.setName(request.getParameter("name"));
		user.setEmail(request.getParameter("email"));
		user.setPassword(request.getParameter("password"));
		manager.insertUser(user);
		response.sendRedirect("user?act=list");
	}

	public void list(HttpServletRequest request, HttpServletResponse response) throws Exception {
		request.setAttribute("list", manager.selectUser());
		request.getRequestDispatcher("/user/list.jsp").forward(request, response);
	}

}
