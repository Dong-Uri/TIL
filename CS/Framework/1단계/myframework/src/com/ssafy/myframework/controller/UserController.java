package com.ssafy.myframework.controller;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.ssafy.myframework.data.UserManager;
import com.ssafy.myframework.model.User;

@WebServlet("/user")
public class UserController extends HttpServlet {

	private static final long serialVersionUID = 1L;
	
    private UserManager manager;
    
    public UserController() {
        manager = UserManager.getInstance();
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
		case "join-form":
		    joinForm(request, response);
			break;
		case "join":
		    join(request, response);
			break;

		}

	}

	public void joinForm(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
	    request.getRequestDispatcher("/user/join-form.jsp").forward(request, response);
    }

	public void join(HttpServletRequest request, HttpServletResponse response) throws IOException {
		User user = new User();
		user.setId(request.getParameter("id"));
		user.setName(request.getParameter("name"));
		user.setEmail(request.getParameter("email"));
		user.setPassword(request.getParameter("password"));
		manager.insertUser(user);
		response.sendRedirect("user?act=list");
	}

	public void list(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setAttribute("list", manager.selectUser());
		request.getRequestDispatcher("/user/list.jsp").forward(request, response);
	}

}
