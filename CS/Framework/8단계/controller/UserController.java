package com.ssafy.myframework.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import com.ssafy.myframework.data.UserManager;
import com.ssafy.myframework.model.User;

public class UserController {

    private UserManager manager;
    
    public UserController() {
        manager = UserManager.getInstance();
	}
	
    @RequestMapping("/user/join-form")
	public ModelAndView joinForm() {
	    return new ModelAndView("/user/join-form.jsp");
    }

    @RequestMapping("/user/join")
	public ModelAndView join(User user) {
		manager.insertUser(user);
		return new ModelAndView("redirect:list");
	}

    @RequestMapping("/user/list")
	public ModelAndView list() {
		ModelAndView mav = new ModelAndView("/user/list.jsp");
		mav.addObject("list", manager.selectUser());
		return mav;
	}

}
