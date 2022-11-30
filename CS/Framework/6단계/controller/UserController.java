package com.ssafy.myframework.controller;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.Controller;
import org.springframework.web.util.WebUtil;

import com.ssafy.myframework.data.UserManager;
import com.ssafy.myframework.model.User;

public class UserController implements Controller {

    private UserManager manager;
    
    public UserController() {
        manager = UserManager.getInstance();
	}
	
	public ModelAndView service(HttpServletRequest request, HttpServletResponse response)
			throws Exception {

		ModelAndView mav = null;
		
		String act = request.getParameter("act");
		if (act == null) act = "list";
		switch (act) {
		case "list":
			mav = list(request, response);
			break;
		case "join-form":
			mav = joinForm(request, response);
			break;
		case "join":
			mav = join(request, response);
			break;
		}
		
		return mav;
	}

	public ModelAndView joinForm(HttpServletRequest request, HttpServletResponse response) throws Exception {
	    return new ModelAndView("/user/join-form.jsp");
    }

	public ModelAndView join(HttpServletRequest request, HttpServletResponse response) throws Exception {
		manager.insertUser(WebUtil.getParamToVO(request, User.class));
		return new ModelAndView("redirect:user?act=list");
	}

	public ModelAndView list(HttpServletRequest request, HttpServletResponse response) throws Exception {
		ModelAndView mav = new ModelAndView("/user/list.jsp");
		mav.addObject("list", manager.selectUser());
		return mav;
	}

}
