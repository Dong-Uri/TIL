package com.ssafy.myframework.controller;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.util.WebUtil;

import com.ssafy.myframework.data.UserManager;
import com.ssafy.myframework.model.User;

public class UserController {

    private UserManager manager;
    
    public UserController() {
        manager = UserManager.getInstance();
	}
	
    @RequestMapping("/user/join-form")
	public ModelAndView joinForm(HttpServletRequest request, HttpServletResponse response)  {
	    return new ModelAndView("/user/join-form.jsp");
    }

    @RequestMapping("/user/join")
	public ModelAndView join(HttpServletRequest request, HttpServletResponse response) throws Exception {
		manager.insertUser(WebUtil.getParamToVO(request, User.class));
		return new ModelAndView("redirect:list");
	}

    @RequestMapping("/user/list")
	public ModelAndView list(HttpServletRequest request, HttpServletResponse response) {
		ModelAndView mav = new ModelAndView("/user/list.jsp");
		mav.addObject("list", manager.selectUser());
		return mav;
	}

}
