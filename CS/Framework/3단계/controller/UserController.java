package com.ssafy.myframework.controller;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.web.servlet.mvc.Controller;

import com.ssafy.myframework.data.UserManager;
import com.ssafy.myframework.model.User;

public class UserController implements Controller {

    private UserManager manager;
    
    public UserController() {
        manager = UserManager.getInstance();
	}
	
	public String service(HttpServletRequest request, HttpServletResponse response)
			throws Exception {

		String viewName = null;
		
		String act = request.getParameter("act");
		if (act == null) act = "list";
		switch (act) {
		case "list":
			viewName = list(request, response);
			break;
		case "join-form":
			viewName = joinForm(request, response);
			break;
		case "join":
			viewName = join(request, response);
			break;

		}
		
		return viewName;
	}

	public String joinForm(HttpServletRequest request, HttpServletResponse response) throws Exception {
	    return "/user/join-form.jsp";
    }

	public String join(HttpServletRequest request, HttpServletResponse response) throws Exception {
		User user = new User();
		user.setId(request.getParameter("id"));
		user.setName(request.getParameter("name"));
		user.setEmail(request.getParameter("email"));
		user.setPassword(request.getParameter("password"));
		manager.insertUser(user);
		return "redirect:user?act=list";
	}

	public String list(HttpServletRequest request, HttpServletResponse response) throws Exception {
		request.setAttribute("list", manager.selectUser());
		return "/user/list.jsp";
	}

}
