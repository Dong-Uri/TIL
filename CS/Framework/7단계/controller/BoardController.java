package com.ssafy.myframework.controller;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.util.WebUtil;

import com.ssafy.myframework.data.BoardManager;
import com.ssafy.myframework.model.Board;

public class BoardController {

    private BoardManager manager;
    
    public BoardController() {
        manager = BoardManager.getInstance();
	}
	
    @RequestMapping("/board/write-form")
	public ModelAndView writeForm(HttpServletRequest request, HttpServletResponse response) {
		return new ModelAndView("/board/write-form.jsp");
    }

    @RequestMapping("/board/list")
    public ModelAndView list(HttpServletRequest request, HttpServletResponse response) {
    	ModelAndView mav = new ModelAndView("/board/list.jsp");
    	mav.addObject("list", manager.selectBoard());
        return mav;
    }

    @RequestMapping("/board/write")
    public ModelAndView write(HttpServletRequest request, HttpServletResponse response) throws Exception {
        manager.insertBoard(WebUtil.getParamToVO(request, Board.class));
        return new ModelAndView("redirect:list");
    }
}
