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
	public void joinForm() { }

    @RequestMapping("/user/join")
	public String join(User user) {
		manager.insertUser(user);
		return "redirect:list";
	}

    @RequestMapping("/user/list")
	public ModelAndView list() {
		ModelAndView mav = new ModelAndView("/user/list");
		mav.addObject("list", manager.selectUser());
		return mav;
	}

}
